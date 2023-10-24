from django.urls import path

from orders import views

urlpatterns = [
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('add_to_wishlist/<int:pk>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('list_products/', views.CartListView.as_view(), name='list_products')
]