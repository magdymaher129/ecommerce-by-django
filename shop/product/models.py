from django.db import models
from django.conf import settings
from django.utils import timezone

CATEGORY_CHOICES=(
    ('S','shirt'),
   ( 'SW','sport wear'),
    ('OW','out wear')
)
LABEL_CHOICES=(
    ('P','primary'),
    ('S','secondary'),
    ('D','danger')
)

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length = 150)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    discount_price=models.FloatField(blank=True,null=True)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2,default='s')
    label=models.CharField(choices=LABEL_CHOICES,max_length=1,default='p')
    slug=models.SlugField(default='')
    description=models.TextField(null=True,blank=True)
    avaliable=models.BooleanField(default=True)
    add_date=models.DateField(auto_now=True)
    update_date = models.DateField(auto_now=False, auto_now_add=True)
    image = models.ImageField(upload_to='',blank=True,null=True  )
    
    
    def __str__(self):
    	
    
        return self.title
    def saving(self):
        if self.discount_price:
            saving_money= float(self.price)-float(self.discount_price)
            return saving_money

class OrderItem(models.Model):
        user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
        item=models.ForeignKey(Item,on_delete=models.CASCADE)
        quantaty=models.IntegerField(default=1)
        ordered=models.BooleanField(default=False)

        def __str__(self):
                return f"{self.quantaty} of {self.item.title}"
        def get_total_item_price(self):
             
                return self.quantaty * self.item.price

        def get_total_discount_item_price(self):
           

                 return self.quantaty * self.item.discount_price

        def get_amount_saved(self):
              return self.get_total_item_price() - self.get_total_discount_item_price()

        def get_final_price(self):
        
         if self.item.discount_price:
            return self.get_total_discount_item_price()
         else:
            return self.get_total_item_price()
        

class Order( models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    item = models.ManyToManyField(OrderItem,related_name='orderItems')# model.objects.add(item)
    start_date=models.DateField(auto_now_add=True)
    ordered_date = models.DateTimeField(default=timezone.now)
    ordered=models.BooleanField(default=False)

    def __str__(self):
      return self.user.username



    def get_final(self):
        
     total=0
     for order_item  in self.item.all():
         total+=float(order_item.get_final_price())
         print('total=',total)
     return total

     
     
     
     





