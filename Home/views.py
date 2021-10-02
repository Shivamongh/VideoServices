from django.shortcuts import render
from .models import *
# Create your views here.
def home(reuest):
    courses = Course.objects.all()
    print(courses)
    context = {'course': courses}
    return render(reuest, 'Home/home.html', context)

def view_courses(request, slug):
    course = course.objects.filter(slug = slug).first()
    course_module = CourseModule.objects.filter(course = course)
    context = {'course':course , 'course_module': course_module}
    render(request, 'course.html', context)