from django.urls import path
from .views import store, cart, checkout, update_item

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('update-item/', update_item, name='update_item'),
    path('', store, name='store'),
]
