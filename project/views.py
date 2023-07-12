from django.shortcuts import HttpResponse, redirect
from datetime import datetime


def hello_view(requests):
    if requests.method == 'GET':
        return HttpResponse("Hello! Its my project")


def date_view(request):
    return HttpResponse(datetime.now())


def goodby_view(requests):
    if requests.method == 'GET':
        return HttpResponse("Goodby user!")
