from django.contrib.admin import register, ModelAdmin
from .models import * 

@register(Customer)
class CustomerAdmin(ModelAdmin):
    pass


@register(Offer)
class OfferAdmin(ModelAdmin):
    pass