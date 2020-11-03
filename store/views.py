from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'store/index.html')


def sellacar(request):
    return render(request, 'store/sell_a_car.html')


def newcar(request):
    return render(request, 'store/new_car.html')


def oldcar(request):
    return render(request, 'store/old_car.html')
