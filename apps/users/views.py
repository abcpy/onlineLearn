#-*-coding=utf-8-*-
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
from users.models import UserProfile,EmailVerifyRecord
from django.db.models import Q
from django.views.generic.base import View
from users.forms import LoginForm,RegisterForm,ForgetPwdForm,ModifyForm
from django.contrib.auth.hashers import make_password
from utils.email_send import send_register



class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user=UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

# # Create your views here.
# def user_login(request):
#     if request.method=='POST':
#         user_name=request.POST.get('username')
#         pass_word=request.POST.get('password')
#         user=authenticate(username=user_name,password=pass_word)
#         if user is not None:
#             login(request,user) #登录成功
#             return render(request,'index.html')
#         else:
#             return render(request,'login.html',{})
#     elif request.method=='GET':
#         return render(request,'login.html',{})

class LoginView(View):
    """登录页面"""
    def get(self,request):
        return render(request,'login.html',{})
    def post(self,request):
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            user_name=request.POST.get('username')
            pass_word=request.POST.get('password')
            user=authenticate(username=user_name,password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return render(request,'index.html')
                else:
                    return render(request, 'login.html', {'msg': '用户未被激活'})

            else:
                return render(request,'login.html',{'msg':'用户名或密码错误'})
        else:
            return render(request,'login.html',{'msg':'用户名或密码错误','login_form':login_form})


class RegisterView(View):
    """注册"""
    def get(self,request):
        register_form=RegisterForm()
        return render(request,'register.html',{'register_form':register_form})

    def post(self,request):
        register_form=RegisterForm(request.POST)
        if register_form.is_valid():
            user_name=request.POST.get('email')
            if UserProfile.objects.filter(email=user_name):
                return render(request,'register.html',{'msg':'用户已存在'})
            pass_word=request.POST.get('password')
            user_profile=UserProfile()
            user_profile.username=user_name
            user_profile.email=user_name
            user_profile.is_active=False
            user_profile.password=make_password(pass_word)
            user_profile.save()
            send_register(user_name,'register') #发送邮件激活用户
            return render(request,'login.html')
        else:
            return render(request,'register.html',{'register_form':register_form})

class ActiveUserView(View):
    """激活邮箱"""
    def get(self,request,active_code):
        all_recodes=EmailVerifyRecord.objects.filter(code=active_code)
        if all_recodes:
            for recode in all_recodes:
                email=recode.email
                user=UserProfile.objects.get(email=email)
                user.is_active=True
                user.save()
        else:
            return render(request,'active_fail.html')
        return render(request,'login.html')

class ForgetpwdView(View):
    def get(self,request):
        forget_pwd_form=ForgetPwdForm()
        return render(request,'forgetpwd.html',{'forget_pwd_form':forget_pwd_form})

    def post(self,request):
        forget_pwd_form=ForgetPwdForm(request.POST)
        if forget_pwd_form.is_valid():
            email=request.POST.get('email')
            send_register(email,'forget')
            return render(request,'success.html')

        else:
            return render(request,'forgetpwd.html',{'forget_pwd_form':forget_pwd_form})

class PasswordResetView(View):
    def get(self,request,reset_code):
        all_records=EmailVerifyRecord.objects.filter(code=reset_code)
        if all_records:
            for record in all_records:
                email=record.email
                return render(request,'password_reset.html',{'email':email})

        else:
           return render(request,'active_fail.html')

class ModifyPasswordView(View):
    def post(self,request):
        modify_form=ModifyForm(request.POST)
        if modify_form.is_valid():
            pwd1=request.POST.get('password')
            pwd2=request.POST.get('password2')
            email=request.POST.get('email')
            if pwd1!=pwd2:
                return render(request,'password_reset.html',{'email':email,'msg':'密码不一致'})
            user=UserProfile.objects.get(email=email)
            user.password=make_password(pwd2)
            user.save()
            return render(request,'login.html')
        else:
            email=request.POST.get('email')
            return render(request, 'password_reset.html', {'email': email, 'modify_form': modify_form})

