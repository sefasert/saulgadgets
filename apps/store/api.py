import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from apps.cart.cart import Cart
from .models import Product

def api_add_to_cart(request):  #Add to Cart'a tıklayınca console'daki işlemler
    data = json.loads (request.body)   # verileri al
    jsonresponse = {"success": True}   #Json yanıtı oluştur
    product_id = data ["product_id"]   #veriden product_id al
    update = data ["update"]
    quantity = data ["quantity"]

    cart = Cart(request)       #def __init__'deki request

    product = get_object_or_404(Product, pk=product_id) #ve pk'ya eşit olan ürünü al

    if not update:   #güncellemiyorsa
        cart.add(product=product, quantity=1, update_quantity=False)
    else:  #güncelliyorsa
        cart.add(product=product, quantity=quantity, update_quantity=True)

    return JsonResponse(jsonresponse)

def api_remove_from_cart(request):
    data = json.loads(request.body) # verileri al
    jsonresponse = {"success": True} #Json yanıtı oluştur
    product_id = str(data["product_id"])  #veriden product_id al

    cart = Cart(request)
    cart.remove(product_id)   #ve sepeti kaldır

    return JsonResponse(jsonresponse)
