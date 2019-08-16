from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # 首页
    url(r'^$',views.index, name="index"),
    # 题目列表
    url(r'^questions/$',views.QuestionsList.as_view(), name="questions"),
    # 贡献题目
    url(r'^question/$',views.Question.as_view(), name="question"),
    # 题目详情，捕获一个参数
    url(r'^question/(?P<pk>\d+)/$', views.QuestionDetail.as_view(), name="question_detail"),
    # 分页
    url(r'^paginator/$',views.listing,name='paginator'),
]