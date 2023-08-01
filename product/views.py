from django.shortcuts import render, redirect
from product.models import product, Category, Review
from product.forms import ProductCreateForm, ReviewCreateForm


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = product.objects.all()
        context_data = {
            'products': products,
            'user': request.user
        }

        return render(request, 'products/products.html', context=context_data)


def categories_view(request):
    categories = Category.objects.all()
    return render(request, 'categories/categories.html', {'categories': categories})


# def products_detail_view(request, id):
#     if request.method == 'GET':
#         products = product.objects.get(id=id)
#
#         context_data = {
#             'product': products
#         }
#         return render(request, 'products/detail.html', context=context_data)

def products_detail_view(request, id):
    if request.method == 'GET':
        products = product.objects.get(id=id)

        context = {
            'product': products,
            'reviews': products.reviews.all(),
            'form': ReviewCreateForm
        }

        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        products = product.objects.get(id=id)
        data = request.POST
        form = ReviewCreateForm(data=data)

        if form.is_valid():
            Review.objects.create(
                text=form.cleaned_data.get('text'),
                product=products
            )

        context = {
            'product': products,
            'review': products.reviews.all(),
            'form': form
        }

        return render(request, 'products/detail.html', context=context)


def product_create_view(request):
    if request.method == 'GET':
        context_data = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=context_data)

    if request.method == 'POST':
        data, files = request.PRODUCT, request.FILES
        form = ProductCreateForm(data, files)

        if form.is_valid():
            product.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate'),
            )
            return redirect('/products/')

        return render(request, 'products/create.html', context={
            'form': form
        })
