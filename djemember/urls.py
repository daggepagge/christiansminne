"""djemember URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from memories import views

urlpatterns = [
#   url(r'^login/$', auth_views.login, {'template_name': 'templates/login.html'}, name='login'),
#   url(r'^logout/$', auth_views.logout, {'template_name': 'templates/logout.html'}, name='logout'),
    url(r'^minnen/', include('memories.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^texter/$', views.writings, name='list_of_writings'),
    url(r'^texter/(?P<writing_id>[0-9]+)/$', views.writing_detail, name='writing_detail'),
    url(r'^$', views.landingpage, name='landingpage'),
#   url(r'^accounts/', include('allauth.urls')),
]

# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]