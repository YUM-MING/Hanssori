import os
from pathlib import Path

# ======================================
# ✅ 기본 경로 설정
# ======================================
BASE_DIR = Path(__file__).resolve().parent.parent

# ======================================
# ✅ 보안
# ======================================
SECRET_KEY = 'django-insecure-개인-키-변경-필요'  # 🔐 실제 배포 시 반드시 변경
DEBUG = True
ALLOWED_HOSTS = []

# ======================================
# ✅ 설치된 앱들
# ======================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # 💬 내 앱들
    'gugak',     

]

# ======================================
# ✅ 미들웨어
# ======================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ======================================
# ✅ 루트 URL 설정
# ======================================
ROOT_URLCONF = 'hanssori.urls'

# ======================================
# ✅ 템플릿 설정
# ======================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),  # 전체 공용 템플릿 디렉토리
            os.path.join(BASE_DIR, 'gugak', 'templates'),  # 앱 전용 템플릿
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # 로그인 상태 확인용
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ======================================
# ✅ WSGI 애플리케이션
# ======================================
WSGI_APPLICATION = 'hanssori.wsgi.application'

# ======================================
# ✅ 데이터베이스 설정 (SQLite 기본)
# ======================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ======================================
# ✅ 비밀번호 유효성 검사
# ======================================
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

# ======================================
# ✅ 언어 및 시간대
# ======================================
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_TZ = True  # ✅ USE_L10N은 Django 4.x 이상에서 deprecated

# ======================================
# ✅ 정적 파일 (CSS, JS 등)
# =================================gugak=====
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'gugak', 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# ======================================
# ✅ 기본 기본키 필드 타입
# ======================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
