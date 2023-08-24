from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('concern/', views.concern, name='concern'),
    path('thankyou/', views.thankyou, name='thankyou'),
]
