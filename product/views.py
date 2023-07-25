from django.shortcuts import render
from product.models import product, Category


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = product.objects.all()
        context_data = {
            'products': products
        }

        return render(request, 'products/products.html', context=context_data)


def categories_view(request):
    categories = Category.objects.all()
    return render(request, 'categories/categories.html', {'categories': categories})

def products_detail_view(request, id):
    if request.method == 'GET':
        products = product.objects.get(id=id)

        context_data = {
            'product': products
        }
        return render(request, 'products/detail.html', context=context_data)
