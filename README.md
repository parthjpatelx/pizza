# Project 3

Web Programming with Python and JavaScript

TODO:
-add data-set to index.html with pk of each food (use class to label food) x
-string representation of pizza x
-create pizza objects in admin x
-confirm we can access id attribute x (yes)
-ensure # of toppings is greater than 0

- view function- pass in menu objects to index.HTML

- implement HTML for login, passing in message
- implement HTML for error page, passing in message
- assign the ul class to the parent


when the user clicks on the link, pass in the pk of the food as well as object Type
at the server side, use a query to get the corresponding object given pk

when you are making the html template for the menu, make sure you are including the pk of in the html data-set. How are we going to get the food type as well? (pass in via dict?)

add object to a temp array called temp_cart- should be associated with cookie or request object

once the user is ready to submit the order, create a cart object

make sure to clear temp cart when a new cart is submitted

two views functions:
- add to CART
- submit cart

Javascript AJAX request called send_to_cart
  send post request to add_to_cart function
    https://www.w3schools.com/js/js_ajax_http_send.asp
  pass in the following using  JSON dict
    pk of food
    food type
  user should be confirmed server-side
















Django notes:

flst = FollowerList.objects.create(follower=user)
flst.followed.add(user)
from django.contrib.auth.models import User

from orders.models import *
from django.conf import settings
from django.contrib.auth.models import User

current_user = User.objects.get(pk=1)
large = Size.objects.get(pk=1)
new_pizza = Regular_Pizza(size=large, price = 10.50, number_toppings = 3)
new_pizza.save()
my_cart = Cart(user=current_user)
my_cart.save()
my_cart.items_in_cart.add(new_pizza)
