from .cart import Cart
#so it works on all pages on the site
#next we let django know that it exists by going to settings, templates and adding
def cart(request):
    return({"cart":Cart(request)})