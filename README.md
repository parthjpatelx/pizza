# Project 3

Web Programming with Python and JavaScript



#SERVER TODO

#figure out a way to add specific toppings to pizza

#figure out how to represent quantity
      if we represent the individual foods as general food objects, will this slice off their individual properties? See what happens. How do we avoid this? Read python the hard way OOP section

#remove API key from source ```

```

# create a submit order function

#modify add_to_cart to iterate over dict directly

# make sure user has to be logged in to access each view

# delete the empty cart assignment in add_to_cart so that user can add multiple items to cart

#edit models.py so that all foods have a corresponding string representation

#set up register view
    note when we register a new user, make sure to set active cart to False

#Compacting two definitions at top
     Figure out how to use meta properties of objects to refer to them. If we return a food query, will it slice off properties?->Probably yes. How can we avoid this?
    foods_for_my_category = Food.objects.filter(string_name = food_category)










#HTML TODO
- each link in list should link to /<food_type>/<pk> which should be linked ot add_to_cart
- create login.html
- create a carts html page
-change add_to_cart view so that cart shows up on index page


#JAVASCRIPT TODO



if food_category == "regularpizza":
    new_food = Regular_Pizza.objects.get(pk = food_pk)


    # request.session['cart'] = current_cart






        checkoutButton.addEventListener("click", function () {
            fetch("/create-checkout-session", {
              method: "POST",
            })
            .then(function (response) {
              return response.json();
            })
            .then(function (session) {
              return stripe.redirectToCheckout({ sessionId: session.id });
            })
            .then(function (result) {
              // If redirectToCheckout fails due to a browser or network
              // error, you should display the localized error message to your
              // customer using error.message.
              if (result.error) {
                alert(result.error.message);
              }
            })
            .catch(function (error) {
              console.error("Error:", error);
            });
        });













Design:

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
