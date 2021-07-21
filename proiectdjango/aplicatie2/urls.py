from django.urls import path
from aplicatie2 import views

app_name = 'aplicatie2'
urlpatterns = [
    path('adaugare/', views.CreateLocationView.as_view(), name='adauga'),
    path('', views.ListLocationView.as_view(), name='listare'),
    path('modificare/<int:pk>/', views.UpdateLocationView.as_view(), name='modifica'),
]