from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_view(request,*args, **kwargs):
    return HttpResponse("<h1>hello miskat</h1>")


def home(request, *args, **kwargs):
    contex={
        "name":"showmik"
    }
    return render(request, "home.html",contex)


def form(request):
    #print(request.POST)
    #print(request.GET)
    if request.method == "GET":
        return render(request, "forms.html")

    if request.method == "POST":
        Title = request.POST['title']
        Content = request.POST['content']
        Price = request.POST['price']     

        context = {
            "Title": Title,
            "content" : Content,
            "price": Price,
        } 

        return render(request, "forms.html",context)
