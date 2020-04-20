from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(template_name='fooddb/userLogin.html'), name='Login'),
    path('home/', LoginView.as_view(template_name='fooddb/home.html'), name='home'),
    path('menu/', views.menu_view, name='menu'),
    path('orderPage/', views.order_page_view, name = 'orderPage'),
    path('orderDisplay/', views.order_display_view, name = 'orderDisplay'),
]