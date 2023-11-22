from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from .models import *
from .serializers import *
from django.db.models.signals import Signal
from django.dispatch import receiver
from django.db.models import F, ExpressionWrapper, fields
from django.db.models import Avg

custm_signal = Signal()
acknowledgment_signal = Signal()
# Create your views here.

#Vendor Profile Management:

# {
#     "name" : "karthik",
#     "contact_details" : "8951908964",
#     "address" : "challakere",
#     "vendor_code" : "V1001"
# }

@api_view(['POST','GET'])
def create_get_Vendor(request):
    # try:
    if request.method == 'GET':
        requestData = Vendor.objects.all()
        serializer = VendorSerializer(requestData, many=True)
        return Response({'status':200,'data':serializer.data})
    else:
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # update_to_performence = Performance.objects.create(vender = serializer[id]
            #                                                    on_time_delivery_rate = serializer[on_time_delivery_rate]
            #                                                    quality_rating_avg = serializer[quality_rating_avg]
            #                                                    average_response_time = serializer[average_response_time]
            #                                                    fulfillment_rate = serializer[fulfillment_rate]
            #                                                    )
            # update_to_performence.save()
            return Response({'status':201,'data':serializer.data})
        else:
            return Response({'status':400,'data':serializer.errors})
    # except Exception as e:
    #     return Response(str(e))
        
        
@api_view(['GET','PUT','DELETE'])
def update_delete_Vendor(request,id):
    try:
        vendorData = Vendor.objects.get(id = id)
        if request.method == 'GET':
            serializer = VendorSerializer(vendorData)
            return Response({'status':200,'data':serializer.data})
        elif request.method == 'PUT':
            print(id)#requestData,request.data)
            serializer = VendorSerializer(vendorData, data=request.data)
            if serializer.is_valid():
                # serializer.save()
                return Response({'status':201,'data':serializer.data})
            else:
                return Response({'status':400,'data':serializer.errors})
        else:
            vendorData.delete()
            return Response({'status':200,'data':'data deleted'})
    except Exception as e:
        return Response(str(e))
    
#working with Purchase Order
    # {
    # "po_number" : "ord01",
    # "vendor" : "2" ,
    # "delivery_date" : "2023-11-25 15:18:16.000000",
    # "items" : "test-item" ,
    # "quantity" : "1",
    # "status" : "pending",
    # "quality_rating" : "3",
    # "issue_date" : "2023-11-24 15:18:16.000000",
    # "acknowledgment_date" : "2023-11-25 15:18:16.000000" 
    # }
    
    # {
    # "po_number" : "ord03",
    # "vendor" : 2,
    # "delivery_date" : "2023-11-28 15:18:16.000000",
    # "items" : "test-item2" ,
    # "quantity" : "1",
    # "status" : "pending",
    # "quality_rating" : "3",
    # "issue_date" : "2023-11-27 15:18:16.000000",
    # "acknowledgment_date" : "2023-11-28 15:18:16.000000" 
    # }
@api_view(['GET','POST'])
def createPO(request):
    if request.method == 'GET':
        name = request.GET.get('vendor')
        purchase_order_list = Purchase_Order.objects.filter(vendor=name)
        serializer = Purchase_OrderSerializer(purchase_order_list,many=True)
        return Response({'status':200,'data':serializer.data})
    else:
        print(request.data)
        serializer = Purchase_OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Some action occurs
            data={'data':request.data}
            custm_signal.send(sender=Purchase_Order,data=request.data)
            return Response({'status':201,'data':serializer.data})
        else:
            return Response({'status':400,'data':serializer.errors})
        
@api_view(['GET','PUT','DELETE'])
def update_delete_PO(request,id):
        po_Data = Purchase_Order.objects.get(id = id)
        if request.method == 'GET':
            serializer = Purchase_OrderSerializer(po_Data)
            return Response({'status':200,'data':serializer.data})
        elif request.method == 'PUT':
            if request.GET.get('status')!='completed':
                serializer = Purchase_OrderSerializer(po_Data,data=request.data)
                if serializer.is_valid():
                    print("Purchase order")
                    serializer.save()
                    custm_signal.send(sender=Purchase_Order,data=request.data)
                    return Response({'status':201,'data':serializer.data})
                else:
                    return Response({'status':400,'msg':'cannot update, thank you.'})
            else:
                return Response({'status':400,'data':serializer.errors})
        else:
            po_Data.delete()
            return Response({'status':200,'data':'deleted successfully'})


