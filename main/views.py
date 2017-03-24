from django.http import HttpResponse
from django.shortcuts import render

from .models import Product, User, Order, ItemOrdered

appname = 'BRACYs'


def loggedin(f):
    def test(request):
        if 'username' in request.session:
            return f(request)
        else:
            return render(request, 'base.html', context={'appname': appname, 'loggedin': False})

    return test


def index(request):
    context = {'appname': appname}
    return render(request, 'base.html', context)


def basket(request):
    user = User.objects.get(username='ks')
    order = Order.objects.get(user=user)
    item = ItemOrdered.objects.filter(order_id=order)
    total = order.total
    context = {'appname': appname, 'item': item, 'total': total}
    return render(request, 'basket.html', context)


def add_to_basket(request):
    if request.POST['product_id']:
        product_id = request.POST['product_id']
        member = User.objects.get(username='ks')
        item = Product.objects.get(pk=product_id)
        total = item.price

        order = Order.objects.get(user=member.id)
        if order is None:
            new_order = Order(user=member, total=total)
            new_order.save()

        else:

            total = order.total + item.price
            new_order = order
            new_order.total = total
            new_order.save()
        item_ordered = ItemOrdered(order_id=new_order.id, product=item, quantity=1)
        item_ordered.save()
        return render(request, 'basket.html', {'appname': appname})


def product(request):
    products = Product.objects.all()
    image = [1, 2, 3, 4, 5, 6]
    data = {'appname': appname,
            'products': products,
            'image': image}

    return render(request, 'product.html', context=data)


def search(request):
    if request.POST:
        search_query = request.POST.get('q')
        product = Product.objects.filter(product_name__icontains=search_query)
        image = [1, 2, 3, 4, 5, 6]
        context = {'appname': appname,
                   'products': product,
                   'image': image}
        return render(request, 'product.html', context)


def login(request):
    if 'username' not in request.POST:
        context = {'appname': appname}
        return render(request, 'base.html', context)
    else:
        u = request.POST['username']
        p = request.POST['password']
        try:
            member = User.objects.get(username=u)
        except User.DoesNotExist:
            return render(request, 'base.html', {
                'appname': appname,
                'exist': False
            })
        if p == member.password:
            request.session['username'] = u
            request.session['password'] = p
            return render(request, 'base.html', {
                'appname': appname,
                'username': u,
                'success': True})
        else:
            return HttpResponse("Wrong password")


def register(request):
    if request.POST:
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']
        password = request.POST['password']
        c_password = request.POST['confirm_password']

        if password == c_password:
            user = User(name=name, username=username, email=email, address=address, password=password)
            user.save()
            return render(request, 'base.html', context={'appname': appname,
                                                         'username': username,
                                                         'success': True})
        else:
            return render(request, 'base.html', context={'appname': appname,
                                                         'success': False})


def contact(request):
    return render(request, 'contact.html', context={'appname': appname})


def checkRegUser(request):
    if 'username' in request.POST:
        u = request.POST['username']
        try:
            User.objects.get(username=u)
            return HttpResponse("<span class='taken'>&nbsp;#x2718; This username is taken</span>")
        except User.DoesNotExist:
            return HttpResponse("<span class='available'>&nbsp;#x2714; This username is available</span>")
    else:
        return HttpResponse("Username is required")


def checkLogUser(request):
    if 'username' in request.POST:
        u = request.POST['username']
        try:
            User.objects.get(username=u)
            return HttpResponse("")
        except User.DoesNotExist:
            return HttpResponse("<span class='available'>&nbsp;#x2718; Unknown username</span>")
    else:
        return HttpResponse("")


def update_basket(request):
    if 'quantity' in request.POST:
        item = request.POST['product_id']
        quan = request.POST['quantity']
        get_item = ItemOrdered.objects.get(product=item)
        get_item.quantity = quan
        get_item.save()

        return render(request, 'basket.html', {'appname': appname})


def remove(request):
    if 'product_remove' in request.POST:
        user = User.objects.get(username='ks')
        remove_id = request.POST['product_remove']
        get_pro = ItemOrdered.objects.get(product_id=remove_id)
        get_pro.delete()
        order = Order.objects.get(pk=get_pro.order.id)
        total = 0
        for i in ItemOrdered.objects.filter(order_id=order):
            total = total + (i.product.price * i.quantity)
        return render(request, 'basket.html', {'appname': appname})
