from django.shortcuts import render
from myapp.models import User
from django.http import HttpResponse


# Create your views here.

def index(request):
    context = {'params': "test params"}
    return render(request, 'index.html', context)


def save_user(request):
    u = User(name="tmm", sex=0, age=25)
    u.save()
    return HttpResponse("success")
