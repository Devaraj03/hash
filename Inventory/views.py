from django.shortcuts import render
from .forms import *
from .models import *

def HomePage(request):
    data={
        "n":10,
        "name":"Devaraj",
        "role":"admin",
        "numbers":[1,2,3,4,5],
        "marks":{
            "tamil":100,
            "english":98
        }
    }
    return render(request,'home.html',data)
def aboutpage(request):
    return render(request,'about.html')
def contactpage(request):
    return render(request,'contact.html')
def servicespage(request):
    return render(request,'services.html')
def productsadd(request):

    context = {
        'product_form' : Product_Form()
    }
    if request.method =="POST":
        product_form = Product_Form(request.POST)

        if product_form.is_valid():
            product_form.save()

    return render(request,'products_add.html', context)


def AllProducts(request):
    context= {
        "all_products":Product.objects.all()
    }

    return render(request,'products.html',context)