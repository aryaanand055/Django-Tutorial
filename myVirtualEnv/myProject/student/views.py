from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Student


# Create your views here.
def schedule(request):
    template = loader.get_template("schedule.html")
    return HttpResponse(template.render())


def studentsList(request):
    studentsList = Student.objects.all().values()
    template = loader.get_template("student_list.html")
    context = {"students": studentsList}
    return HttpResponse(template.render(context, request))


def studentsDetails(request, id):
    student = Student.objects.get(id=id)

    template = loader.get_template("student_details.html")
    context = {"student": student}
    return HttpResponse(template.render(context, request))


def testing(request):
    template = loader.get_template("template.html")
    context = {
        "fruits": ["Apple", "Banana", "Cherry"],
    }
    return HttpResponse(template.render(context, request))
