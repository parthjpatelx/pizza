from django.http import HttpResponse
from django.shortcuts import render
from orders.models import *
import json
from django.templatetags.static import static
from django.views.decorators.csrf import csrf_exempt # new
from django.http.response import JsonResponse # new
import stripe

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

def view_checkout(request):
    return render(request, "orders/checkout.html")



#taken from https://testdriven.io/blog/django-stripe-tutorial/
@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_config, safe=False)


#taken from https://testdriven.io/blog/django-stripe-tutorial/
@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:

            #take information in session key and represent it as a dict
            items = []
            request.session['cart'] = current_cart
            cart_food_objects = convert_key_to_objects(current_cart)

            for object in cart_food_objects:
                temp_dict = {
                    'name': object,
                    'quantity': 1,
                    'currency': 'usd',
                    'amount': object.price,
                }

                items.append(temp_dict)


            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items= items
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})

def success(request):
    return render(request, "orders/success.html")

def cancelled(request):
    return render(request, "orders/cancelled.html")
