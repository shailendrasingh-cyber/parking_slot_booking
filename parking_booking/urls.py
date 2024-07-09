from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('booking/', views.booking, name='booking'),
    path('ticket/<int:booking_id>/', views.ticket, name='ticket'),
]
