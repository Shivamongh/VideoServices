
from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('course/<slug>/', view_courses, name="course")
]