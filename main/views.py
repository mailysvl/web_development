from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Product, User


def index(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render(request))


def basket(request):
    template = loader.get_template('basket.html')
    return HttpResponse(template.render(request))


def product(request):
    products = Product.objects.all()
    data = {'products': products}

    return render(request, 'product.html', context=data)


def search(request):
    if request.method == 'POST':
        search_query = request.POST['q']
        searched = Product.objects.filter(product_name=search_query)

        return render(request, 'search.html', {'products': searched})


def login(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        try:
            user = User.objects.get(pk=u)
        except User.DoesNotExist:
            return HttpResponse("User does not exist")
        if p == user.password:
            request.session['username'] = u
            request.session['password'] = p
            return render(request, 'base.html',
                          {'username': u,
                           'loggedin': True}
                          )
