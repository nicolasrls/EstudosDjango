from django.shortcuts import render
from django.http import HttpResponse
import datetime

def home(request):
    now = datetime.datetime.now()
        # html = "<html><body><h1>Testando {} HTML com django {}</h1></body></html>".format("Nicolas", now)
    return render(request, 'site/home.html')

