from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("<str:food_category>/<int:food_pk>", views.add_to_cart, name="add_to_cart")
]
