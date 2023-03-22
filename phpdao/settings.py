"""
Django settings for phpdao project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5s5=8p)268&1)ch-66(et=lkd0w4h^^nkikdyb=t5rf+@ux*49'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['13.112.123.94']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'phpdao1.apps.Phpdao1Config',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'utils.md.AuthMiddleware',
]

ROOT_URLCONF = 'phpdao.urls'

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

WSGI_APPLICATION = 'phpdao.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'phpdao',  # 数据库名字，要和app的名字一致
        'USER': 'root',
        'PASSWORD': 'clarck71983',
        # 'HOST': 'phpdao.cbu5q7jha9cg.ap-northeast-1.rds.amazonaws.com',
        'HOST': '127.0.0.1',
        'PORT': 3306
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -------------新增--------------#
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "/media/"

####菜单###
UNICOM_MENU = {
    # 1 super admin
    'superadmin': [
        # {'text': 'Home', 'url': '/home/'},
        {'text': 'Dashboard', 'url': '/dashboard/'},
        {'text': 'HID', 'url': '/hid_list/'},
        {'text': 'Upload', 'url': '/upload/'},
        {'text': 'Asset', 'url': '/asset/'},
        {'text': 'Profile', 'url': '/profile/'},
        {'text': 'Message', 'url': '/message/'},
        {'text': 'DataSearch', 'url': '/datasearch/'},
        {'text': 'Audit', 'url': '/audit/'},
        {'text': 'Manage', 'url': '/manage/'},
        {'text': 'Locationsearch', 'url': '/locationsearch/'},
        {'text': 'ChatGPT', 'url': '/chatgpt/'},

    ],

    # 2 admin
    'admin': [
        # {'text': 'Home', 'url': '/home/'},
        {'text': 'Dashboard', 'url': '/dashboard/'},
        {'text': 'HID', 'url': '/hid_list/'},
        {'text': 'Upload', 'url': '/upload/'},
        {'text': 'Asset', 'url': '/asset/'},
        {'text': 'Message', 'url': '/message/'},
        {'text': 'DataSearch', 'url': '/datasearch/'},
        {'text': 'Audit', 'url': '/audit/'},
        {'text': 'Manage', 'url': '/manage/'},
        {'text': 'ChatGPT', 'url': '/chatgpt/'},
    ],

    # 3 contributor admin
    'contributor': [
        {'text': 'Dashboard', 'url': '/dashboard/'},
        {'text': 'HID', 'url': '/hid_list/'},
        {'text': 'Upload', 'url': '/upload/'},
        {'text': 'Asset', 'url': '/asset/'},
        {'text': 'Message', 'url': '/message/'},
        {'text': 'Audit', 'url': '/audit/record_audit/'},
    ],

    # 4 user
    'user': [
        # {'text': 'Home', 'url': '/home/'},
        {'text': 'Dashboard', 'url': '/dashboard/'},
        {'text': 'HID', 'url': '/hid_list/'},
        {'text': 'Upload', 'url': '/upload/'},
        {'text': 'Asset', 'url': '/asset/'},
        {'text': 'Message', 'url': '/message/'},
    ],

    # 5 partner
    'partner': [
        {'text': 'Dashboard', 'url': '/dashboard/'},
        {'text': 'Profile', 'url': '/profile/'},
        {'text': 'Message', 'url': '/message/'},
        {'text': 'DataSearch', 'url': '/datasearch/'},
    ],

}

# 如果访问页面弹出无权访问，请检查urls,unicom_menu以及unicom_permission里的大小写
UNICOM_PERMISSION = {
    # 1 superadmin
    'superadmin': {'home', 'dashboard', 'asset', 'upload', 'profile', 'message', 'datasearch', 'audit',
                   'manage', 'account_list', 'account_add', 'account_edit', 'account_delete', 'account_suspend',
                   'account_active', 'hid_list', 'hid_add', 'hid_edit', 'hid_delete', 'hid_suspend', 'hid_active',
                   'drugdict_list', 'drugdict_add', 'drugdict_edit', 'drugdict_delete',
                   'manuf_list', 'manuf_add', 'manuf_edit', 'manuf_delete',
                   'vaccinedict_list', 'vaccinedict_add', 'vaccinedict_edit', 'vaccinedict_delete',
                   'diseasedict_list', 'diseasedict_add', 'diseasedict_edit', 'diseasedict_delete',
                   'locationdict_list', 'locationdict_add', 'locationdict_edit', 'locationdict_delete',
                   'locationsearch', 'check', 'audit', 'audit_rejected', 'audit_approved', 'asset', 'message',
                   'message_add', 'profile', 'signup',
                   'change_password', 'editlocation', 'diseasesearch', 'chatgpt',

                   },

    # 2 admin
    'admin': {'home', 'asset', 'upload', 'profile', 'message', 'dataSearch', 'audit',
              'manage', 'account_list', 'account_add', 'account_edit', 'account_delete', 'account_suspend',
              'account_active', 'hid_list', 'hid_add', 'hid_edit', 'hid_delete', 'hid_suspend', 'hid_active',
              'drugdict_list', 'drugdict_add', 'drugdict_edit', 'drugdict_delete',
              'manuf_list', 'manuf_add', 'manuf_edit', 'manuf_delete',
              'vaccinedict_list', 'vaccinedict_add', 'vaccinedict_edit', 'vaccinedict_delete',
              'diseasedict_list', 'diseasedict_add', 'diseasedict_edit', 'diseasedict_delete',
              'locationdict_list', 'locationdict_add', 'locationdict_edit', 'locationdict_delete', 'locationsearch',
              'check', 'audit', 'audit_rejected', 'audit_approved', 'asset', 'message', 'message_add', 'profile', 'signup',
              'change_password', 'editlocation', 'diseasesearch', 'chatgpt',

              },

    # 3 contributor admin
    'contributor admin': {'home', 'Asset', 'Upload', 'Profile', 'Message', 'hid_add', 'hid_edit'},

    # 4 user
    'user': {'home', 'dashboard', 'asset', 'upload', 'profile', 'message', 'hid_list', 'hid_add', 'hid_edit',
             'upload_list', 'profile', },

    # 5 partner
    'partner': {'home', 'Asset', 'Upload', 'Profile', 'Message'},

}
