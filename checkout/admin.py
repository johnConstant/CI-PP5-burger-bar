from django.contrib import admin
from .models import Order, OrderLineItem, Comment


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    search_fields = ('order_number', 'full_name',)
    readonly_fields = ('order_number', 'order_date',
                       'delivery_cost', 'order_total',
                       'grand_total',)

    fields = ('order_number', 'user_profile', 'order_date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total',)

    list_display = ('order_number', 'order_date', 'full_name',
                    'grand_total', 'order_type', 'order_location')

    list_filter = ('order_type', 'order_location', 'order_date')

    ordering = ('-order_date',)


admin.site.register(Order, OrderAdmin)


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):

    list_filter = ('approved', 'created_date')
    list_display = ('name', 'body', 'order', 'created_date')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
