from django.urls import path
from .views import cart_detail, cart_remove, cart_add, update_cart, clear_cart

urlpatterns = [
    path('', cart_detail, name = 'cart_detail'),
    path('add/<int:phone_id>/', cart_add, name = 'cart_add'),
    path('remove/<int:phone_id>/', cart_remove, name = 'cart_remove'),
    path('update/<int:phone_id>/', update_cart, name = 'update_cart'),
    path('clear_cart/', clear_cart, name='clear_cart'),
]