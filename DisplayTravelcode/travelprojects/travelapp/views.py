from django.http import HttpResponse
from django.shortcuts import render
from .models import home
from .models import mypage


# Create your views here.
def demo(request):
    obj = home.objects.all()
    return render(request, "index.html", {'result': obj})

def demo(request):
    objt = mypage.objects.all()
    return render(request, "index.html", {'results': objt})
