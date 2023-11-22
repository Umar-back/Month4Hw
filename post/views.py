from django.shortcuts import HttpResponse, render

from post.models import Product


def main_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all() # QuerySet

        context = {
            "products": products,
        }

        return render(request, 'products/products.html', context=context)


def date_view(request):
    return HttpResponse('22.11.2023')

def by_view(request):
    return HttpResponse('Goodbye user!')
