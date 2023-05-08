from django.urls import path

from . import views

urlpatterns = [
    path('', views.seznam_pojistenych, name='seznam_pojistenych'),
    path('pojisteny/<int:pk>/', views.detail_pojisteneho, name='detail_pojisteneho'),
]