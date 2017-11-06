#-*-coding=utf-8-*-
from django.shortcuts import render
from django.views.generic.base import View
from organization.models import CityDict,CourseOrg
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

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
