from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .cart import Cart
from Advertisements.models import ads
from .forms import CartAddProductForm

@require_POST
def cart_add(request, ads_id):
    cart = Cart(request)
    ad = get_object_or_404(ads, id=ads_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(ads=ad,
                 ad_count=cd['ad_count'],
                 update_count=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, ads_id):
    cart = Cart(request)
    ad = get_object_or_404(ads, id=ads_id)
    cart.remove(ad)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart':cart})
