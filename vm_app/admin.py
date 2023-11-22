from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.
@admin.register(Vendor)
class VendorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','name', 'contact_details', 'address', 'vendor_code', 'on_time_delivery_rate', 'quality_rating_avg',
                  'average_response_time', 'fulfillment_rate']

@admin.register(Purchase_Order)
class Purchase_OrderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','po_number', 'delivery_date', 'items', 'quantity',
                  'status', 'quality_rating','issue_date','acknowledgment_date']
    
@admin.register(Performance)
class PerformanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'vendor','date', 'on_time_delivery_rate', 'quality_rating_avg',
                  'average_response_time', 'fulfillment_rate']
    
    
    
    # "quality_rating" : "3",
    # "issue_date" : "2023-11-27 15:18:16.000000",
    # "acknowledgment_date" : "2023-11-28 15:18:16.000000" 