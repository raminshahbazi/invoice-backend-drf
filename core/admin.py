from django.contrib import admin

from core.models import Item, Invoice


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount', 'manufacturing_country')


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'description')


admin.site.register(Item, ItemAdmin)
admin.site.register(Invoice, InvoiceAdmin)
