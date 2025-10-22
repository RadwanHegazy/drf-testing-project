from . import views
from django.urls import path

urlpatterns = [
    path('product/get/', views.ListProductAPI.as_view(), name='list-product'),
    path('product/create/', views.CreateProductAPI.as_view(), name='create-product'),
    path('products/get/<int:id>/', views.RetrieveProductAPI.as_view(), name='retrieve-product'),
    path('category/get/', views.ListCategoryAPI.as_view(), name='list-category'),
    path('category/create/', views.CreateCategoryAPI.as_view(), name='create-category'),
]