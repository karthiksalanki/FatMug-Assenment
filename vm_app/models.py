from django.db import models

# Create your models here.

class Vendor(models.Model):
    
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=25)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)
    
    class Meta:
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendor'
        
    def __str__(self):
        return self.name

# {
#     "name":"karthik",
#     "contact_details":"8951908964",
#     "address":"challakere",
#     "vendor_code":"V1001"
# }    

class Purchase_Order(models.Model):
    
    PENDING = 'pending'
    COMPLETED = 'completed'
    CANCELED = 'canceled'

    STATUS_CHOICES = [
        (PENDING, 'pending'),
        (COMPLETED, 'completed'),
        (CANCELED, 'canceled'),
    ]
    # {
    # "po_number" : "ord01",
    # "vendor" : "1" ,
    # "delivery_date" : "2023-11-25 15:18:16.000000",
    # "items" : "test-item" ,
    # "quantity" : "1",
    # "status" : "pending",
    # "quality_rating" : "3",
    # "issue_date" : "2023-11-24 15:18:16.000000",
    # "acknowledgment_date" : "2023-11-25 15:18:16.000000" 
    # }
    
    po_number = models.CharField(max_length=10)
    vendor = models.ForeignKey(Vendor,on_delete=models.DO_NOTHING)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(auto_now_add=False)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default=PENDING)
    quality_rating = models.FloatField(null=True,blank=True)
    issue_date = models.DateTimeField(null=True,blank=True)
    acknowledgment_date = models.DateTimeField(null=True,blank=True)
    
    class Meta:
        verbose_name = 'Purchase Order'
        verbose_name_plural = 'Purchase Order'
        
    def __str__(self):
        return self.po_number
        
class Performance(models.Model):

    vendor = models.ForeignKey(Vendor,on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)
        
    class Meta:
        verbose_name = 'Performance'
        verbose_name_plural = 'Performance'

        