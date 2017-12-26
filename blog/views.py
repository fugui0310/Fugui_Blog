

from django.shortcuts import render, HttpResponse, redirect
from django.db import transaction
from blog.forms import *
from django.db.models import Count
# from blog import forms
from django.db.models import F

from django.contrib import auth
import json
# Create your views here.



def login(request):
    # if request.is_ajax():

    if request.is_ajax():

        username = request.POST.get("username")
        password = request.POST.get("password")
        validCode = request.POST.get("validCode")

        login_response = {"is_login": False, "error_msg": None}
        if validCode.upper() == request.session.get("keepValidCode").upper():
            user = auth.authenticate(username=username, password=password)
            if user:
                login_response["is_login"] = True
                auth.login(request, user)  # session   request.session[is_login]=True

            else:
                login_response["error_msg"] = "username or password error"

        else:
            login_response["error_msg"] = 'validCode error'

        import json

        return HttpResponse(json.dumps(login_response))

    return render(request, "login.html")


def get_validCode_img(request):

    from io import BytesIO
    import random

    from PIL import Image, ImageDraw, ImageFont
    img = Image.new(mode="RGB", size=(120, 30),
                    color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    draw = ImageDraw.Draw(img, "RGB")
    font = ImageFont.truetype("blog/static/font/kumo.ttf", 20)

    for i in range(40):  # 写噪点点
        draw.point([random.randint(0, 120), random.randint(0, 30)], fill=random_color)

        # 写干扰圆圈
    for i in range(20):
        draw.point([random.randint(0, 120), random.randint(0, 30)], fill=random_color)
        x = random.randint(0, 120)
        y = random.randint(0, 30)
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=random_color)

    for i in range(5):  # 画噪点线
        x1 = random.randint(0, 120)
        y1 = random.randint(0, 30)
        x2 = random.randint(0, 120)
        y2 = random.randint(0, 30)
        draw.line((x1, y1, x2, y2), fill=random_color)

    valid_list = []
    for i in range(5):
        random_num = str(random.randint(0, 9))
        random_lower_zimu = chr(random.randint(65, 90))
        random_upper_zimu = chr(random.randint(97, 122))

        random_char = random.choice([random_num, random_lower_zimu, random_upper_zimu])
        draw.text([5 + i * 24, 7], random_char,
                  (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), font=font)
        valid_list.append(random_char)

    f = BytesIO()
    img.save(f, "png")
    data = f.getvalue()

    valid_str = "".join(valid_list)
    print(valid_str)

    request.session["keepValidCode"] = valid_str

    return HttpResponse(data)


def register(request):
    if request.is_ajax():
        form_obj = forms.RegForm(request, request.POST)

        regResponse = {"user": None, "errorsList": None}
        if form_obj.is_valid():
            username = form_obj.cleaned_data["username"]
            password = form_obj.cleaned_data["password"]
            email = form_obj.cleaned_data.get("email")
            avatar_img = request.FILES.get("avatar_img")

            user_obj = models.UserInfo.objects.create_user(username=username, password=password, email=email,
                                                           avatar=avatar_img, nickname=username)
            regResponse["user"] = user_obj.username

        else:
            regResponse["errorsList"] = form_obj.errors
        import json
        return HttpResponse(json.dumps(regResponse))

    form_obj = forms.RegForm(request)
    return render(request, "register.html", {"form_obj": form_obj})


def log_out(request):
    auth.logout(request)

    return redirect("/login/")


def index(request, *args, **kwargs):
    if kwargs:
        data_list = models.Article.objects.filter(SiteArticlecategory__name=kwargs.get("sitearticlecategory"))
    else:
        data_list = models.Article.objects.all()
    site_list = models.SiteCategory.objects.all()
    return render(request, "index.html", locals())


def homeSite(request, username,**kwargs):
    # 查询当前用户

    current_user = models.UserInfo.objects.filter(username=username).first()
    current_blog = models.Blog.objects.filter(user__username=username).all()
    if not current_user:
        return render(request, 'notFound.html')

    # 查询当前用户所有文章
    img = models.UserInfo.objects.filter(username=username).all()
    data_list = models.Article.objects.filter(user__username=username).all()

    # 查询 当前用户的分类归档
    category_list=models.Category.objects.filter(blog=current_blog).annotate(count=Count("article__nid")).values_list('title','count')

    # 查询当前用户的标签归档

    tag_list=models.Tag.objects.filter(blog=current_blog).annotate(count=Count("article__nid")).values_list('title','count')

    # 查询当前用户的日期归档
    date_list=models.Article.objects.filter(user=current_user).extra(select={"filter_create_date":"strftime('%%Y/%%m',create_time)"}).values_list("filter_create_date").annotate(Count("nid"))

    #跳转
    if kwargs:
        if kwargs.get("condition")=="tag":
            data_list = models.Article.objects.filter(user=current_user,tags__title=kwargs.get("para"))
        elif kwargs.get("condition")=="category":
            data_list= models.Article.objects.filter(user=current_user,category__title=kwargs.get("para"))
        elif kwargs.get("condition")=="date":
            year, month = kwargs.get("para").split("/")
            data_list = models.Article.objects.filter(user=current_user,create_time__year=year,create_time__month=month)

    return render(request, "homeSite.html", locals())

