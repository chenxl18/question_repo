from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import View, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.repo.models import Category, Questions, User, Answers
from django.core import serializers
from django.db import transaction
from django.http import JsonResponse
from apps.repo.models import UserLog
import json, logging

logger = logging.getLogger('repo')


# Create your views here.
def test(request):
    return HttpResponse("功能还在测试中~")


def question_detail(request):
    return render(request, "question_detail.html")


@login_required
def index(requeset):
    # userlog = UserLog.objects.all().order_by('-create_time')[:10]
    userlog = UserLog.objects.all()[:10]
    operator = dict(UserLog.OPERATE)
    for log in userlog:
        log.operate_cn = operator[int(log.operate)]
    recent_user_ids = [item['user'] for item in UserLog.objects.filter(operate=3).values('user').distinct()[:10]]
    recent_user = User.objects.filter(id__in=recent_user_ids)
    kwgs = {
        "userlog": userlog,
        'recent_user': recent_user,
    }
    # print(kwgs)
    return render(requeset, "index.html", kwgs)


class QuestionsList(LoginRequiredMixin, View):
    def get(self, request):
        category = Category.objects.all().values('id', 'name')
        grades = Questions.DIF_CHOICES
        # 添加search参数，以便搜索刷新后在页面上还能看到搜索的关键字
        search_key = request.GET.get("search", '')
        kwgs = {"category": category, "grades": grades, "search_key": search_key}
        return render(request, 'questions.html', kwgs)


class QuestionDetail(LoginRequiredMixin, DetailView):
    model = Questions
    pk_url_kwarg = 'pk'
    template_name = "question_detail.html"
    # 默认名：object
    context_object_name = "object"

    # 额外传递my_answer
    def get_context_data(self, **kwargs):
        # kwargs：字典、字典中的数据返回给html页面
        # self.get_object() => 获取当前id的数据（问题）
        question = self.get_object()  # 当前这道题目
        kwargs["my_answer"] = Answers.objects.filter(question=question, user=self.request.user)
        return super().get_context_data(**kwargs)

    def post(self, request, id):

        try:
            # 没有回答过。create
            # 更新回答。get->update
            # 获取对象，没有获取到直接创建对象
            with transaction.atomic():
                # data_answer: 用户提交的数据
                data_answer = request.POST.get('answer', "没有回答")
                new_answer = Answers.objects.get_or_create(question=self.get_object(), user=self.request.user)
                # 元组：第一个元素获取/创建的对象， True（新创建）/False（老数据）
                new_answer[0].answer = data_answer
                new_answer[0].save()
                UserLog.objects.create(user=request.user, operate=3, question=self.get_object(), answer=new_answer[0])
            my_answer = json.loads(serializers.serialize("json", [new_answer[0]]))[0]["fields"]
            msg = "提交成功"
            code = 200
            # OPERATE = ((1, "收藏"), (2, "取消收藏"), (3, "回答"))
            # raise  TypeError
            # result = {'status': 1, 'msg': '提交成功', 'my_answer': my_answer}
            # return JsonResponse(result)
            # todo: 做一些判断=》 提交失败或其他异常情况
        except Exception as ex:
            logger.error(ex)
            my_answer = {}
            msg = "提交失败"
            code = 500
        result = {"status": code, "msg": msg, "my_answer": my_answer}
        return JsonResponse(result)


@login_required
def questions(request):
    category = Category.objects.all()
    grades = Questions.DIF_CHOICES
    search = request.GET.get("search", "")
    kwgs = {"category": category,
            "grades": grades,
            "search_key": search
            }
    return render(request, "questions.html", kwgs)


class Question(LoginRequiredMixin, View):
    def post(self, request):
        # print(request.POST)
        try:
            title = request.POST.get("title")
            category = request.POST.get("category")
            content = request.POST.get("content")
            if category:
                Questions.objects.create(title=title, category_id=category, content=content, contributor=request.user)
            else:
                Questions.objects.create(title=title, content=content, contributor=request.user)
        except Exception as ex:
            logger.error(ex)
            # return render(request,'uc_profile.html',"提交失败!")
            return HttpResponse('提交失败!')
        # return render(request,'uc_profile.html',"提交成功!")
        return HttpResponse('提交成功!')

        # form全局commit
        # ajax提交form



from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def listing(request):
    questions_list = Questions.objects.all()
    p = Paginator(questions_list, 25)

    page = request.GET.get('page')
    # page = int(page)
    try:
        qs = p.page(page)
    except PageNotAnInteger:
        qs = p.page(1)
    except EmptyPage:
        qs = p.page(p.num_pages)
    return render(request, 'list.html', {'qs':qs})
