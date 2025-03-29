from django.urls import path
from .views import homeView,aboutView,ProductDetails,AddProduct,UpdateProduct,DeleteProduct,searchView

urlpatterns = [
    path("",homeView,name="home"),
    path("about",aboutView, name="aboutPage"),
    path('products/<int:pk>',ProductDetails.as_view(),name='prod_details'),
    path('products/add',AddProduct.as_view(),name='add_prod'),
    path('products/edit/<int:pk>',UpdateProduct.as_view(),name='edit_prod'),
    path('products/del/<int:pk>',DeleteProduct.as_view(),name='del_prod'),
    path('products/search',searchView,name='search')
]