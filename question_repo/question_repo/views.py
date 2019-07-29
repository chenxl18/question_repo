from django.shortcuts import HttpResponse,render
import logging

# apis为settings中Logging配置中的loggers
logger = logging.getLogger('apis')

def logtest(request):
    logger.info("欢迎访问")
    return HttpResponse('日志测试')

def base(request):
    return render(request,"base.html")