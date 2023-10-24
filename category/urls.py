from django.urls import path

from category import views


urlpatterns = [
    path('create_category/', views.CategoryCreateView.as_view(), name='create_category'),
    path('list_of_categories/', views.CategoryListView.as_view(), name='list_of_categories'),
    path('update_category/<int:pk>/', views.CategoryUpdateView.as_view(), name='update_category'),
    path('delete_category/<int:pk>/', views.CategoryDeleteView.as_view(), name='delete_category'),
    path('detail_category/<int:pk>/', views.CategoryDetailView.as_view(), name='detail_category'),



]