from django.shortcuts import render
from django.http import HttpResponse
from fooddb.models import Food
from fooddb.models import Orders
from fooddb.models import Customers

# Create your views here.

def index(request):
    return render(request, 'fooddb/home.html')

def menu_view(request):
    query_set = Food.objects.all()
    context = {
        'object_list' : query_set
    }
    # obj = Food.objects.get(item_num = '1')
    # context = {
    #     'menu item' : obj.item_name,
    #     'price' : obj.price,
    # }  
    return render(request, 'fooddb/menu.html', context)

def order_display_view(request):
    itemNumber = request.GET['item number']
    orderNumber = request.GET['order number']
    total = request.GET['total']
    custId = request.GET['cust id']
    order_info = Orders(order_num=orderNumber,total=total,item_num=itemNumber,cust=cust_id)

    order_info.save()

    
    return render(request, 'fooddb/orderDisplay.html', context)

def order_page_view(request):



    # 
     return render(request, 'fooddb/orderPage.html')


