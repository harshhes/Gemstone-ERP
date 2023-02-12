from pyexpat import model
from django.contrib import admin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'phone', 'country', 'role', 'business_name', 'is_superuser']


admin.site.register(SupplierDetail)

admin.site.register(PurchaseMemo)

admin.site.register(PurchaseOrder)

admin.site.register(Item)