"""question_repo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views



urlpatterns = [
    # url(r'^accounts', include('apps.accounts.urls',namespace='accounts')),
    # 注册
    url(r'^register/$', views.Register.as_view(), name='register'),
    # 登录
    url(r'login/$',views.Login.as_view(), name="login"),
    # 退出
    url(r'logout/$', views.logout, name="logout"),
    # 忘记密码
    url(r'password/forget/$', views.PasswordForget.as_view(), name="password_forget"),
    # 重置密码
    url(r'password/reset/(\w+)/$', views.PasswordReset.as_view(), name="password_reset"),

]
