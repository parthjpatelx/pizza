from django.http import HttpResponse
from django.shortcuts import render
from orders.models import *
import json
# Create your views here.

food_strings = ["regularpizza", "sicilianpizza", "salad","dinnerplatter", "pasta"]

REGULAR_PIZZA_IDX = 0
SICILIAN_PIZZA_IDX = 1
SALAD_IDX = 2
PLATTER_IDX = 3
PASTA_IDX = 4


def get_all_objects_from_string(food_category):
    if food_category ==  food_strings[REGULAR_PIZZA_IDX]:
        return Regular_Pizza.objects.all()
    elif food_category == food_strings[SICILIAN_PIZZA_IDX]:
        return Sicilian_pizza.objects.all()
    elif food_category == food_strings[SALAD_IDX]:
        return Salad.objects.all()
    elif food_category == food_strings[PLATTER_IDX]:
        return Dinner_platter.objects.all()
    elif food_category == food_strings[PASTA_IDX]:
        return Pasta.objects.all()

def get_object_from_string(food_category, food_pk):
    if food_category == 'regularpizza':
        food_object = Regular_Pizza.objects.get(pk = food_pk)

    if food_category == "sicilianpizza":
        food_object = Sicilian_pizza.objects.get(pk=food_pk)

    return food_object


def convert_key_to_objects(current_cart):
    cart_food_objects = []

    for food_category in current_cart:
        for id in current_cart[food_category]:
            quantity = current_cart[food_category][id]

            if quantity > 0:
                food_object = get_object_from_string(food_category, id)
                cart_food_objects.append(food_object)

    return cart_food_objects




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

    if food_category not in food_strings:
        return render(request, "orders/error.html", {"message": "Invalid food."})

    try:
         Food.objects.get(pk = food_pk)
    except KeyError:
        return render(request, "orders/error.html", {"message": "Key error"})


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
    cart_food_objects = convert_key_to_objects(current_cart)

    context = {
        "cart" : cart_food_objects
    }

    return render(request, "orders/cart.html",context)


# def submit_order(request):
#     check if user has any items in his cart
#     current_cart = request.session['cart']
#     #convert all the keys into objects
#     #add the objects to the cart
#     #as you add each object, calculate Price
