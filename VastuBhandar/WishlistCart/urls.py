from django.urls import path
from .views import CreateCart, DeleteCartProduct, AddProductWishlist, CartList, \
    DeleteProductWishlist, WishList, CartEdit

urlpatterns = [
    # ====================== CARTS URLS ================================
    path("CreateCart/<pk>",
         CreateCart.as_view(),
         name='CreateCart'
         ),
    path("CartList/",
         CartList.as_view(),
         name='CartList'
         ),
    path("CartEdit/<pk>",
         CartEdit.as_view(),
         name='CartEdit'
         ),
    path("DeleteCartProduct/<pk>",
         DeleteCartProduct.as_view(),
         name='DeleteCartProduct'
         ),
    # ============================ WISHLIST URLS =========================
    path("AddProductWishlist/<pk>",
         AddProductWishlist.as_view(),
         name='AddProductWishlist'
         ),
    path("DeleteProductWishlist/<pk>",
         DeleteProductWishlist.as_view(),
         name='DeleteProductWishlist'
         ),
    path("WishList/",
         WishList.as_view(),
         name='WishList'
         ),

]
