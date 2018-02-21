from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import RequestContext, Context
from mysite import models, forms
from django.core.mail import EmailMessage
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

def posting(request):

    products = models.Product.objects.all()
    return render(request, 'posting.html', Context(locals()))

def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            message = '感谢来信'
            user_name = form.cleaned_data['user_name']
            user_city = form.cleaned_data['user_city']
            user_school = form.cleaned_data['user_school']
            user_email = form.cleaned_data['user_email']
            user_message = form.cleaned_data['user_message']

            # mail_body = u'''
            # 网友姓名:{}
            # 居住城市:{}
            # 是否在学:{}
            # 反映意见如下:{}
            # '''.format(user_name, user_city, user_school, user_message)
            # email = EmailMessage('来自网友', mail_body, user_email, ['k1637108208@aliyun.com'])
            # email.send()
            return HttpResponseRedirect('/index/')
        else:
            message = '请检查输入'
    else:
        form = forms.ContactForm()

    return render(request,'contact.html', Context(locals()))

def post2db(request):
    product_form = forms.ProductForm()
    pmodels = models.PModel.objects.all()
    return render(request, 'post2db.html', Context(locals()))