from django.shortcuts import render,HttpResponse
from django.views.generic import View
import logging
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from .forms import  RegisterForm
from .models import User
logger = logging.getLogger('account')

# Create your views here.
def test(request):
    return HttpResponse("功能还在测试中")



# Create your views here.
class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "accounts/register.html", {"form": form})

    # Ajax提交表单
    def post(self, request):
        from django.core.cache import cache
        ret = {"status": 400, "msg": "调用方式错误"}
        if request.is_ajax():
            form = RegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                mobile = form.cleaned_data["mobile"]
                mobile_captcha = form.cleaned_data["mobile_captcha"]
                mobile_captcha_reids = cache.get(mobile)
                if mobile_captcha == mobile_captcha_reids:
                    user = User.objects.create(username=username, password=make_password(password))
                    user.save()
                    ret['status'] = 200
                    ret['msg'] = "注册成功"
                    logger.debug("新用户{}注册成功！".format(user))
                    user = auth.authenticate(username=username, password=password)
                    if user is not None and user.is_active:
                        auth.login(request, user)
                        logger.debug("新用户{}登录成功".format(user))
                    else:
                        logger.error("新用户{}登录失败".format(user))
                else:
                    # 验证码错误
                    ret['status'] = 401
                    ret['msg'] = "验证码错误或过期"
            else:
                ret['status'] = 402
                ret['msg'] = form.errors
        logger.debug("用户注册结果：{}".format(ret))
        return JsonResponse(ret)