@receiver(custm_signal)
def custm_signal_handler(sender, **data):
    print("Signal received!",data)
    #On-Time Delivery Rate
    status = data['data']['status']
    vendor = data['data']['vendor']
    delivery_date = data['data']['delivery_date']
    vendorData = Vendor.objects.get(id = vendor)
    vendor_data_list = Purchase_Order.objects.filter(status='completed',vendor=vendor)
    #print(vendorData,vendor_data_list,len(vendor_data_list),status,vendor,issue_date,delivery_date)
    
    if status == 'completed':
        issue_date = data['data']['issue_date']
        if len(vendor_data_list)>0:
            on_time_delivery_count=0        #for ontime delivery
            sum=0       #for qualityrate
            time_diff=None         #Average Response Time
            for vendor in vendor_data_list:
                if vendor.issue_date <= vendor.delivery_date:
                    on_time_delivery_count += 1
                sum += vendor.quality_rating
                # time_diff = time_diff+(vendor.issue_date - vendor.acknowledgment_date)
                # average_time_difference = Purchase_Order.objects.filter(vendor_id=vendor).annotate(
                #     time_difference=ExpressionWrapper(
                #         F('acknowledgment_date') - F('issue_date'),
                #         output_field=fields.DurationField())).aggregate(avg_time=Avg('time_difference'))
            on_Time_Delivery_rate = (on_time_delivery_count/len(vendor_data_list))*100
            #update to vender profile
            vendorData.on_time_delivery_rate = on_Time_Delivery_rate
            vendorData.save()
            
            #Quality Rating Average:
            vendorData.quality_rating_avg = (sum/len(vendor_data_list))
            vendorData.save()
            
            #Average Response Time:
            # for po in vendor_data_list:
            #     duration = (po.acknowledgment_date-po.issue_date).total_seconds() / 3600
            #     time_diff=time_diff+duration
            # average_response_time = sum/len(vendor_data_list)
            # average_time_difference = Purchase_Order.objects.filter(vendor=vendorData.id).annotate(
            #         time_difference=ExpressionWrapper(
            #             F('acknowledgment_date') - F('issue_date'),
            #             output_field=fields.DurationField())).aggregate(avg_time=Avg('time_difference'))
            # vendorData.average_response_time = (average_time_difference['avg_time'].total_seconds() / 3600)
            # vendorData.save()
            
            #Fulfilment Rate:
            vender_count = Purchase_Order.objects.filter(vendor=vendorData.id)
            vendorData.fulfillment_rate = (len(vendor_data_list)/len(vender_count))*100
            print(on_Time_Delivery_rate,vendorData.quality_rating_avg,vendorData.fulfillment_rate)
            vendorData.save()
            
            ##update to Performance
            print(vendorData.id,vendorData.on_time_delivery_rate,vendorData.quality_rating_avg,vendorData.average_response_time)
            data={
                'vendor':vendorData,
                'on_time_delivery_rate':vendorData.on_time_delivery_rate,
                'quality_rating_avg':vendorData.quality_rating_avg,
                #'average_response_time':vendorData.average_response_time,
                'fulfillment_rate':vendorData.fulfillment_rate
            }
            createPerformance = Performance.objects.create(**data)
            createPerformance.save()
    else:
        #Fulfilment Rate: obviously will be 0 if vendor_count=0
        vendor_count = Purchase_Order.objects.filter(vendor=vendor)
        if len(vendor_count)>0:
            vendorData.fulfillment_rate = (len(vendor_data_list)/len(vendor_count))*100
            vendorData.save()
        createPerformance = Performance.objects.create(vendor_id=vendor,
                                                        on_time_delivery_rate=vendorData.on_time_delivery_rate,
                                                        quality_rating_avg=vendorData.quality_rating_avg,
                                                        average_response_time=vendorData.average_response_time,
                                                        fulfillment_rate=vendorData.fulfillment_rate)
    #createPerformance.update(fulfillment_rate=vendorData.fulfillment_rate)

    # return Response({'status':200,'data':'updated'})


#get performance details
@api_view(['GET'])         
def getPerformance(request,id):
    performanceData = Performance.objects.get(id = id)
    serializer = PerformanceSerializer(performanceData)
    return Response({'status':200,'data':serializer.data})


#updating the acknowledgment
@api_view(['POST'])
def update_Acknowledgment(request,id):
    po_data = Purchase_Order.objects.get(id=id)
    acknowledgment = request.data.get('acknowledgment')
    po_data.acknowledgment_date = acknowledgment
    po_data.save()
    print(po_data.acknowledgment_date)
    acknowledgment_signal.send(sender=Purchase_Order,data={'id':po_data.vendor.id})
    return Response({'status':200,'msg':'Updated successfully'})

#to trigger the recalculation of average_response_time.  
@receiver(acknowledgment_signal)
def calculate_acknowledgment(sender, **data):
    vendorData=Vendor.objects.get(id=data['data']['id'])
    average_time_difference = Purchase_Order.objects.filter(vendor=vendorData.id).annotate(
            time_difference=ExpressionWrapper(
                F('acknowledgment_date') - F('issue_date'),
                output_field=fields.DurationField())).aggregate(avg_time=Avg('time_difference'))
    vendorData.average_response_time = (average_time_difference['avg_time'].total_seconds() / 3600)
    vendorData.save()
    
