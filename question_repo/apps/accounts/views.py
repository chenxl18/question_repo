from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def test(request):
    return HttpResponse("功能还在测试中")

def index(request):
    return render(request, "index.html")