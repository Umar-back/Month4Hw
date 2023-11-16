from django.shortcuts import HttpResponse, render

# CDV - Class Based View
# FBV - Function

def hello_view(request):
    print(request.method)
    if request.method == 'GET':
        return render(request, 'index.html')


def date_view(request):

    return HttpResponse('16.11.2023')

def by_view(request):

    return HttpResponse("Goodby user!")