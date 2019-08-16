"""

"""

from . import settings


def site_info(request):
    # 站点基本信息
    site = {}
    # site["SITE_URL"] = settings.SITE_URL
    site["SITE_NAME"] = settings.SITE_NAME
    site["SITE_DESC"] = settings.SITE_DESC
    # site["PRO_GIT"] = settings.PRO_GIT
    # site["PRO_RSS"] = settings.PRO_RSS
    # site["WEIBO_URL"] = settings.WEIBO_URL
    return locals()


# from libs.repo_data import user_answer_data
# from apps.repo.models import Answers,Category
#
# def repo_data(request):
#     if request.user.is_authenticated:
#         user_data = user_answer_data(request.user)
#         hot_question = Answers.objects.hot_question()
#         hot_user = Answers.objects.hot_user()
#         category = Category.objects.all()
#     # current_url = request.path
#     return locals()
