from django.core.management import BaseCommand

from shopapp.models import Product


class Command(BaseCommand):
    """
    Create products
    """
    def handle(self, *args, **options):
        self.stdout.write('Creating products...')

        products = [
            {'name': 'Laptop', 'price': 1000, 'quantity': 10, 'description': 'Laptop description'},
            {'name': 'Mobile', 'price': 500, 'quantity': 20, 'description': 'Mobile description'},
            {'name': 'Tablet', 'price': 700, 'quantity': 0, 'description': 'Tablet description'},
            {'name': 'Desktop', 'price': 2000, 'quantity': 5, 'description': 'Desktop description'},
        ]
        for product in products:
            Product.objects.get_or_create(**product)
            self.stdout.write(self.style.SUCCESS('Product created: {}'.format(product['name'])))

        self.stdout.write(self.style.SUCCESS('Products created successfully'))