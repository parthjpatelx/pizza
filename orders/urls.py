from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("checkout", views.view_checkout, name="checkout"),
    path("create-checkout-session", views.create_checkout_session, name="create_checkout_session"),
    path("<str:food_category>/<int:food_pk>", views.add_to_cart, name="add_to_cart")
]
