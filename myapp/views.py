from django.shortcuts import render
from myapp.models import Product

def product_list(request):
    products = Product.objects.all()
    context = {
        "products_list": products
    }
    return render(
        request,
        "myapp/product_list.html",
        context=context, 
    )


def get_product_by_id(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        "product": product,
    }
    return render(
        request,
        "myapp/product_details.html",
        context=context
    )