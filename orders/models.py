from django.db import models
from django.conf import settings

# Create your models here.

#FOOD TYPES
class Type(models.Model):
    def __str__(self):
        return f"{self.type}"

    class Meta:
        abstract = True

class Platter_type(Type):
    type = models.CharField(max_length=64)

class Pasta_type(Type):
    type = models.CharField(max_length=64)

class Sub_type(Type):
    type = models.CharField(max_length=64)

class Salad_type(Type):
    type = models.CharField(max_length=64)

class Topping(Type):
    type = models.CharField(max_length=64)

class Size(models.Model):
    sizes = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.sizes}"

# FOOD CATEGORIES
class Food(models.Model):
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Size: {self.size} Price: {self.price}"


class Pizza(Food):
    number_toppings = models.IntegerField()
    topping_types = models.ManyToManyField(Topping, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"toppings: {self.number_toppings}, Price: {self.price}"

class Sicilian_pizza(Pizza):
    class Meta:
        verbose_name = "sicilianpizza"


class Regular_Pizza(Pizza):
    class Meta:
        verbose_name = "regularpizza"


class Salad(Food):
    salad_type = models.ForeignKey(Salad_type, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "salad"

class Dinner_platter(Food):
    platter_type = models.ForeignKey(Platter_type, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "dinnerplatter"

class Pasta(Food):
    pasta_type = models.ForeignKey(Pasta_type, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "pasta"


#CART
class Cart_item(models.Model):
    item = models.ForeignKey(Food, blank=True, on_delete = models.CASCADE)
    quantity = models.IntegerField()


class Cart(models.Model):
    items_in_cart = models.ManyToManyField(Cart_item, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    time = models.TimeField(auto_now=False, auto_now_add=False)
