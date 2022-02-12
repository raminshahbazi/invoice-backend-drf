from django.contrib import admin

from core.models import Item, Invoice, InvoiceItem


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount', 'manufacturing_country')


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'description')


class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'item', 'registration_date')


admin.site.register(Item, ItemAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceItem, InvoiceItemAdmin)
