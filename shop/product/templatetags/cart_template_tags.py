from django import template
from product.models import Order


register=template.Library()
@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        if qs.exists():     
            items= qs[0].item.all()
            quantaty=0
            for item in items:
                quantaty+=item.quantaty
            return quantaty

        else:
            return 0

