from django.urls import path

from pojisteni import views


urlpatterns = [
    path('', views.seznam_pojistenych, name='seznam_pojistenych'),
    path('pojisteny/<int:pk>/', views.detail_pojisteneho, name='detail_pojisteneho'),
    path('pojisteni/novy/', views.novy_pojisteny, name='novy_pojisteny'),
    path('pojisteny/<int:pk>/pridat/', views.pridat_pojisteni, name='pridat_pojisteni'),
    path('pojisteny/<int:pk>/editovat/', views.editovat_pojisteneho, name='editovat_pojisteneho'),
    path('pojisteny/<int:pk>/odstranit/', views.odstranit_pojisteneho, name='odstranit_pojisteneho'),
    path('pojisteni/<int:pk>/editovat/', views.editovat_pojisteni, name='editovat_pojisteni'),
    path('pojisteni/<int:pk>/odstranit/', views.odstranit_pojisteni, name='odstranit_pojisteni'),

]