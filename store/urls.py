from django.urls import path, include
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.store, name='home'),
    path('<slug:slug>/', views.store, name='product_by_category'),
]

