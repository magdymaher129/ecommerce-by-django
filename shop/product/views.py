from django.shortcuts import render,HttpResponse,HttpResponseRedirect,get_object_or_404
from django.utils import timezone
from.models import Item,OrderItem,Order
from collections import Counter
from django.contrib.auth.models import User
from django.db.models import Sum
from django.core.cache import cache
from django.contrib.auth.decorators import login_required
def item_list(request):
 items =Item.objects.all()
 user=request.user
 context={
    'items':items,
    'user':user,
}
 template='home.html'
 return render(request,template,context)
# Create your views here.
def home(request):
     
    items =Item.objects.all()
    user=request.user
    context={
        'items':items,
        'user':user,
                     
    }
    template='home.html'
    return render(request,template,context)




def oneItem(request,slug):
    item =Item.objects.get(slug=slug)

    context={
        'item':item,
    }
    template='product.html'
    return render(request,template,context)
# def addToCart(request,slug):
#   item =Item.objects.get(slug=slug)
#   try:
#    cart_obj=new_or_create(request,slug)
#    items=cart_obj.product.all()
#    cart_obj.save()
#    context={
    #   'item':item,
    #   'cart_obj':cart_obj,
    #   'items':items,
    #  }
#    template='item-list.html'
#    
#    return render(request,template,context)
#   except:
    # return HttpResponse("illegal proccess  login first")
# 

""" def add_to_cart2(request,slug): """
"""    # create item """
"""     # item=get_object_or_404(Item,slug=slug) """
"""     # print(item.title) """
"""     #add item to order item """
"""     # order_item=OrderItem.objects.get_or_create(item= item)
"""     #  """
""" #     """
"""     #check if we have an already order """
"""     # order_qs=Order.objects.filter(user=request.user,ordered=False)
"""     # if order_qs.exists(): """
"""       #  order is already exist """
"""         #print(order_qs.user) """
"""         # order=order_qs[0] """
"""        # check if order item is in order """
"""         # if order.item.filter(item__slug=item.slug).e xists():
"""             #  order_item.quantaty+=1 """
"""             #  order_item.save() """
"""         # else: """
"""             #  order.item.add(order_item) """
"""  """
"""             #   """
"""     # else: """
"""             # ordered_date=timezone.now() """
"""             # order=Order.objects.create(user=request. user,ordered_date=ordered_date)
"""             # order.item.add(order_item) """
"""             # order.save() """
"""     # template='item-list.html' """
"""     # return  render(request,template,{}) """
"""  """
"""  # create item """
"""   if request.user.is_authenticated: """
"""     item = get_object_or_404(Item, slug=slug) """
"""     if not item: """
"""         return render(request,'404.html',{}) """
"""      #add item to order item """
"""     order_item, created = OrderItem.objects.get_or_create(
"""         #item=item, """
"""         user=request.user, """
"""         #ordered=False """
"""     ) """
"""      """
"""       #  order is already exist """
"""     order_qs = Order.objects.filter(user=request.user, ordered=False)
"""  
"""     if order_qs.exists(): """
"""         order = order_qs[0] """
"""         # check if the order item is in the order """
"""         if order.item.filter(item__slug=item.slug).exists():
"""             #order_item.quantaty += 1 
"""             order_item.save() """
"""             """
"""             """
"""             #messages.info(request, "This item quantity was updated.")
"""            # return render(request,'item-list.html',{}) 
"""         else: """
"""             order.item.add(order_item) """
"""             """
"""             """
"""              """
"""             #messages.info(request, "This item was added to your cart.")
"""            # return render(request,'item-list.html',{}) 
"""     else: """
"""        # ordered_date = timezone.now() """
"""         order = Order.objects.create( """
"""             user=request.user)#, ordered_date=ordered_date)
"""        """
"""        """
"""         #order.item.add(order_item) """
"""         #messages.info(request, "This item was added to your cart.")
"""         #return render(request,'item-list.html',{}) """
"""   #else: """
"""       return HttpResponse('you have to login first!!') """






