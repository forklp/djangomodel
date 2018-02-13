from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from mysite import models
# Create your views here.

def index(request):
    products = models.Product.objects.all()
    template = get_template('index.html')
    html = template.render(locals())
    return HttpResponse(html)

def form(request):
    template= get_template('form.html')
    try:
        urid = request.GET['user_id']
        urpass = request.GET['user_pass']
        urfcolor = request.GET.getlist('fcolor')
        uryear = request.GET['byear']
    except:
        urid = None

    if urid != None and urpass == '12345':
        verified = True
    else:
        verified = False
    years = range(1960, 2021)
    html = template.render(locals())
    return HttpResponse(html)
