from django.urls import path
from . import views

urlpatterns = [
    path('cartDetails', views.cart_details, name='cartDetails'),
    path('addcart/<int:product_id>', views.add_Cart, name='addcart'),
    path('dec/<int:product_id>', views.min_cart, name='dec'),
    path('remove/<int:product_id>', views.cart_delete, name='remove')
]
