from pathlib import Path
from hidekey import MY_DB_PASSWORD, SECRET_MY_KEY, MY_URL_ID # 키 숨기기위해 임포트
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#프로젝트의 기본위치 다른말로 루트패쓰

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_MY_KEY
#해쉬를 생성할때 만들어주는 문자열 이건 절대 배포X

# SECURITY WARNING: don't run with debug turned on in production!

###########################배포할떄

DEBUG = True #배포할때에는 False
#어떤 식으로 서버를 열것인지 false 중요!

ALLOWED_HOSTS = [
    MY_URL_ID,
] #나의 배포 아이디 작성




# Application definition
# 어플리케이션 설치후 적기
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dashboard.apps.DashboardConfig', #이렇게도 어플리케이션 추가 가능
    'payment',
    'cart',
    'myapp',
    'accounts',

    # The following apps are required:
    #소셜 로그인 기능 pip install django-allauth
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'allauth.socialaccount.providers.naver',
    'allauth.socialaccount.providers.google',
]

SITE_ID = 1 #소셜 로그인

#소셜 로그인 어떤 수단을 통해서 로그인을 할건지
AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend', #기존 장고 인증기능

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend', #추가한 소셜로그인 기능
    
]

#로그인을 성공했을때 url
LOGIN_REDIRECT_URL = '/'





MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'basicsettings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'basicsettings.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}


# 외부 데이터 베이스 연결 pip install mysqlclient 해주어야함 sqlite 연결시에는 다시 바꾸어주어야함
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysql',
        'USER' : 'root',
        'PASSWORD' : MY_DB_PASSWORD,
        'HOST' : '127.0.0.1',
        'PORT' : '3306',
        }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization  # 국제화 어떤 시간을 기준 어떤 언어를 기준
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
#'ko-kr'

TIME_ZONE = 'UTC'
#'Asia/Seoul'

USE_I18N = True

USE_TZ = True

LOGIN_REDIRECT_URL = "/" #로그인이 성공했을시 이동되는 url


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# 미리 준비한 정적인 대상들이 어디에 위치해 있는지
STATIC_URL = 'static/'

#static 파일들 위치 설정
STATICFILES_DIRS = [
    BASE_DIR / 'static',  #base dir은 최상위 디렉토리 manage.py와 같이있는 
                          #'static폴더이름' 직접 디렉토리도 만들어줘야함 폴더 안에 img,css,js 등이 있음
    os.path.join(BASE_DIR,'myapp','static'),  #이렇게도 가능 경로,경로,경로

]


#static 파일들을 모두 모아서 배포함 한곳에다 모으는 작업을 해야함. 모으는 경로
STATIC_ROOT = os.path.join('staticfiles')
#python manage.py collectstatic 명령

MEDIA_ROOT = os.path.join(BASE_DIR,'media') # 사용자가 업로드한 파일을 'media'에 저장

MEDIA_URL = '/media/' #사용자의 의해 사진이 업로드되면 접근할수 있는 url 경로




# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
