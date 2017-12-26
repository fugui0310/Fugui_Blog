from django import forms

from django.forms import widgets,ValidationError


from blog import models

class RegForm(forms.Form):

    username=forms.CharField(max_length=12,min_length=5,required=True,error_messages={
        "required":"不能为空",
    },widget=widgets.TextInput(attrs={"class":"form-control","placeholder":"username"}))

    password=forms.CharField(min_length=6,widget=widgets.PasswordInput(
        attrs={"class": "form-control", "placeholder": "password"}
    ))

    repeat_pwd=forms.CharField(min_length=6,widget=widgets.PasswordInput(
        attrs={"class": "form-control", "placeholder": "repeat_pwd"}
    ))

    email=forms.EmailField(widget=widgets.EmailInput(
        attrs={"class": "form-control", "placeholder": "email"}
    ))


    def clean_username(self):

        ret=models.UserInfo.objects.filter(username=self.cleaned_data.get("username"))
        if not ret:
            return self.cleaned_data.get("username")
        else:
            raise ValidationError("用户名已注册")

    def clean_password(self):
        data=self.cleaned_data.get("password")

        if not data.isdigit():
            return self.cleaned_data.get("password")
        else:
            raise ValidationError("密码不能全是数字")


    def clean_validCode(self):
        if self.cleaned_data.get("validCode")== self.request.session.get("validCode"):
            return self.cleaned_data.get("validCode")

        else:
            raise  ValidationError("验证码错误")
    def clean(self):
        if self.cleaned_data.get("password") == self.cleaned_data.get("repeat_pwd"):
            return self.cleaned_data

        else:
            raise  ValidationError("两次密码不一致")

    def __init__(self,request,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.request=request



from blog.plugins import xss_plugin

class ArticleForm(forms.Form):

    title=forms.CharField(max_length=20,error_messages={
        "required":"不能为空",
    })

    content=forms.CharField(error_messages={
        "required":"不能为空",
    },widget=widgets.Textarea())

    def clean_content(self):

        html_str=self.cleaned_data.get("content")
        clean_content=xss_plugin.filter_xss(html_str)
        self.cleaned_data["content"]=clean_content

        return self.cleaned_data.get("content")





