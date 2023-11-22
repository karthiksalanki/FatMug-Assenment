from rest_framework import serializers
from .models import *

class VendorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vendor
        #fields = ['__all__']
        fields = ['id','name', 'contact_details', 'address', 'vendor_code', 'on_time_delivery_rate', 'quality_rating_avg',
                  'average_response_time', 'fulfillment_rate'] 

class Purchase_OrderSerializer(serializers.ModelSerializer):
   # vendor = VendorSerializer()
    class Meta:
        model = Purchase_Order
        fields = ['id','po_number', 'vendor', 'delivery_date', 'items', 'quantity',
                  'status', 'quality_rating','issue_date','acknowledgment_date']
        
        
class PerformanceSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer()
    class Meta:
        model = Performance
        fields = ['id','vendor', 'on_time_delivery_rate', 'quality_rating_avg',
                  'average_response_time', 'fulfillment_rate'] 