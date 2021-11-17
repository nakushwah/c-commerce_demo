from django.urls import path
from .views import AddProduct, ListProducts, DetailProduct, ProductByCategory,\
    ProductDelete, ProductUpdate

urlpatterns = [
    path("AddProduct/",
         AddProduct.as_view(),
         name="AddProduct"
         ),
    path("ListProducts/",
         ListProducts.as_view(),
         name="ListProducts"
         ),
    path("ProductByCategory/<category>",
         ProductByCategory.as_view(),
         name="ProductByCategory"
         ),
    path("DetailProduct/<pk>",
         DetailProduct.as_view(),
         name="DetailProduct"
         ),
    path("ProductUpdate/<pk>",
         ProductUpdate.as_view(),
         name="ProductUpdate"
         ),
    path("ProductDelete/<pk>",
         ProductDelete.as_view(),
         name="ProductDelete"
         ),
]
