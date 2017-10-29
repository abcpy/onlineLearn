#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    nick_name=models.CharField(max_length=50,verbose_name=u'昵称',default='')
    birthday=models.DateField(verbose_name=u'生日',null=True,blank=True)
    gender=models.CharField(choices=(("male",u"男"),("female",u"女")),default='male',max_length=10)
    address=models.CharField(max_length=100,default=u'')
    mobile=models.CharField(max_length=11,null=True,blank=True)
    image=models.ImageField(upload_to="image/%Y/%m",default=u'image/default.png',max_length=100)

    class Meta:
        verbose_name='用户信息'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    """邮箱验证码"""
    code=models.CharField(max_length=20,verbose_name=u'验证码')
    email=models.EmailField(max_length=50,verbose_name=u'邮箱')
    send_type=models.CharField(choices=(('register',u'注册'),('forget',u'未注册')),max_length=20)
    send_time=models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name=u'邮箱验证码'
        verbose_name_plural=verbose_name

class Banner(models.Model):
    title=models.CharField(max_length=100,verbose_name=u'标题')
    image=models.ImageField(upload_to='banner/%Y/%m',verbose_name=u'轮播图')
    url=models.URLField(max_length=200,verbose_name=u'访问地址')
    index=models.IntegerField(default=100,verbose_name=u'顺序')
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name=u'轮播图'
        verbose_name_plural=verbose_name



