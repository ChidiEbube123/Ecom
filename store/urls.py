from django.urls import path
from django.shortcuts import redirect,render
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("about/",views.about,name="about"),
    path("login/", views.login_user, name="login_user"),
    path("logout/", views.logout_user, name="logout_user"),
    path("register/", views.register_user, name="register_user"),
    path("products/<int:pk>/",views.products, name="product"),
    path("category/<str:foo>/",views.category,name="category"),
    path("update_user/", views.update_user, name="update_user"),
    path("update_profile/", views.update_profile, name="update_profile"),
    path("update_password/", views.update_password, name="update_password"),
    path("product_search/",views.product_search, name="product_search")

#int primary key

]