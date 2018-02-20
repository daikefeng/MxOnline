import re

from django import forms

from operation.models import UserAsk


class UserAskForm(forms.ModelForm):
    class Meta:
        #继承UserAsk
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        #验证手机号码是否合法
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,4-9])|(17[6]))\\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError('手机号码非法', code='mobile_invalid')


