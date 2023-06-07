from django.urls import path

from .views import ProductCreate, ProductDetail, ProductList, ProductUpdate, ProductDelete
#from .views import UserList, UserCreate

app_name = 'webmin'

urlpatterns = [
    path('products/', ProductList.as_view(), name='product_list'),
    path('products/<int:pk>/detail/', ProductDetail.as_view(), name='product_detail'),
    path('products/create/', ProductCreate.as_view(), name='product_create'),    
    path('products/<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
    
    
    #path('users/', UserList.as_view(), name='user_list'),
    #path('users/<int:pk>/detail/', UserDetail.as_view(), name='user_detail'),
    #path('users/create/', UserCreate.as_view(), name='user_create'),    
    #path('users/<int:pk>/update/', UserUpdate.as_view(), name='user_update'),
    #path('users/<int:pk>/delete/', UserDelete.as_view(), name='user_delete'),
]