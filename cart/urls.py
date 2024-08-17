from django.urls import path
from .views import *
urlpatterns = [
    path("", cart_home,name="cart_home"),
    path("add/",cart_add, name="cart_add"),
    path("delete/",cart_delete, name="cart_delete"),
    path("update/", cart_qty_update, name="cart_qty_update")
]
