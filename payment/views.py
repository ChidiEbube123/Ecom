from django.shortcuts import render, redirect
from cart.cart import Cart
from django.core.mail import EmailMessage, get_connection

from .forms import ShippingForm
from .models import ShippingAddress
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from  ecom.settings import EMAIL_HOST_USER
# Create your views here.
def payment_success(request):
    return render(request, "payment/payment_success.html")

def checkout(request):
    cart=Cart(request)
    cart_products=cart.get_prods
    quantitites=cart.get_quants
    totals=cart.cart_total()
    if request.user.is_authenticated:
        current_user=ShippingAddress.objects.get(user__id=request.user.id)
        if current_user:
            shipping_form=ShippingForm(request.POST or None, instance=current_user)
            return render(request, "payment/checkout.html",{"cart_products":cart_products, "quantities":quantitites, "totals":totals, "shipping_form":shipping_form})
        else:
            shipping_form=ShippingForm(request.POST)
            return render(request, "payment/checkout.html",{"cart_products":cart_products, "quantities":quantitites, "totals":totals})

    else:
        return render(request, "payment/checkout.html",{"cart_products":cart_products, "quantities":quantitites, "totals":totals, })

def purchase(request):
    if request.method == 'POST':
        cart=Cart(request)

        cart_products=cart.get_prods
        quantitites=cart.get_quants
        subject = f'New Order from {request.user.username}'
        message = f"""
        Order Details:
        User: {request.user.username}
        Total: ${cart.cart_total}
        Items:
        """
        for item in cart_products:
             message += f"- {item.name}: ${item.sale_price} "
             ''''for keys,values in quantitites.items:
                 if keys==item.id:
                     message+=f"{values}"'''
        send_mail(
            subject,
            message,
            'electricsheep1910@gmail.com',  # From email
            ['fleektyre@gmail.com'],  # To email
            fail_silently=False,
        )
        messages.success(request, 'Your order has been placed successfully!')
        return redirect('checkout')
    
    return redirect('home')  # Redirect to cart if not a POST request

def order_success(request):
    
        return render(request,'payment/order_success.html')

    