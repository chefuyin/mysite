from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.
def index(request):
    return HttpResponse("HELLO,WORLD!YOU'RE AT THE INDEX.IT'S {}".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())))