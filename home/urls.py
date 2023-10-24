from django.urls import path, include

from home import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home_page'),
    path('', include('userextend.urls'))
]