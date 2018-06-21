"""self_develop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from mainsite import views
urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^student/$',views.student),
    url(r'^accounts/logout/$',views.logout),
    url('admin/', admin.site.urls),
    url(r'^student/course_plan/$',views.course_plan),
    url(r'^student/personal_info/$',views.person_info),
    url(r'^student/course/$',views.course),
    url(r'^student/suggest_course/$',views.suggest_course),
    url(r'^accounts/register/$',views.register),
    url(r'^accounts/identify/$',views.identify),
]
