from django.conf.urls import url

from .views import CourseListView, CourseDetailView, CourseInfoView, CommentView, AddCommentsView, VideoPlayView

urlpatterns = [
    url(r'^list/$', CourseListView.as_view(), name='course_list'),
    #课程详情
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='course_detail'),
    #课程视频列表
    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name='course_info'),
    #课程评论
    url(r'^comment/(?P<course_id>\d+)/$', CommentView.as_view(), name='course_comment'),
    #添加课程评论,因为ajax把Course.id传过去了，这里不用添加
    url(r'^add_comment/$', AddCommentsView.as_view(), name='add_comment'),
    url(r'^video/(?P<video_id>\d+)/$', VideoPlayView.as_view(), name='video_play'),
]