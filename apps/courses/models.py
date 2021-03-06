#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from organization.models import CourseOrg

# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=50,verbose_name=u'课程名')
    desc=models.CharField(max_length=300,verbose_name=u'课程描述')
    org=models.ForeignKey(CourseOrg,verbose_name=u'课程机构',null=True,blank=True)
    detail=models.TextField(verbose_name=u'课程详情')
    degree=models.CharField(choices=(('cj',u'初级'),('zj',u'中级'),('gj',u'高级')),max_length=3,verbose_name='课程等级')
    learn_times=models.IntegerField(default=0,verbose_name=u'学习时长（分钟）')
    students=models.IntegerField(default=0,verbose_name=u'学习人数')
    fav_nums=models.IntegerField(default=0,verbose_name=u'收藏人数')
    image=models.ImageField(upload_to='courses/%Y/%m',verbose_name=u'封面图片')
    chick_nums=models.IntegerField(default=0,verbose_name=u'点击数')
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name=u'课程'
        verbose_name_plural=verbose_name

class Lesson(models.Model):
    course=models.ForeignKey(Course,verbose_name=u'课程')
    name=models.CharField(max_length=100,verbose_name=u'章节名称')
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name=u'章节'
        verbose_name_plural=verbose_name

class video(models.Model):
    lesson=models.ForeignKey(Lesson,verbose_name=u'章节')
    name=models.CharField(max_length=100,verbose_name=u'视频名称')
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name=u'视频'
        verbose_name_plural=verbose_name


class CourseResource(models.Model):
    course=models.ForeignKey(Course,verbose_name=u'课程')
    name=models.CharField(max_length=100,verbose_name=u'资源名称')
    download=models.FileField(upload_to='course/resource/%Y/%m',verbose_name=u'下载地址')
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name=u'课程资源'
        verbose_name_plural=verbose_name

