from django.shortcuts import render
from.models import own_production, user1, Autorization,Articl
from.forms import ArticlForm, Own_productionForm
from django.views.generic import DetailView


# Create your views here.

def index(request):
    context = {
        "product":own_production.objects.all(),
        }
    return render(request, 'HZ/sklad.html', context)

class NewsDetail(DetailView):
    model = Articl
    template_name = "HZ/about_views.html"
    context_object_name = 'art'

def about(request):
    news = Articl.objects.all()
    return render(request, 'HZ/about.html', {'news':news})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма заполнена не верно'
    form = ArticlForm()
    data = {
        'form':form,
        'error':error,

    }
    return render(request, 'HZ/about_news.html', data)

def create_prod(request):
    error = ''
    if request.method == 'POST':
        prod = Own_productionForm(request.POST)
        if prod.is_valid():
            prod.save()
        else:
            error = 'Форма заполнена не верно'
    prod = Own_productionForm()
    expend = {
        'prod':prod,
        'error': error,

    }
    return render(request, 'HZ/home_sklad.html', expend)





