"""
Django settings for question_repo project.

Generated by 'django-admin startproject' using Django 1.11.20.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l$q1_)yram9iudgh$cb@o3dh*&j&#+i@*6s)+^(ig@%1ml^k5#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SITE_NAME = '题库系统'
SITE_DESC = '人生苦短，我用Python'
SITE_KEYWORDS = 'python, django, flask'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.repo.apps.RepoConfig',
    'apps.accounts',
    'apps.usercenter',
    'apps.apis',
    # 'apps.forms_base',
    'ckeditor',
    'ckeditor_uploader',
    'easy_thumbnails',
]

THUMBNAIL_ALIASES = {
    '':{
        'avator': {'size':(50, 50), 'crop':True},
    }
}


# 注意：在此之前需要配置MEDIA_URL和MEDIA_ROOT
# 配置媒体文件路径
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
if not os.path.exists(MEDIA_ROOT):
    os.mkdir(MEDIA_ROOT)
MEDIA_URL = '/media/'
# 单位：px
THUMB_SIZE = 70
if not os.path.exists(MEDIA_ROOT):
    os.mkdir(MEDIA_ROOT)

# 修改上传文件大小（Default: 2621440 (i.e. 2.5 MB).）
DATA_UPLOAD_MAX_MEMORY_SIZE = 2621440*10

# CKEditor配置
# 真实路径为：MEDIA_URL+CKEDITOR_UPLOAD_PATH(MEDIA_ROOT/CKEDITOR_UPLOAD_PATH)
CKEDITOR_UPLOAD_PATH = "ckeditor_upload"

CKEDITOR_CONFIGS = {
    'default': {
        'update': ['Image', 'Update', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak'],
        'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',
            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join(
            [
                # your extra plugins here
                'div',
                'autolink',
                'autoembed',
                'embedsemantic',
                'autogrow',
                # 'devtools',
                'widget',
                'lineutils',
                'clipboard',
                'dialog',
                'dialogui',
                'elementspath'
            ]),
    }
}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'question_repo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'question_repo.context_processors.repo_data',
                'apps.repo.context_processors.repo_data',

            ],
        },
    },
]

WSGI_APPLICATION = 'question_repo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

# 自定义用户model： "应用名.Model名
AUTH_USER_MODEL = 'accounts.User'
# 注意：如果扩展了User一定需要指定AUTH_USER_MODEL

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

# 通过CMD方式插入数据时，因为数据包含日期类型，所以会报： RuntimeWarning: DateTimeField Event.starttime received a naive datetime (2016-09-02 10:20:00) while time zone support is active.的错误。
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# 静态文件的查找路径
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(os.path.join(BASE_DIR, "static"))
]

STATIC_ROOT = os.path.join(BASE_DIR, 'allstatic')

# 配置日志
LOG_ROOT = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOG_ROOT):
    os.mkdir(LOG_ROOT)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}  #日志格式
    },
    'filters': {
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
            },
        'default': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_ROOT, 'all.log'),     # 日志输出文件
            'maxBytes': 1024*1024*5,       # 文件大小
            'backupCount': 5,              # 备份份数
            'formatter':'standard',        # 使用哪种formatters日志格式
        },
        'error': {
            'level':'ERROR',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_ROOT, 'error.log'),
            'maxBytes':1024*1024*5,
            'backupCount': 5,
            'formatter':'standard',
            },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'request_handler': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_ROOT, 'script.log'),
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'formatter':'standard',
            },
        'scripts_handler': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_ROOT, 'script.log'),
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'formatter':'standard',
            },
        'account_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_ROOT, 'account.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'apis_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_ROOT, 'apis.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        'repo_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_ROOT, 'repo.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        }
    },
    'loggers': {
        # 'django': {
        #     'handlers1': ['console'],
        #     'level': 'DEBUG',
        #     'propagate': False
        # },
        'account':{
            'handlers': ['account_handler', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'apis': {
            'handlers': ['apis_handler', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'repo': {
            'handlers': ['repo_handler', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}

CACHES = {
    'default': {
        # BACKEND配置缓存后端为RedisCache
        'BACKEND': 'django_redis.cache.RedisCache',
        # LOCATION配置redis服务器地址
        'LOCATION': 'redis://192.168.0.156:6379',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
             "PASSWORD": "rootroot",
        },
    },
}

# # 以下配置可参考，在settings自定义配置项，方便统一管理
# REDIS_TIMEOUT=7*24*60*60
# CUBES_REDIS_TIMEOUT=60*60
# NEVER_REDIS_TIMEOUT=365*24*60*60

FontPath = os.path.join(BASE_DIR,"static/fonts/")


# 配置发送邮件
DEFAULT_FROM_EMAIL = '1210972564@qq.com'
# 163邮箱SMTP服务器地址
EMAIL_HOST = 'smtp.qq.com'
# 发件人的邮箱
EMAIL_HOST_USER = '1210972564@qq.com'
# 发件人邮箱密码
EMAIL_HOST_PASSWORD = 'iasaxjxzhbatgfja'
# tls协议，有True和False两种情况
EMAIL_USE_TLS = True
# 发件人的邮箱
EMAIL_FROM = '1210972564@qq.com'