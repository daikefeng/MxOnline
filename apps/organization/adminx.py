import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    ist_filter = ['name', 'desc', 'add_time']

xadmin.site.register(CityDict, CityDictAdmin)


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_num', 'fav_nums', 'add_time']
    search_fields = ['name', 'desc', 'click_num', 'fav_nums']
    ist_filter = ['name', 'desc', 'click_num', 'fav_nums', 'add_time']
    relfield_style = 'fk-ajax'

xadmin.site.register(CourseOrg, CourseOrgAdmin)


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_position', 'work_company', 'points', 'click_num', 'fav_nums', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_position', 'work_company', 'points', 'click_num', 'fav_nums']
    ist_filter = ['org', 'name', 'work_years', 'work_position', 'work_company', 'points', 'click_num', 'fav_nums', 'add_time']

xadmin.site.register(Teacher, TeacherAdmin)
