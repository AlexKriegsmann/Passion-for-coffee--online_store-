from django.urls import path

from product import views

urlpatterns = [
    path('create_product/', views.ProductCreateView.as_view(), name='create_product'),
    path('list_of_products/', views.ProductListView.as_view(), name='list_of_products'),
    path('update_product/<int:pk>/', views.ProductUpdateView.as_view(), name='update_product'),
    path('delete_product/<int:pk>/', views.ProductDeleteView.as_view(), name='delete_product'),
    path('detail_product/<int:pk>', views.ProductDetailView.as_view(), name='detail_product'),
    path('products_per_category/<int:pk>/', views.get_all_products_per_category, name='product-per-category')


]