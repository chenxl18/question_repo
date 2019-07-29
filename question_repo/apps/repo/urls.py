from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # 首页
    url(r'^$',views.index, name="index"),
    # 题目列表
    url(r'^questions/$',views.questions, name="questions"),
    # 贡献题目
    url(r'^question/$',views.test, name="question"),
    # 题目详情，捕获一个参数
    url(r'^questions/id/$',views.question_detail, name="question_detail"),
]