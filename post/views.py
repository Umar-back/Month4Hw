from django.shortcuts import HttpResponse, render

from post.models import Product, Hashtag, Comment

from django.shortcuts import HttpResponse, render

from post.models import Product, Hashtag, Comment

def main_view(request):
    # post = Product.objects.get(id=1)
    # hashtag = Hashtag.objects.get(id=1)
    # hashtag.products.all()
    # comments = post.comments.all()
    # hashtags = post.comments.all()
    # print(comments)
    # print(hashtags)
    # for i in comments:
    #     print(i.text)
    if request.method == "GET":
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


def category_view(request):
    if request.method == 'GET':
        hashtags = Hashtag.objects.all()

        context = {
            "hashtags": hashtags
        }

        return render(request, 'products/categories.html', context=context)