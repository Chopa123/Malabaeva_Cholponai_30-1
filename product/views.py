from django.db.models import Q
from django.shortcuts import render, redirect
from product.models import product, Category, Review
from product.forms import ProductCreateForm, ReviewCreateForm
from product.constants import PAGINATION_LIMIT

def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = product.objects.all()
        max_page = products.__len__() / PAGINATION_LIMIT
        if round(max_page)<max_page:
            max_page= round(max_page)+1
        else:
            max_page = round(max_page)

        search_text = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if search_text:
            products = products.filter(Q(title__icontains=search_text) |
                                       Q(description__icontains=search_text))

            products=products[PAGINATION_LIMIT*(page-1):PAGINATION_LIMIT*page]

            context_data = {
                'products': products,
                'user': request.user,
                'pages': range(1, max_page + 1)
            }

        return render(request, 'products/products.html', context=context_data)


def categories_view(request):
    categories = Category.objects.all()
    return render(request, 'categories/categories.html', {'categories': categories})


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
