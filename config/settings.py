import os

from config.django_starter import config_django_starter
from config.logging import config_logging, config_debug_logging
from config.caches import config_caches
from config.rest_framework import config_rest_framework

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@4gkf7*k+_1@u8z$2*ila%%)ck&i=o$g1lnr40=%mlt-4rh+xd'

# SECURITY WARNING: don't run with debug turned on in production!
# 读取环境变量判断是否开启Debug模式，无须手动设置
DEBUG = os.environ.get('DEBUG', 'true') == 'true'

# 读取环境变量判断是否docker环境，无须手动设置
DOCKER = os.environ.get('ENVIRONMENT', 'default') == 'docker'

# 读取环境变量，设置URL前缀
URL_PREFIX = os.environ.get('URL_PREFIX', '')
# 不为空则后面加个斜杠
if len(URL_PREFIX) > 0:
    URL_PREFIX += '/'

ALLOWED_HOSTS = ['*']

# 应用定义
INSTALLED_APPS = [
    # 后台扩展
    'simpleui',
    'multi_captcha_admin',

    # Django核心
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # DjangoStarter组件
    'django_starter.contrib.admin',
    'django_starter.contrib.auth',
    'django_starter.contrib.code_generator',
    'django_starter.contrib.config',
    'django_starter.contrib.guide',
    'django_starter.contrib.oauth',
    'django_starter.contrib.rest_framework',

    # 第三方组件
    'captcha',
    'drf_yasg',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',

    # 我们自己的应用
    'apps.demo',
    'apps.oda'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls_root'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',

            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# 数据库配置
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangostarter',
        'USER': 'root',
        'PASSWORD': 'Dd678678,,',
        'HOST': '192.168.2.189',
        'PORT': 3306,
    }
}
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 密码验证配置
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

# 国际化配置
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = False

# 日志配置
# 不是调试模式才开启日志记录
if DEBUG:
    LOGGING = config_debug_logging()
else:
    LOGGING = config_logging(BASE_DIR)

# 静态文件配置 (CSS, JavaScript, Images)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static_collected')
STATIC_URL = f'/{URL_PREFIX}static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = f'/{URL_PREFIX}media/'

# 配置redis缓存
CACHES = config_caches(DOCKER)

# Drf 配置
REST_FRAMEWORK = config_rest_framework()

# 验证码配置
MULTI_CAPTCHA_ADMIN = {
    'engine': 'simple-captcha',
}

# Cors Header 配置
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)
CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)

# SimpleUI 配置
SIMPLEUI_DEFAULT_THEME = 'admin.lte.css'  # 默认主题
# SIMPLEUI_LOGO = f'/{URL_PREFIX}static/admin/images/custom_logo.png'
SIMPLEUI_HOME_PAGE = f'/{URL_PREFIX}django-starter/admin/extend_home/'
SIMPLEUI_HOME_ICON = 'fa fa-home'
SIMPLEUI_HOME_INFO = False  # 显示服务器信息
SIMPLEUI_HOME_QUICK = True  # 快速操作
SIMPLEUI_HOME_ACTION = True  # 最近动作
SIMPLEUI_ANALYSIS = False  # 关闭使用分析
SIMPLEUI_STATIC_OFFLINE = True  # 离线模式
SIMPLEUI_ICON = {
    'Core': 'fa fa-cat',
    '令牌': 'fa fa-lock',
    '认证令牌': 'fa fa-lock',
}

# Swagger 配置
SWAGGER_SETTINGS = {
    'DEFAULT_AUTO_SCHEMA_CLASS': 'config.swagger.CustomSwaggerAutoSchema',
    'DEFAULT_GENERATOR_CLASS': 'config.swagger.CustomOpenAPISchemaGenerator',
    # Controls the default expansion setting for the operations and tags.
    # ‘none’: everything is collapsed
    'DOC_EXPANSION': 'none',
}

# DjangoStarter 框架配置
DJANGO_STARTER = config_django_starter()
