from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
def home(request):
    template = loader.get_template("file1.html")
    return HttpResponse(template.render())


def about(request):
    template = loader.get_template("file2.html")
    return HttpResponse(template.render())


def sayHello(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())
