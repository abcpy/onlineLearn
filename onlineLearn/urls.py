"""onlineLearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin
import xadmin
from django.views.generic import TemplateView
from users.views import LoginView,RegisterView,ActiveUserView,ForgetpwdView,PasswordResetView,ModifyPasswordView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url('^$',TemplateView.as_view(template_name='index.html'),name='index'),
    url(r'^login/$',LoginView.as_view(),name='login'),
    url(r'^register/$',RegisterView.as_view(),name='register'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$',ActiveUserView.as_view(),name='activeuser'),
    url(r'^forgetpwd/$',ForgetpwdView.as_view(),name='forgetpwd'),
    url(r'^reset/(?P<reset_code>.*)/$',PasswordResetView.as_view(),name='pwdreset'),
    url(r'^modifypwd/$',ModifyPasswordView.as_view(),name='modifypwd'),
    # url(r'^login/$',user_login,name='login'),
    # url('^login.html/$',TemplateView.as_view(template_name='login.html'),name='login')
]
