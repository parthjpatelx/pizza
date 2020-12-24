from django.http import HttpResponse
from django.shortcuts import render
from orders.models import *
import json
# Create your views here.

def get_all_objects_from_string(food_category):
    if food_category == "regularpizza":
        return Regular_Pizza.objects.all()
    if food_category == "sicilianpizza":
        return Sicilian_pizza.objects.all()


def get_object_from_string(food_category, food_pk):
    if food_category == 'regularpizza':
        food_object = Regular_Pizza.objects.get(pk = food_pk)

    if food_category == "sicilianpizza":
        food_object = Sicilian_pizza.objects.get(pk=food_pk)

    return food_object


def index(request):
    context = {
        "regular_pizzas" : Regular_Pizza.objects.all()
    }
    return render(request, "orders/index.html", context)


def login(request):
      username = request.POST["username"]
      password = request.POST["password"]
      user = authenticate(request, username=username, password=password)
      if user is not None:
          login(request, user)
          return HttpResponseRedirect(reverse("index"))
          request.session['has_cart'] = False
          request.session['cart'] = {}
      else:
          return render(request, "users/login.html", {"message": "Invalid credentials."})


def add_to_cart(request, food_category, food_pk):

    request.session['cart'] = {}
    current_cart = request.session['cart']

    #add all menu items for corresponding food category to cart, set q = 0
    if food_category not in current_cart:
        current_cart[food_category] = {}

        food_objects = get_all_objects_from_string(food_category)

        for food in food_objects:
            current_cart[food_category][food.id] = 0


    #update quantity and cart
    current_cart[food_category][food_pk] += 1
    request.session['cart'] = current_cart

    #convert food string/id stored in session dict into objects
    cart_food_objects = []

    list_of_categories = list(current_cart)
    number_of_categories = len(list_of_categories)

    for category_idx in range(number_of_categories):
        food_category = list_of_categories[category_idx]

        list_of_food_ids = list(current_cart[food_category])
        number_of_food_ids = len(list_of_food_ids)

        for id_idx in range(number_of_food_ids):
            id = list_of_food_ids[id_idx]

            quantity = current_cart[food_category][id]
            if quantity > 0:
                food_object = get_object_from_string(food_category, id)
                cart_food_objects.append(food_object)



    context = {
        "cart" : cart_food_objects
    }

    return render(request, "orders/cart.html",context)
