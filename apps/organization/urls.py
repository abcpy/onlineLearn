#-*-coding: utf-8 -*-
__data__ = '17-11-6 下午5:40'
from django.conf.urls import url
from  .views import OrganizationView,UserAskView,OrgDetailHomeView,OrgCourseView,OrgIntroduceView,OrgTeacherView,UserFavoriteView

urlpatterns=[
    url(r'^list/$', OrganizationView.as_view(), name='org_list'),
    url(r'^add_ask/$',UserAskView.as_view(),name='add_ask'),
    url(r'^org_detail_homepage/(?P<org_id>\d+)/$',OrgDetailHomeView.as_view(),name='detail_homepage'),
    url(r'^org_course/(?P<org_id>\d+)/$',OrgCourseView.as_view(),name='org_course'),
    url(r'^org_introduce/(?P<org_id>\d+)/$',OrgIntroduceView.as_view(),name='org_introduce'),
    url(r'^org_teacher/(?P<org_id>\d+)/$',OrgTeacherView.as_view(),name='org_teacher'),
    url(r'^add_fav/$',UserFavoriteView.as_view(),name='user_fav'),

]