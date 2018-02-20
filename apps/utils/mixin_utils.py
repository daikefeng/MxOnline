# _*_ coding:utf-8 _*_
__author__ = 'Bruse'
__date__ = '2017-01-24 13:32'

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


#自定义一个class来设置用户的登录权限，把这个类引入到需要登录才能进入的类视图中
class LoginRequiredMixin(object):
    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
