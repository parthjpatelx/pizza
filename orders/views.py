from django.http import HttpResponse
from django.shortcuts import render
from orders.models import *
# Create your views here.


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
      else:
          return render(request, "users/login.html", {"message": "Invalid credentials."})


def add_to_cart(request):
    pass
