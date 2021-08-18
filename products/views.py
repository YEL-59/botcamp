from typing import ContextManager
from django.shortcuts import redirect, render
from django.http import HttpResponse
# Create your views here.
from .models import Product


def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>hello miskat</h1>")


def home(request, *args, **kwargs):
    contex = {
        "name": "showmik"
    }
    return render(request, "home.html", contex)


def form(request):
    # print(request.POST)
    # print(request.GET)
    if request.method == "GET":
        return render(request, "forms.html")

    elif request.method == "POST":
        Title = request.POST['title']
        Content = request.POST['content']
        Price = request.POST['price']
        Product.objects.create(title=Title, content=Content, price=Price)
        render(request, "forms.html")

    return redirect('/showa')


def show(request):
    if request.method == "GET":
        obj = Product.objects.all()
        context = {
            "obj": obj
        }
        return render(request, 'home.html', context)


def se(request):
    if request.method == "GET":
        return render(request, 'search.html')

    elif request.method == "POST":
        name = request.POST['search']
        obj = Product.objects.get(title=name)

        Context = {
            "obj": obj
        }

        return render(request, 'search.html', Context)