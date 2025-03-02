#Url app_utama
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('tryout/', list_data, name='tryout'),
    path('add/', add_data, name='add_data'),
    path('edit/<int:id>/', edit_data, name='edit_data'),
    path('delete/<int:id>/', delete_data, name='delete_data')
]