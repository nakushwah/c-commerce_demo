"""
File containing  with two model's views
1. UserCart
2 .Wishlist
"""


import uuid
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View, UpdateView
from .models import UserCart, Wishlist
from products.models import Product


class CreateCart(LoginRequiredMixin, View):

    def get(self, request, pk):
        product = Product.objects.get(id=uuid.UUID(pk))
        obj = UserCart.objects.get_or_create(
            user_id=self.request.user,
            product_id=product,
            cart_price=product.price)
        cartlist = UserCart.objects.filter(user_id=self.request.user.id)
        return render(request, template_name="cart.html", context={"data": cartlist})


class CartList(LoginRequiredMixin, View):

    def get(self, request):
        cartlist = UserCart.objects.filter(user_id=self.request.user.id)
        return render(request, template_name="cart.html", context={"data": cartlist})


class CartEdit(LoginRequiredMixin, UpdateView):
    model = UserCart
    template_name = 'edit_carts_quantity.html'
    fields = ['quantity']
    success_url = "/carts/CartList"


class DeleteCartProduct(LoginRequiredMixin, View):

    def get(self, request, pk):
        obj = UserCart.objects.get(pk=pk)
        obj.delete()
        return render(request, template_name="cart.html")


# ============================== Wishlist Views =============================================
class AddProductWishlist(LoginRequiredMixin, View):

    def get(self, request, pk):
        obj = Wishlist.objects.get_or_create(
            user_id=self.request.user,
            product_id=Product.objects.get(id=uuid.UUID(pk)))
        wishlist = Wishlist.objects.filter(user_id=self.request.user.id)
        return render(request, template_name="wishlist.html", context={"data": wishlist})


class WishList(LoginRequiredMixin, View):

    def get(self, request):
        wishlist = Wishlist.objects.filter(user_id=self.request.user.id)
        return render(request, template_name="wishlist.html", context={"data": wishlist})


class DeleteProductWishlist(LoginRequiredMixin, View):

    def get(self, request, pk):
        obj = Wishlist.objects.get(pk=pk)
        obj.delete()
        return render(request, template_name="wishlist.html")
