from django.contrib import admin

from core.models import Item, Invoice, InvoiceType, Country, InvoiceChangeLog


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount', 'manufacturing_country')


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'description')


class InvoiceTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']


class InvoiceChangeLogAdmin(admin.ModelAdmin):
    list_display = ['last_description']


admin.site.register(Item, ItemAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceType, InvoiceTypeAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(InvoiceChangeLog, InvoiceChangeLogAdmin)
