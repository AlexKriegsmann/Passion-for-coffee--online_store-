from django.urls import path

from address import views

urlpatterns = [
    path('create_address/', views.AddressCreateView.as_view(), name='create_address'),

]