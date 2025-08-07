from django.contrib import admin
from .models import Bill

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'date_created', 'amount', 'gst_percent', 'total_amount', 'paid')
    readonly_fields = ('gst_amount', 'total_amount')
