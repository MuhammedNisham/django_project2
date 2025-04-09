from django.urls import path
from .import views

urlpatterns =[
    path('', views.homeView, name = 'homepage'),
    path('about', views.aboutView, name = 'aboutpage'),
    path('contact', views.ContactView, name = 'contactpage'),
    path('products/<int:pk>', views.ProductDetails.as_view(), name = 'prod_details'),
    path('products/<int:pk>', views.ProductDetails.as_view(), name = 'prod_details'),
    path('products/add', views.AddProduct.as_view(), name='add_product'),
    path('products/edit/<int:pk>', views.EditProduct.as_view(), name='edit_product'),
    path('products/del/<int:pk>', views.DelProduct.as_view(), name='del_product')
]