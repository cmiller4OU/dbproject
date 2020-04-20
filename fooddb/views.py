from django.shortcuts import render
from django.http import HttpResponse
from fooddb.models import Food
from fooddb.models import Orders
from fooddb.models import Customers
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# from django.core.exceptions import ObjectDoesNotExist

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

     return render(request, 'fooddb/orderPage.html')



# @api_view(["POST"])
# @csrf_exempt
# @permission_classes([IsAuthenticated])
# def make_order(request):
#     payload = json.loads(request.body)
#     user = request.user
#     try:
#         author = Author.objects.get(id=payload["author"])
#         book = Book.objects.create(
#             title=payload["title"],
#             description=payload["description"],
#             added_by=user,
#             author=author
#         )
#         serializer = BookSerializer(book)
#         return JsonResponse({'books': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
#     except ObjectDoesNotExist as e:
#         return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
#     except Exception:
#         return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
