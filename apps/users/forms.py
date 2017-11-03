#-*-coding: utf-8 -*-
__data__ = '17-11-1 下午11:07'


from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    """表单验证"""
    username=forms.CharField(required=True)
    password=forms.CharField(required=True,min_length=5)

class RegisterForm(forms.Form):
    """注册验证"""
    email=forms.EmailField(required=True)
    password=forms.CharField(required=True,min_length=5)
    captcha=CaptchaField(error_messages={"invalid":u"验证码错误"})

class ForgetPwdForm(forms.Form):
    """忘记密码验证"""
    email=forms.EmailField(required=True)
    captcha=CaptchaField(error_messages={"invalid":u"验证码错误"})

class ModifyForm(forms.Form):
    password=forms.CharField(required=True,min_length=5)
    password2=forms.CharField(required=True,min_length=5)



