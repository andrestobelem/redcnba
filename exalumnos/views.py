# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    return render(request, "exalumnos/home.html", context)