def article(request, username, article_id,**kwargs):
    # 查询当前用户

    current_user = models.UserInfo.objects.filter(username=username).first()
    current_blog = models.Blog.objects.filter(user__username=username).all()
    if not current_user:
        return render(request, 'notFound.html')

    # 查询当前用户所有文章
    img = models.UserInfo.objects.filter(username=username).all()
    data_list = models.Article.objects.filter(user__username=username).all()

    # 查询 当前用户的分类归档
    category_list=models.Category.objects.filter(blog=current_blog).annotate(count=Count("article__nid")).values_list('title','count')

    # 查询当前用户的标签归档

    tag_list=models.Tag.objects.filter(blog=current_blog).annotate(count=Count("article__nid")).values_list('title','count')

    # 查询当前用户的日期归档
    date_list=models.Article.objects.filter(user=current_user).extra(select={"filter_create_date":"strftime('%%Y/%%m',create_time)"}).values_list("filter_create_date").annotate(Count("nid"))


    #跳转
    if kwargs:
        if kwargs.get("condition")=="tag":
            data_list = models.Article.objects.filter(user=current_user,tags__title=kwargs.get("para"))
        elif kwargs.get("condition")=="category":
            data_list= models.Article.objects.filter(user=current_user,category__title=kwargs.get("para"))
        elif kwargs.get("condition")=="date":
            year, month = kwargs.get("para").split("/")
            data_list = models.Article.objects.filter(user=current_user,create_time__year=year,create_time__month=month)
    # user_id = request.user.nid
    article_obj = models.Article.objects.filter(nid=article_id).first()
    articleComment = models.Comment.objects.filter(article_id=article_id).all()

    obj = render(request, "article_detail.html", locals())
    obj.set_cookie("next_path", request.path)
    obj.set_cookie("user_username", request.user.username)
    return obj

def poll(request):

    from django.db.models import F
    user_id=request.user.nid
    article_id=request.POST.get("article_id")

    pollResponse={"state":True,"is_repeat":None}
    if models.ArticleUp.objects.filter(user_id=user_id, article_id=article_id):
        pollResponse["state"]=False
        pollResponse["is_repeat"]=True

    else:
        try:
            articleUp = models.ArticleUp.objects.create(user_id=user_id, article_id=article_id)
            models.Article.objects.filter(nid=article_id).update(up_count=F("up_count") + 1)
        except:
            pollResponse["state"] = False

    import json
    return HttpResponse(json.dumps(pollResponse))


def down(request):

    user_id=request.user.nid
    article_id=request.POST.get("article_id")

    pollResponse={"state":True,"is_repeat":None}
    if models.ArticleUp.objects.filter(user_id=user_id, article_id=article_id):
        pollResponse["state"]=False
        pollResponse["is_repeat"]=True

    else:
        try:
            transaction.Atomic()
            articleUp = models.ArticleUp.objects.create(user_id=user_id, article_id=article_id)
            models.Article.objects.filter(nid=article_id).update(down_count=F("down_count") + 1)
        except:
            pollResponse["state"] = False

    import json
    return HttpResponse(json.dumps(pollResponse))

def comment(request):
    comment_text=request.POST.get('comment_text')
    user_id = request.user.nid
    article_id = request.POST.get("article_id")
    article_obj = models.Article.objects.filter(nid=article_id).first()
    import datetime
    comment_list={'state':False,}

    # print(request.POST.get("parent_comment_id"), )
    if request.user.username:
        if request.POST.get("parent_comment_id"):
            with transaction.atomic():
                pid = request.POST.get("parent_comment_id")
                comment_obj = models.Comment.objects.create(article_id=article_id, user_id=user_id,create_time=datetime.datetime.now(),
                                                            content=comment_text, parent_comment_id=pid)
        else:
            with transaction.atomic():

                comment_obj = models.Comment.objects.create(article_id=article_id, user_id=user_id,create_time=datetime.datetime.now(),
                                                            content=comment_text)
                models.Article.objects.filter(nid=article_id).update(comment_count=F("comment_count") + 1)
        comment_list['state'] = True

    else:
        return redirect('/login/')
    return HttpResponse(json.dumps(comment_list))
def commentTree(request,article_id):
    comment_list = models.Comment.objects.filter(article_id=article_id).values("nid","content","parent_comment_id")
    for comment in comment_list:
        comment["chidren_commentList"] = []
    comment_tree = []
    for comment in comment_list:
        if comment["parent_comment_id"]:
            pid = comment["parent_comment_id"]
            # print(comment)
            for i in comment_list:
                if i["nid"] == pid:
                    i["chidren_commentList"].append(comment)
        else:
            comment_tree.append(comment)
    print(comment_tree)
    return HttpResponse("OK")



def backendIndex(request):
    if not request.user.is_authenticated():
        return redirect("/login/")
    article_list = models.Article.objects.filter(user=request.user).all()
    site_list = models.SiteArticlecategory.objects.filter(article__user=request.user).all()
    return render(request, "backend_index.html", {"article_list": article_list,"site_list":site_list})



import datetime
def add_article(request):

    if request.method=="POST":
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            title=article_form.cleaned_data.get("title")
            content=article_form.cleaned_data.get("content")
            print(">>>>>>>>>>",content)
            article_obj=models.Article.objects.create(title=title,desc=content[0:150],create_time=datetime.datetime.now(),user=request.user)
            models.ArticleDetail.objects.create(content=content,article=article_obj)

        return HttpResponse("添加成功")

    article_form=ArticleForm()
    site_list = models.SiteArticlecategory.objects.filter(article__user=request.user).all()

    return render(request,"add_article.html",{"article_form":article_form,"site_list":site_list})



def uploadFile(request):
    print("POST",request.POST)
    print("FILES",request.FILES)
    file_obj=request.FILES.get("imgFile")
    file_name=file_obj.name
    print(file_name)

    from fugui_blog import settings
    import os
    path=os.path.join(settings.MEDIA_ROOT,"article_uploads",file_name)
    with open(path,"wb") as f:
        for i in file_obj.chunks():
            f.write(i)
    response={
        "error":0,
        "url":"/media/article_uploads/"+file_name+"/"
    }
    return HttpResponse(json.dumps(response))