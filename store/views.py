from django.shortcuts import render
from .models import Car
from django.http import JsonResponse
import json
import numpy as np
import sklearn
import jsonify
import pickle
from sklearn.preprocessing import StandardScaler
import os
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# load Car_prediction model
model = pickle.load(open(os.path.join(os.getcwd(),
                                      'random_forest_regression_model.pkl'), 'rb'))

standard_to = StandardScaler()

# Create your views here.
context = {
    'cars': Car.objects.all()
}


def home(request):
    tourSection = {'cars': Car.objects.all()[:6]}
    return render(request, 'store/index.html', tourSection)


# def newcar(request):
#     return render(request, 'store/new_car.html', context)


# def oldcar(request):
#     return render(request, 'store/old_car.html', context)


class NewCarListView(ListView):
    model = Car
    template_name = 'store/new_car.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'cars'
    ordering = ['-date_posted']


class CarDetailView(DetailView):
    model = Car
    template_name = 'store/car_details.html'  # <app>/<model>_<viewtype>.html


class OldCarListView(ListView):
    model = Car
    template_name = 'store/old_car.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'cars'
    ordering = ['-date_posted']


class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    fields = ['car_name', 'image', 'purchase_year', 'ex_price',
              'kms_driven', 'no_owners', 'fuel_type', 'engine', 'seats',
              'transmission', 'seller_type', 'car_type', 'selling_price']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CarUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Car
    fields = ['car_name', 'image', 'purchase_year', 'ex_price',
              'kms_driven', 'no_owners', 'fuel_type', 'engine', 'seats',
              'transmission', 'seller_type', 'car_type', 'selling_price']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        car = self.get_object()
        if self.request.user == car.user:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Car
    success_url = '/'

    def test_func(self):
        car = self.get_object()
        if self.request.user == car.user:
            return True
        return False

def sellacar(request):

    if request.method == "POST":
        car_name = request.POST['car_name']
        image = request.FILES['image']
        purchase_year = int(request.POST['purchase_year'])
        ex_price = float(request.POST['ex_price'])
        kms_driven = int(request.POST['kms_driven'])
        no_owners = int(request.POST['no_owners'])
        fuel_type = request.POST['fuel_type']
        engine = int(request.POST['engine'])
        seats = int(request.POST['seats'])
        transmission = request.POST['transmission']
        seller_type = request.POST['seller_type']
        selling_price = request.POST['selling_price']
        user = request.user
        if purchase_year == 2020 and kms_driven == 0:
            car_type = 'New'
        else:
            car_type = 'Old'

        if selling_price == '':
            selling_price = ex_price

        print([car_name, purchase_year, ex_price, kms_driven, no_owners, fuel_type,
               engine, seller_type, seats, transmission, selling_price, car_type, user])

        instance = Car(car_name=car_name, image=image, purchase_year=purchase_year,
                       ex_price=ex_price, kms_driven=kms_driven, no_owners=no_owners,
                       fuel_type=fuel_type, engine=engine, seller_type=seller_type,
                       seats=seats, transmission=transmission, car_type=car_type,
                       selling_price=selling_price, user=request.user)

        instance.save()

    return render(request, 'store/sell_a_car.html')


def estimate(request):

    if request.method == "PUT":
        print('This is a estimate method')
        data = json.loads(request.body)
        print(data)

        Year = int(data['purchase_year'])
        Present_Price = float(data['ex_price'])
        Kms_Driven = int(data['kms_driven'])
        Owner = int(data['no_owners'])
        Fuel_Type_Petrol = data['fuel_type']
        Seller_Type_Individual = data['seller_type']
        Transmission_Mannual = data['transmission']

        Year = 2020 - Year

        Fuel_Type_Diesel = 0

        print([Present_Price, Kms_Driven, Owner, Year,
               Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual])

        if(Fuel_Type_Petrol == 'Petrol'):
            Fuel_Type_Petrol = 1
            Fuel_Type_Diesel = 0
        elif(Fuel_Type_Petrol == 'Diesel'):
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 1
        else:
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 0

        if(Seller_Type_Individual == 'Individual'):
            Seller_Type_Individual = 1
        else:
            Seller_Type_Individual = 0

        if(Transmission_Mannual == 'Mannual'):
            Transmission_Mannual = 1
        else:
            Transmission_Mannual = 0

        if Year == 0 and Kms_Driven == 0:
            output = Present_Price
        else:
            prediction = model.predict([[Present_Price, Kms_Driven, Owner, Year, Fuel_Type_Diesel,
                                         Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual]])

            output = round(prediction[0], 2)

        print(output)

        return JsonResponse({
            'message': output,
            'status': 200
        }, status=200)

    return render(request, 'store/sell_a_car.html', data)
