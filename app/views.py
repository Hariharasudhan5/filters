from django.shortcuts import render
import datetime
# Create your views here.
def filter(request):
    dt=datetime.datetime.now()
    d={'data':'tomorrow is a pongal celebration','dt':dt,'n':3}
    return render(request,'filter.html',d)