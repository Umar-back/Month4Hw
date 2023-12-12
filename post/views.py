from django.shortcuts import HttpResponse, render, redirect
from post.models import Product, Category
from post.forms import ProductCreateForm
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
        context = {
            'product': product
        }
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


def product_create(request):
    if request.method == 'GET':
        return render(request, 'products/create.html')
    if request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            Product.objects.create(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                image=form.cleaned_data['image'],
                rating=form.cleaned_data['rate']
                )
        return redirect("/products/")