from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.
def home(request):
    # return render(request,'home.html')
    string = "django learning"
    tlist = [i for i in range (1,10)]
    info_dict={'site':'lawtribes','content':'law search'}
    List = map(str,range(20))

    return render(request,'home.html',
    {'string':string,'tlist':tlist,
    'info_dict':info_dict,'List':List})


def index(request):
    return HttpResponse("HELLO,WORLD!YOU'RE AT THE INDEX.IT'S {}".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())))