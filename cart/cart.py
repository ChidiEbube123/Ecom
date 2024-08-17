from store.models import Product, Profile

class Cart():#req is akin ti the user
    def __init__(self,request):#init our class
        self.session=request.session
        self.request=request#get request
        cart=self.session.get("session_key")#getting current session key if it exitsts in the sesh
#if user is new, create a new one
        if "session_key"  not in request.session:
            cart=self.session["session_key"]={}
#to make sure the scart is working on all pages we :
        self.cart=cart
        #we also use a context_processort
    def add(self, product, quantity):
        product_id=str(product.id)
        product_qty=str(quantity)
        #if producyt is already in cart we dont need to add it again
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id]=int(product_qty)#ding!
        self.session.modified=True
        #deal with logged in user
        if self.request.user.is_authenticated:
            current_user=Profile.objects.filter(user__id=self.request.user.id)#get user profile
            #convert "" to ''
            cart_conv=str(self.cart)
            cart_conv=cart_conv.replace("\'", "\"")
            #save our cart_conv to our profile
            current_user.update(old_cart=str(cart_conv))
    def delete(self, product):
            product_id=str(product)#cuz "3":1 is returned
            if product_id in self.cart:#justtt incase
                del self.cart[product_id]
            self.session.modified=True


            if self.request.user.is_authenticated:
                    current_user=Profile.objects.filter(user__id=self.request.user.id)#get user profile
                    #convert "" to ''
                    cart_conv=str(self.cart)
                    cart_conv=cart_conv.replace("\'", "\"")
                    #save our cart_conv to our profile
                    current_user.update(old_cart=str(cart_conv))



    def db_add(self, product, quantity):
            product_id=str(product)
            product_qty=str(quantity)
            #if producyt is already in cart we dont need to add it again
            if product_id in self.cart:
                pass
            else:
                self.cart[product_id]=int(product_qty)#ding!
            self.session.modified=True
            #deal with logged in user
            if self.request.user.is_authenticated:
                current_user=Profile.objects.filter(user__id=self.request.user.id)#get user profile
                #convert "" to ''
                cart_conv=str(self.cart)
                cart_conv=cart_conv.replace("\'", "\"")
                #save our cart_conv to our profile
                current_user.update(old_cart=str(cart_conv))
                
                    
    #get quantity pf items in ccart 
    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        #get id from cart
        product_ids=self.cart.keys()
        #use id to lookup prod in our db
        products=Product.objects.filter(id__in=product_ids)
        return products
    def get_quants(self):
        quantities=self.cart
        return quantities
    def update_qty(self, product,quantity):
        product_id=str(product)
        product_qty=int(quantity)#no reason am
        #get cart
        ourcart=self.cart
        #update dic
        ourcart[product_id]=product_qty
        self.session.modified=True
        thing=self.cart
        
        if self.request.user.is_authenticated:
                current_user=Profile.objects.filter(user__id=self.request.user.id)#get user profile
                #convert "" to ''
                cart_conv=str(self.cart)
                cart_conv=cart_conv.replace("\'", "\"")
                #save our cart_conv to our profile
                current_user.update(old_cart=str(cart_conv))

        return thing
    
    def cart_total(self):
          print(self.cart)
          product_ids=self.cart.keys()
          products=Product.objects.filter(id__in=product_ids)
            #get quantities
          quantities=self.cart
                    #rememeber our cart is {'4':3,}
          total=0
          for key,value in quantities.items():
                #convert our string key to an int key
                key=int(key)
                for product in products:
                    if product.id==key:
                        total+= (product.sale_price*value)#

          return total


        #rememeber our csrt is {'4':3,}