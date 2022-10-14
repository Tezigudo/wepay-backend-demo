from django.contrib import admin

from .models import Bills, Food, Payment

class BillsAdmin(admin.ModelAdmin):
    list_display = ('header', 'name', 'pub_date')

class FoodAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'bill')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'bill', 'status', 'image')

admin.site.register(Bills, BillsAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Payment, PaymentAdmin)
