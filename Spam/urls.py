"""
URL configuration for SMD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path
from .import views 

# the use of django.contib------
# This imports Django's built-in admin module.
# The Django admin panel allows superusers to manage models (like adding, editing, or deleting records) through a web-based interface.
# Typically, the admin site is enabled in a project by including admin.site.urls in the urlpatterns.

# the use of django.urls----------------
# This imports the path function from django.urls, which is used to define URL patterns in Django.
# path() is used to map URLs to specific views in your Django application.

# the use of .import views-----------
# This imports the views.py file from the same directory (indicated by .).
# It allows you to reference view functions in your urls.py file.

# admin: Enables Django’s admin panel.
# path: Defines URL routes for views.
# views: Connects views.py functions to the URLs.



urlpatterns = [
    path('', views.index, name="Index"),
    path('check', views.checkSpam, name="CheckSpam"),

]

