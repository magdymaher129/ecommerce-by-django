from django.urls import path
from .views import home,oneItem,add_to_cart,remove_from_cart,remove_singleItem_from_cart

urlpatterns = [
    path('', home,name='home'),
    path('oneItem/<slug:slug>',oneItem,name='oneItem'),
   
    path('add_to_cart/<slug>',add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug>',remove_from_cart,name="remove_from_cart"),
     path('remove_singleItem_from_cart/<slug>',remove_singleItem_from_cart,name="remove_singleItem_from_cart"),
   
   
   
    
]
