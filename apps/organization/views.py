#-*-coding=utf-8-*-
from django.shortcuts import render
from django.views.generic.base import View
from organization.models import CityDict,CourseOrg
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from forms import UserAskForm
from django.http import HttpResponse
from operation.models import UserFavorite

# Create your views here.
class OrganizationView(View):
    def get(self,request):
        all_org=CourseOrg.objects.all() #课程机构
        all_city=CityDict.objects.all() #城市信息

        hot_orgs=all_org.order_by('-chilc_nums')[:3]

        # 学习人数排序
        cate_sort=request.GET.get('sort','')
        if cate_sort:
            if cate_sort=='students':
                all_org=all_org.order_by('-studets')
            elif cate_sort=='courses':
                 # 课程数
                all_org=all_org.order_by('-course_num')

        #筛选城市
        city_id =request.GET.get('city','')
        if city_id:
            all_org=all_org.filter(city_id=int(city_id))

        #筛选课程机构
        cate=request.GET.get('ct','')
        if cate=='pxjg':
            all_org=all_org.filter(category=cate)
        elif cate=='gx':
            all_org=all_org.filter(category=cate)
        elif cate=='gr':
            all_org=all_org.filter(category=cate)


        """对课程机构进行分类"""
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_org, 2,request=request)
        orgs = p.page(page)

        org_num=all_org.count()#机构人数




        return render(request,'org-list.html',{
            'all_org':orgs,
            'all_city':all_city,
            'org_num':org_num,
            'city_id':city_id,
            'cate':cate,
            'hot_orgs':hot_orgs,
            'cate_sort':cate_sort,
        })


class UserAskView(View):
    def post(self,request):
        userask_form=UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask=userask_form.save(commit=True)#提交表单
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"发生错误"}', content_type='application/json')

class OrgDetailHomeView(View):
    """机构详情首页"""
    def get(self,request,org_id):
        currentpage='OrgDetailHomeView'
        course_org=CourseOrg.objects.get(id=int(org_id))
        all_courses=course_org.course_set.all()[:3]
        all_teachers=course_org.teacher_set.all()[:1]
        has_fav=False
        if request.user.is_authenticated():
             if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                 has_fav=True

        return render(request,'org-detail-homepage.html',{
            'all_courses':all_courses,
            'all_teachers':all_teachers,
            'course_org':course_org,
            'currentpage':currentpage,
            'has_fav':has_fav
        })


class OrgCourseView(View):
    """机构课程"""
    def get(self,request,org_id):
        currentpage = 'OrgCourseView'
        course_org=CourseOrg.objects.get(id=int(org_id))
        all_course=course_org.course_set.all()
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True

        return render(request,'org-detail-course.html',{
            'all_course':all_course,
            'course_org':course_org,
            'currentpage': currentpage,
            'has_fav':has_fav,

        })

class OrgIntroduceView(View):
    """机构介绍"""
    def get(self,request,org_id):
        course_org=CourseOrg.objects.get(id=int(org_id))
        currentpage = 'OrgIntroduceView'
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True

        return render(request,'org-detail-desc.html',{
            'course_org': course_org,
            'currentpage': currentpage,
            'has_fav':has_fav,
        })

class OrgTeacherView(View):
    """机构讲师"""
    def get(self,request,org_id):
        currentpage = 'OrgTeacherView'
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_teachers=course_org.teacher_set.all()
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True

        return render(request, 'org-detail-teachers.html', {
            'course_org': course_org,
            'all_teachers':all_teachers,
            'currentpage': currentpage,
            'has_fav':has_fav,
        })

class UserFavoriteView(View):
    def post(self,request):
        fav_id=request.POST.get('fav_id',0)
        fav_type=request.POST.get('fav_type',0)

        if not request.user.is_authenticated():
            return HttpResponse('{"status":"fail","msg":"用户未登录"}',content_type='application/json')

        exist_records=UserFavorite.objects.filter(user=request.user,fav_id=int(fav_id),fav_type=int(fav_type))
        if exist_records:
            exist_records.delete()
            return HttpResponse('{"status":"success","msg":"收藏"}', content_type='application/json')

        else:
            if int(fav_id)>0 and int(fav_type)>0:
                user_fav =UserFavorite()
                user_fav.user=request.user
                user_fav.fav_id=int(fav_id)
                user_fav.fav_type=int(fav_type)
                user_fav.save()
                return HttpResponse('{"status":"success","msg":"已收藏"}',content_type='application/json')
            else:
                return HttpResponse('{"status":"fail","msg":"收藏错误"}',content_type='application/json')




