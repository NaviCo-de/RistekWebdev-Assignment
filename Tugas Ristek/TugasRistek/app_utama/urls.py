#Url app_utama
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('tryout/', list_data, name='tryout'),

    path('<str:judul_tryout>/<int:id>/add_question/', add_question, name='add_question'),
    path('<str:judul_tryout>/<int:id>/<int:nomor_pertanyaan>/edit_question/', edit_question, name='edit_question'),
    path('<str:judul_tryout>/<int:id>/<int:nomor_pertanyaan>/delete_question/', delete_question, name='delete_question'),

    path('add/', add_data, name='add_data'),
    path('<str:judul_tryout>/<int:id>/', detail_data, name='detail_data'),
    path('edit/<int:id>/', edit_data, name='edit_data'),
    path('delete/<int:id>/', delete_data, name='delete_data'),
]