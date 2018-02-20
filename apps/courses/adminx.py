import xadmin

from .models import Course, Lesson, Video, CourseResource, BannerCourse
from organization.models import CourseOrg


class LessonInline(object):
    model = Lesson
    extra = 0


class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'click_nums']
    search_files = ['name', 'desc', 'detail', 'degree', 'students']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students']
    ordering = ['-click_nums']
    inlines = [LessonInline, CourseResourceInline]

    def queryset(self):
        qs = super(CourseAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs

    def save_models(self):
        #这是获得一个新的课程对象
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()

xadmin.site.register(Course, CourseAdmin)


class BannerCourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'click_nums']
    search_files = ['name', 'desc', 'detail', 'degree', 'students']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students']
    ordering = ['-click_nums']
    inlines = [LessonInline, CourseResourceInline]

    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs

xadmin.site.register(BannerCourse, BannerCourseAdmin)


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_files = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']

xadmin.site.register(Lesson, LessonAdmin)


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_files = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']

xadmin.site.register(Video, VideoAdmin)


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_files = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']

xadmin.site.register(CourseResource, CourseResourceAdmin)




