from django.urls import path, include
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.store, name='home'),
    path('<slug:slug>/', views.store, name='product_by_category'),
    path('<slug:slug>/<slug:product_slug>/', views.product_detail, name='single_product'),
]

