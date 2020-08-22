from django.conf import settings
from Advertisements.models import ads
from decimal import Decimal

class Cart(object):

    def __init__(self, request):

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, ads, ad_count=1, update_count=False):
        ads_id = str(ads.id)
        if ads_id not in self.cart:
            self.cart[ads_id] = {'ad_count':1, 'price':str(ads.price)}
        if update_count:
            self.cart[ads_id]['product_count'] = ad_count
        else:
            self.cart[ads_id]['product_count'] += ad_count
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, ads):
        ads_id = str(ads.id)
        if ads_id in self.cart:
            del self.cart[ads_id]
            self.save()

    def __iter__(self):
        ads_ids = self.cart.keys()
        adss = ads.objects.filter(id__in=ads_ids)
        for ad in adss:
            self.cart[str(ads.id)]['ads'] = ad

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['ads_count']
            yield item

    def __len__(self):
        return sum(item['ads_count'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['ads_count'] for item in self.cart.values())

    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True

