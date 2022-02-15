from django.shortcuts import render
from .models import Product
from django.http.response import JsonResponse
import json

# Create your views here.
def add(request):
    response = {}
    products = Product.objects.all()
    # print(products)
    # for i in products:
    #     print(i.product_name)
    try:
        msg=""
        if request.method=="POST":
            print(request.POST)
            product_id = request.POST.get('id')
            print("product id=====>",product_id)
            product_name=request.POST['name']
            desc=request.POST['address']
            price=request.POST['age']
            response["status"]="true"
            response['msg']="data submitted successfully"
            if(product_id==""):
                Product(product_name=product_name,desc=desc,price=price).save()
            else:
                Product(id=product_id, product_name=product_name, desc=desc, price=price).save()
        # return JsonResponse({'response':True})
            return JsonResponse(json.dumps(response), safe=False)
        else:
            return render(request,"index.html", {"products":products})
    except Exception as e:
        print(e)
        response["status"] = "false"
        response['msg'] = "data cannot be submitted"
        return JsonResponse(json.dumps(response), safe=False)

def editData(request):
    response = {}
    if request.method == "POST":
        id=request.POST.get('id')
        prod =Product.objects.get(pk=id)
        print(prod)
        prod_data = {"id":prod.id, "name":prod.product_name, "desc":prod.desc, "price":prod.price}
        print(prod_data)
        # response['status'] = 'true'
        # response['msg'] = 'Record Updated'
        return JsonResponse(json.dumps(prod_data), safe=False)

def deleteData(request):
    response = {}
    if request.method == "POST":
        id=request.POST.get('id')
        print(id)
        pi=Product.objects.get(pk=id)
        pi.delete()
        response['status'] = 'true'
        response['msg'] = 'Record deleted Successfully'
        return JsonResponse(json.dumps(response), safe=False)
    else:
        response['status'] = 'false'
        response['msg'] = 'Record cannot be deleted'
        return JsonResponse(json.dumps(response), safe=False)
