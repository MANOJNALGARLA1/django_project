from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def registration(request):
    template=loader.get_template('registration.html')
    return HttpResponse(template.render())


def kids(request):
    template=loader.get_template('kids.html')
    return HttpResponse(template.render())


def men(request):
    template=loader.get_template('men.html')
    return HttpResponse(template.render())


def women(request):
    template=loader.get_template('women.html')
    return HttpResponse(template.render())






