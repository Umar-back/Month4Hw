from django.shortcuts import HttpResponse, render
from post.models import Product, Category

def main_view(request):
    if request.method == "GET":
        return render(request, 'index.html')

def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context = {"products": products}
        return render(request, 'products/products.html', context=context)

def products_detail_view(request, product_id):
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return render(request, 'errors/404.html')
        context = {'product': product}
        return render(request, 'products/product_detail.html', context=context)

def date_view(request):
    return HttpResponse('22.11.2023')

def by_view(request):
    return HttpResponse('Goodbye user!')

def category_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {"categories": categories}
        return render(request, 'products/categories.html', context=context)
