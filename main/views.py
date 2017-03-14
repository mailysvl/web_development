from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render(request))


def basket(request):
    template = loader.get_template('basket.html')
    return HttpResponse(template.render(request))


def search(request):
    if request.POST.get('click', False):
        print("clicked")
