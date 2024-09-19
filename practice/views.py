from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    data = {
        "title": "Home Page",
        "bodyData": "Welcome to my first page. This templates need to be included on the settings.py inside the templates section.",
        "languages": ["Javascript", "Python", "Ruby", "C#"],
    }
    return render(request, "index.html", data)


def aboutUs(request):
    return HttpResponse("Welcome to about us")


def course(request):
    return HttpResponse("Welcome to my course")


def courseDetail(request, courseId):
    return HttpResponse("Welcome to {courseId} course.".format(courseId=courseId))
