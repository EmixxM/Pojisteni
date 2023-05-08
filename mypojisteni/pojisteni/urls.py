from django.urls import path

from pojisteni import views


urlpatterns = [
    path('', views.seznam_pojistenych, name='seznam_pojistenych'),
    path('pojisteny/<int:pk>/', views.detail_pojisteneho, name='detail_pojisteneho'),
    path('pojisteni/novy/', views.novy_pojisteny, name='novy_pojisteny'),
]