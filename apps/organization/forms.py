#-*-coding: utf-8 -*-
__data__ = '17-11-6 下午6:18'

from operation.models import UserAsk
from django import forms
import re

class UserAskForm(forms.ModelForm):
    class Meta:
        model=UserAsk
        fields=['name','mobile','course_name']

    def clean_mobile(self):
        mobile=self.cleaned_data['mobile']
        REGEX_MOBILE="^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        pattern=re.compile(REGEX_MOBILE)
        if pattern.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u'手机号码非法',code='mobile_invalid')

