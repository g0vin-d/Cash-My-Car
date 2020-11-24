from django.urls import path
from . import views
from .views import (
    NewCarListView,
    OldCarListView,
    CarDetailView,
    CarCreateView,
    CarUpdateView,
    PostDeleteView
)

urlpatterns = [
    path('', views.home, name="store-home"),
    path('newcar/', NewCarListView.as_view(), name="store-newcar"),
    path('oldcar/', OldCarListView.as_view(), name="store-oldcar"),
    path('sellcar/', views.sellacar, name="store-sellcar"),
    path('car/<int:pk>/', CarDetailView.as_view(), name="car-detail"),
    path('car/<int:pk>/update/', CarUpdateView.as_view(), name="car-update"),
    path('car/<int:pk>/delete/', PostDeleteView.as_view(), name="car-delete"),
    path('car/new/', CarCreateView.as_view(), name="car-create"),
    path('estimate', views.estimate, name="store-estimate"),
]
