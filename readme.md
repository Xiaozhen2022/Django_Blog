---
title: "Blog"  
author: "Janet"  
date: "2024-02-12"  
output: html_document  
---
## Preview the blog page


## Build development environment
django-admin startproject blogProject
## Build project application
Build the app:
python manage.py startapp blog 
Add the app name in setting : 
``` INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog",
]  
```
```
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog",
]
```
Configure the setting database environment  
```
DATABASES = {  
    "default": {  
        "ENGINE":'django.db.backends.mysql',  
        "NAME": 'django',  
        "HOST": '127.0.0.1',  
        "PORT": 3306,  
        "USER": 'root
        ',  
        'PASSWORD': '********',  
    }  
}  
```
__init__.py
import pymysql
pymysql.install_as_MySQLdb()
## Create a data model
[Knowledge about ForeignKey、ManyToManyField ](https://docs.djangoproject.com/en/2.2/topics/db/models/#relationships)  
Create three table classes: Category, Tag, and Post
## Migration database
```
python manage.py migrate
python manage.py makemigrations blog
python manage.py migrate blog
```
## View of blog
Project root directory set up templates/blog/index. The HTML
Modify the setting
```
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...
    },
]
```
IN blogProject/views.py:
```
from django.shortcuts import render

def index(request):
    return render(request, 'blog/index.html', context={
    'title': '我的博客首页',
    'welcome': '欢迎访问我的博客首页'
    })

```
## Background management system to publish articles
Create administrative user
```
python manage.py createsuperuser
用户名 (leave blank to use 'yangxg'): admin
电子邮件地址: admin@example.com
Password:
Password (again):
Superuser created successfully.

```
127.0.0.1:8000/admin/
## Develop blog post details page
## Latest article template tags
## Sort archive and label pages
