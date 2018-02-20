from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.static import serve

import xadmin

from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView, LogoutView, IndexView
#解决无法直接import settings的问题
from django.conf import settings


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url('^$', IndexView.as_view(), name='index'),
    url('^login/$', LoginView.as_view(), name='login'),
    url('^logout/$', LogoutView.as_view(), name='logout'),
    url('^register/$', RegisterView.as_view(), name='register'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),
    url(r'^forget/$', ForgetPwdView.as_view(), name='forget_pwd'),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name='reset_pwd'),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),
    #课程机构URL配置
    url(r'^org/', include('organization.urls', namespace='org')),
    #课程相关url配置
    url(r'^course/', include('courses.urls', namespace='course')),
    #配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # #配置非生产环境下的static目录下的文件
    # url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    #课程相关url配置
    url(r'^user/', include('users.urls', namespace='users')),
    #Ueditor插件
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
]

#全局404页面
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'
