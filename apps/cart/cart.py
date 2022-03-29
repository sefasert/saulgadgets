from django.conf import settings  #settings'de yaptığımız sessionları içe aktarcaz

from apps.store.models import Product

class Cart(object):
    def __init__(self, request): #session işlemler
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def __iter__(self):   #sepetteki ürünleri yineler
        product_ids = self.cart.keys()

        product_clean_ids = []

        for p in product_ids:
            product_clean_ids.append(p)

            self.cart[str(p)] ["product"] = Product.objects.get(pk=p)

        for item in self.cart.values(): #ürünlerin toplam fiyatını verir
            item["total_price"] = int(item["price"]) * int(item["quantity"])

            yield item

    def __len__(self): #sepetteki toplam ürün sayısını sayar
        return sum(item["quantity"] for item in self.cart.values())

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        price = product.price

        if product_id not in self.cart: #product_id'nin sepette olup olmadığını kontrol et değilse oluştur
            self.cart[product_id] = {"quantity":0, "price": price, "id": product_id}

        if update_quantity:  #miktarı güncelle
            self.cart[product_id] ["quantity"] = quantity
        else:                #miktarı 1 artır
            self.cart[product_id] ["quantity"] = self.cart[product_id] ["quantity"] + 1

        self.save()

    def remove(self, product_id):  #sepetteki ürünü kaldır
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):  #session'ı kaydet
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
