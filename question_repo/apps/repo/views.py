from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def test(request):
    return HttpResponse("功能还在测试中~")
def index(request):
    return render(request,"index.html")
def questions(request):
    return render(request,"questions.html")
def question_detail(request):
    return render(request,"question_detail.html")

@login_required
def index(requeset):
    return render(requeset,"index.html")