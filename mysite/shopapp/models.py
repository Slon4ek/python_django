from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Product(models.Model):
    """
    Represents a product in the shop.

    Attributes:
        name (str): The name of the product, up to 100 characters.
        price (Decimal): The price of the product, with up to 10 digits and 2 decimal places, defaults to 0.
        quantity (int): The quantity of the product available.
        description (str): A detailed description of the product.
        discount (int): The discount percentage for the product, defaults to 0.
        created_at (datetime): The timestamp when the product was created, set automatically.
        updated_at (datetime): The timestamp when the product was last updated, set automatically.
    """

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.IntegerField()
    description = models.TextField()
    discount = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    """
    Represents an order in the shop.

    Attributes:
        delivery_address (TextField): The delivery address for the order. Can be null or blank.
        promocode (CharField): A promotional code applied to the order, up to 10 characters. Can be null or blank.
        user (ForeignKey): The user who placed the order. Related to the User model. Protected from deletion.
        quantity (IntegerField): The quantity of items in the order. Cannot be null, defaults to 1.
        created_at (DateTimeField): The timestamp when the order was created. Automatically set on creation.
        updated_at (DateTimeField): The timestamp when the order was last updated. Automatically updated on save.
        products (ManyToManyField): The products included in the order. Related to the Product model.
        total_price (DecimalField): The total price of the order. Max 10 digits with 2 decimal places, defaults to 0.
    """

    delivery_address = models.TextField(null=True, blank=True)
    promocode = models.CharField(max_length=10, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders')
    quantity = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(Product, related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)