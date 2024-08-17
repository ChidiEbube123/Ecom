from django.shortcuts import  redirect,render
from .models import Product, Category
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from payment.forms import ShippingForm
from payment.models import ShippingAddress
from django.contrib.auth.models import User
from .forms import *
from cart.cart import Cart
import json
from django.db.models import Q #for multiple queries
def home(request):
    return render(request, "index.html", {"products":Product.objects.all()})

def about(request):
    return render(request, "about.html")
#djangoc ant tell our css

def login_user(request):
    if request.method=="POST":
        password=request.POST["password"]
        username=request.POST["username"]
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #shopping cart
            current_user=Profile.objects.get(user__id=request.user.id)
            #insert create profile condition..lol
            #get saved cart from db
            saved_cart=current_user.old_cart
            if saved_cart:
                #convert to dic using json

            #convert db string to py dic
                converted_cart=json.loads(saved_cart)
                #add loaded cart dic to ,session
                cart=Cart(request)
                #loop thry cart and add items
                for key, value in converted_cart.items():
                  #  cart.add(product=key,quantity=value) could get weird
                     cart.db_add(product=key,quantity=value)
            messages.success(request, ("You have been logged in"))
            return redirect("home")
        else:
            messages.success(request, ("There was an error please try again"))
            return redirect("login_user")

    return render(request, "login.html")
@login_required
def logout_user(request):
    messages.success(request, ("You have been logged out.. Thanks"))
    logout(request)
    return redirect("login_user")

def register_user(request):
    form= SignUpForm()
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password1"]
            user=authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("User Created, please fill out your profile below"))
            return redirect("update_profile")
        else:
            messages.success(request, ("There was a problem try again"))
            return redirect("register_user")

    return render(request, "register.html", {"form": form})

def products(request, pk):
        return render(request, "product.html",{"prod":Product.objects.get(id=pk)})

def category(request, foo):
    foo=foo.replace("-"," ")
    category=Category.objects.get(name=foo)
    products=Product.objects.filter(category=category)
    print(type(products))
    return render(request,"category.html", {"products":products, "category": category})
@login_required
def update_user(request):
    if request.user.is_authenticated:
        #get currentuser
        current_user=User.objects.get(id=request.user.id)
        form= UpdateUserForm(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
            login(request, current_user)
            messages.success(request, ("Successfully changed up"))
            return redirect("home")
        return render(request, "update_user.html", {'form':form})
    else:
        messages.success(request, "must be logged in to register")


#useless featudre
@login_required
def update_password(request):
    if request.user.is_authenticated:
            #get currentuser
            current_user=User.objects.get(id=request.user.id)
            if request.method=="POST":
                form=ChangePassword(current_user,request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Successfylly changed pwd ")
                    login(request, current_user)
                    return redirect('login')
                else:
                    for error in list(form.errors.values()):
                        messages.error(request, error)
                        return redirect('update_password')
            #did they fill out thr form
            else:
                form=ChangePassword(current_user)
                return render(request, "update_password.html", {'form':form})
    else:
        messages.success(request, "Create an account first")
        return redirect('sign_up')

@login_required
def update_profile(request):
    if request.user.is_authenticated:
        #get currentuser
        #stupid profile not matching current_user=User.objects.get(id=request.user.id)..wouldnt happen if we started well

        current_user=Profile.objects.get(user__id=request.user.id)
        shipping_user=ShippingAddress.objects.get(user__id=request.user.id)#couldve been done inside this apps model sef
        form= UserProfileForm(request.POST or None, instance=current_user)
        shipping_form=ShippingForm(request.POST or None, instance=shipping_user)#couldve been done inside this apps model sef

        if form.is_valid() or shipping_form.is_valid(): 
            form.save()
            shipping_form.save()
            messages.success(request, ("Successfully updated Profile"))
            return redirect("home")
        return render(request, "update_profile.html", {'form':form, 'shipping_form':shipping_form})
    else:
        messages.success(request, "must be logged in to register")

def product_search(request):
    if request.method == "POST":
        searched = request.POST.get('searched', '')
        products = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
        if products.exists():
            return render(request, "product_search.html", {'searched': products, 'query': searched})
        else:
            messages.error(request, "No products match your search query")
            return render(request, "product_search.html", {'searched': None, 'query': searched})
    return render(request, "product_search.html", {'searched': None, 'query': ''})