from django.conf.urls import url, include
from . import views

urlpatterns = [
    # 获取手机验证码
    url(r'^get_mobile_captcha/$', views.get_mobile_captcha, name='get_mobile_captcha'),
    url(r'^get_captcha/$', views.get_captcha, name='get_captcha'),
    url(r'^check_captcha/$', views.check_captcha, name='check_captcha'),
    url(r'^questions/$', views.QuestionsView.as_view(), name='questions'),
    url(r'^question/collection/(?P<id>\d+)/$', views.QuestionCollectionView.as_view(), name='question_collection'),
    # 参考答案接口
    url(r'^answer/(?P<id>\d+)/$', views.AnswerView.as_view(), name="answer"),
    # 某题所有人的回答接口
    url(r'^other_answer/(?P<id>\d+)/$', views.OtherAnswerView.as_view(), name="other_answer"),
    url(r'^answer/collection/(?P<id>\d+)/$', views.AnswerCollectionView.as_view(), name='answer_collection'),
    # 修改头像
    url(r'^change_avator/$', views.ChangeAvator.as_view(),name='change_avator'),
    ]