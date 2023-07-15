from django.shortcuts import render
from product.models import product


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')

def prodcuts_view(request):
    if request.method == 'GET':
        posts = product.objects.all()
        context_data = {
            'products': product
        }

        return render(request, 'products/products.html', context=context_data)