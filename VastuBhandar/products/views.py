from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from .forms import ProductForms
from .models import Product


class AddProduct(CreateView):
    form_class = ProductForms
    success_url = "/UserLogin"
    template_name = "register.html"


class ListProducts(ListView):
    template_name = "product.html"
    model = Product


class DetailProduct(DetailView):
    pass
    # template_name = "two.html"
    # model = Product


class ProductDelete(DeleteView):
    template_name = "Delete.html"
    model = Product


class ProductUpdate(UpdateView):
    template_name = "Update.html"
    model = Product
    form_class = ProductForms


class ProductByCategory(View):

    def get(self, request, category):
        try:
            data = Product.objects.filter(category=category)
            return render(request, template_name='product.html', context={"object_list": data})
        except None:
            return render(request, template_name='product.html')
