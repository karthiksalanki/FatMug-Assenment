from django.urls import path
from .views import *

urlpatterns = [

    # get or create vendor
    path('vendors/', create_get_Vendor, name="creategetVendor"),
    path('vendors/<int:id>', update_delete_Vendor, name="update-delete-Vendor"),
    
    #purchase_orders
    path('purchase_orders/', createPO, name="creategetpo"),
    path('purchase_orders/<int:id>', update_delete_PO, name="update-delete-PO"),
    
    #test
    #path('test/',test,name="test")
    path('vendors/<int:id>/performance', getPerformance, name="getPerformances"),
    path('purchase_orders/<int:id>/acknowledge',update_Acknowledgment, name="acknowledge")
]