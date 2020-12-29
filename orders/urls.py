from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("checkout", views.view_checkout, name="checkout"),
    path("success", views.success, name="success"),
    path("cancelled", views.cancelled, name="cancelled"),
    path("create-checkout-session", views.create_checkout_session, name="create_checkout_session"),
    path("<str:food_category>/<int:food_pk>", views.add_to_cart, name="add_to_cart"),
    path('config/', views.stripe_config),  # new
]
