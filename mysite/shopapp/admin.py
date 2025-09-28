from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest
from .admin_mixins import ExportAsCSVMixin

from .models import Product, Order


class ProductInline(admin.StackedInline):
    model = Order.products.through

class OrderInline(admin.TabularInline):
    model = Product.orders.through

@admin.action(description='Mark selected orders as archived')
def mark_as_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)

@admin.action(description='Unmark selected orders as archived')
def unmark_as_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=False)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    actions = (
        mark_as_archived,
        unmark_as_archived,
        'export_as_csv',
    )
    inlines = (OrderInline,)
    list_display = ('pk', 'name', 'description_short', 'price', 'quantity', 'discount', 'archived')
    list_display_links = ('pk', 'name')
    search_fields = ('name', 'description')
    fieldsets = (
        (None, {
            'fields': ('name', 'description',)
        }),
        ('Price & Availability', {
            'fields': ('price', 'quantity', 'discount'),
            'classes': ('collapse',),
        }),
        ('Archived', {
            'fields': ('archived',),
            'classes': ('collapse',),
        }),
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (ProductInline,)
    list_display = ('pk', 'user_verbose_name', 'delivery_address', 'promocode', 'total_price', 'created_at')
    list_display_links = ('pk', 'user_verbose_name')
    search_fields = ('user_verbose_name', 'delivery_address')

    def get_queryset(self, request):
        return Order.objects.select_related('user').prefetch_related('products')

    def user_verbose_name(self, obj: Order) -> str:
        return obj.user.get_full_name() or obj.user.username

