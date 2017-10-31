#-*-coding: utf-8 -*-
__data__ = '17-10-29 上午5:41'
import xadmin
from .models import EmailVerifyRecord,Banner
from xadmin import views

class BaseSetting(object):
    enable_themes=True  #主题设置
    use_bootswatch=True

class GlobalSetting(object):
    site_title='在线学习后台管理系统' #全局配置
    site_footer='在线学习网'
    menu_style='accordion' #收起菜单


class EmailVerifyRecordAdmin(object):
    list_display=['code','email','send_type','send_time'] #后台列表显示的列
    search_fields=['code','email','send_type']  #后台列表查询条件
    list_filter=['code','email','send_type','send_time'] #后台列表过滤的条件

class BannerAdmin(object):
    list_display=['title','image','url','index','add_time']
    search_fields=['title','image','url','index']
    list_filter=['title','image','url','index','add_time']



xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)