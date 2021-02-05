# controllers
from django.shortcuts import render
from time import localtime, strftime

def index(request):
    context = {
        "date": strftime("%b %m, %Y", localtime()),
        "hour": strftime("%H:%M %p", localtime())
    }
    return render(request, 'index.html', context)