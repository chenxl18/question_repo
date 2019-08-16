"""
放自定义信号
"""
import django.dispatch
# 自定义信号（有两个参数arg1,arg2）
mysignal = django.dispatch.Signal(providing_args=['arg1','arg2'])

# 自定义信号不会自动触发
# 内置信号