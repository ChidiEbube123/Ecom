from django.urls import path
from .views import *
urlpatterns = [
    path('', payment_success, name="payment_success"),
    path('checkout/', checkout, name="checkout"),
    path('purchase/', purchase, name="purchase"),
    path('order_success/', order_success, name="order_success")
]
