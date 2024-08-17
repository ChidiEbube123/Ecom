from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from django.contrib import messages
from store.models import Product
from django.http import JsonResponse #why
# Create your views here.
def cart_home(request):
    cart=Cart(request)
    cart_products=cart.get_prods
    quantitites=cart.get_quants
    totals=cart.cart_total()
    return render(request, "cart_home.html", {"cart_products":cart_products, "quantities":quantitites, "totals":totals})
#were going to need to access our cart from here
def cart_add(request):
    #get cart
    cart=Cart(request)
    if request.POST.get("action")=="post":
        print(request.POST.get("product_qty"))
        product_qty=int(request.POST.get("product_qty"))

        product_id=int(request.POST.get("product_id"))
        
        # look up prod in db
        product=get_object_or_404(Product, id=product_id)
        #add to session
        cart.add(product, product_qty)
        #get card quantity
        cart_quantity=cart.__len__()
        response=JsonResponse({"qty": cart_quantity})
        messages.success(request, ("Product added"))
        return response
  
    
def cart_delete(request):
     cart=Cart(request)
     if request.POST.get("action")=="post":
        product_id=int(request.POST.get("product_id"))

        cart.delete(product_id)
        #not reall;y useful
     response=JsonResponse({'prod':product_id})
     messages.success(request, ("Product removed"))

     return response
        # look up prod in db
def cart_qty_update(request):
    cart=Cart(request)
    if request.POST.get("action")=="post":
        product_id=int(request.POST.get("product_id"))
        product_qty=int(request.POST.get("product_qty"))
        cart.update_qty(product_id, product_qty)
        #not rea;;y doing anything
        response=JsonResponse({'qty':product_qty})
        print(type(product_qty))
        return response


#To test em session:  python manage.py shell
'''
from django.contrib.sessions.models import Session
k=Session.objects.get(pk='al3z5sjs923nuxao9alv353dahcuy6u3')
k.get_decoded()
{'session_key': {'1': {'price': '50.00'}}}
>>>'''