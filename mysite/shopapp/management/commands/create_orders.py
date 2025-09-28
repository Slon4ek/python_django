from django.contrib.auth.models import User
from django.core.management import BaseCommand
from shopapp.models import Order
class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Create order')
        user = User.objects.get(username='admin')
        order = Order.objects.create(
            user=user,
            delivery_address='г.Чебоксары, ул.Ленина, д.1, кв.1',
            promocode='SALE123',
        )
        self.stdout.write(f'Order {order} created')