@login_required(login_url="/log/")
def add_to_cart(request,slug):
    cache.clear()
    #checkout user if is authenticated
    if request.user.is_authenticated:
        #check item is exist or not
        item=get_object_or_404(Item,slug=slug)
        
        if  item.avaliable==False:
           
          return render(request,'404.html', {'item':item})
               # check order item,order
        order_item, Created = OrderItem.objects.get_or_create(user=request.user,item=item)
        order_qs=Order.objects.filter(user=request.user)
       
        if order_qs:
            
            #check if item is in order:
             if order_qs[0].item.filter(item__slug=item.slug) and order_item:
                 #add quantity +1
                 
                  order_item.quantaty+=1
                  order_item.save()
                  items=OrderItem.objects.filter(user=request.user)
                 
                  totalprice=order_qs[0].get_final()
                  quantaty=0
                  for xitem in items:
                      quantaty+=xitem.quantaty
                                                                                                                                    

                

                 
                 
                 
                  return render(request,'item-list.html',{'items':items,'quantaty':quantaty,'totalprice':totalprice})
                
                
               
             else:
                order_qs[0].item.add(order_item)
                order_qs[0].save()
                totalprice=order_qs[0].get_final()
                items=OrderItem.objects.filter(user=request.user)
                quantaty=0
                for xitem in items:
                    quantaty+=xitem.quantaty
               

                return render(request,'item-list.html',{'items':items,'quantaty':quantaty,'totalprice':totalprice})
        else:
            order_obj=Order.objects.create(user=request.user)
            #print(order_obj)
            order_obj.item.add(order_item)
            
            items=OrderItem.objects.filter(user=request.user)
            totalprice=order_obj.get_final()
            quantaty=0
            for xitem in items:
               quantaty+=xitem.quantaty
          
            


            return render(request,'item-list.html',{'items':items,'quantaty':quantaty,'totalprice':totalprice})
       
        
   # else:
        #return render(request,'login.html',{})


def display_cart(request):

    return render(request,template,context)



@login_required(login_url="/log/")
def remove_from_cart(request,slug):
     cache.clear()
     if request.user.is_authenticated:
         # return HttpResponse('you login !!')
          item=get_object_or_404(Item,slug=slug)
          order_item = OrderItem.objects.filter(user=request.user,item=item)
          if order_item :
              order_item.delete()
          else:
               return HttpResponse('you have not an items to delete  ')

          

          order_qs=Order.objects.filter(user=request.user)
          if order_qs:
              
             

                  #order_qs[0].item.remove(order_item)
                  
                 
                

                  order_qs[0].save()
                  items=OrderItem.objects.filter(user=request.user)
                 
                 
                  totalprice=order_qs[0].get_final()
                  quantaty=0
                  for xitem in items:
                     quantaty+=xitem.quantaty
                  return render(request,'item-list.html',{'items':items,'quantaty':quantaty,'totalprice':totalprice})
          else:
              return HttpResponse('you have not an order first')






   #check item is exist or not
      
      

     else:
          return HttpResponse('you have to log in first')


@login_required(login_url="/log/")
def remove_singleItem_from_cart(request,slug):
     cache.clear()
     if request.user.is_authenticated:
        
          item=get_object_or_404(Item,slug=slug)
          order_item = OrderItem.objects.get(user=request.user,item=item)
          order_qs=Order.objects.filter(user=request.user)
        
          if order_item.quantaty>1 :
              order_item.quantaty-=1
              order_item.save()
              order_qs[0].save()
             
           
           
           
                 
                                          
             
             
             
             
             
             

          elif order_item.quantaty <= 1:
                
              
                   order_item.delete()
                   order_qs[0].save()
     items=OrderItem.objects.filter(user=request.user)
     totalprice=order_qs[0].get_final()
     quantaty=0
     for xitem in items:
                     quantaty+=xitem.quantaty
     return render(request,'item-list.html',{'items':items,'quantaty':quantaty,'totalprice':totalprice})
                 
               
               
                                
                 
                 
                 
                 
                 
                 
             
  
  






      
      

    
    
      
   
   
   
   
   
   
   

      
      





























