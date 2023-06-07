from django.urls import path

from .views import Items, ShoppingCart

app_name = 'webstore'

urlpatterns = [
    path('', Items.as_view(), name='index'),
    path('shoppingcart/<int:product_id>/user/<int:user_id>/', ShoppingCart.as_view(), name='shoppingcart'),
]