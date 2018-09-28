from django.shortcuts import render
from django.http import  HttpResponse
from myblog.models import Blog,Tag,Category
from pure_pagination import PageNotAnInteger, Paginator
from django import  forms
from myblog.models import  Comment
from django.shortcuts import render_to_response,render
from django import  forms
from django.views.decorators.csrf import csrf_exempt

from myblog.models import User
from django.http import HttpResponseRedirect,HttpResponse
def get(request):
    all_blog=Blog.objects.all().order_by('-id')
    category=Category.objects.all().order_by('-id')
    all_comment=Comment.objects.all().order_by('-id')
    username = request.COOKIES.get('cookie_username', '')
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(all_blog, 5, request=request)
    all_blog = p.page(page)
    return render(request,'index.html',{'all_blog':all_blog,'category':category,'all_comment':all_comment,'username':username})
def re_group(request):
    all_blog=Blog.objects.all().order_by('-create_time')
    length=Blog.objects.all().count()
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(all_blog, 5, request=request)
    all_blog = p.page(page)
    return render(request,'regroup.html',{'all_blog':all_blog,'length':length})
def tag(request):
    all_tag=Tag.objects.all().order_by('name').iterator()
    for tag_name in all_tag:
        tag_f=Tag.objects.filter(name=tag_name).first()
    tag_blogs=tag_f.blog_set.all()
    # 分页
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(tag_blogs, 5, request=request)
    tag_blogs = p.page(page)
    return render(request,'tag.html',{'all_tag':all_tag,'tag_blogs':tag_blogs,'tag_name':tag_name})
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name','comment','blog']
def comment_re(request):
    comment_from=CommentForm(request.POST)
    if comment_from.is_valid():
        comment_from.save()
        return HttpResponse('{"status": "success"}', content_type='application/json')
    else:
        return HttpResponse('{"status": "fail"}', content_type='application/json')
#my database forms
class UserForm(forms.Form):
    username=forms.CharField(label='用户名',max_length=20)
    password=forms.CharField(label='密_码',max_length=20)
@csrf_exempt
def register(request):
    Method=request.method
    if Method=='POST':
        usermess=UserForm(request.POST)
        print(usermess)
        print(usermess.is_valid())
        if usermess.is_valid():
            username=usermess.cleaned_data['username']
            password=usermess.cleaned_data['password']
            print(password)
            try:
                reg=User.objects.filter(username=username).get().username
                print(reg)
                return render(request,'register.html',{'reg':reg})
            except:
                regadd=User.objects.create(username=username,passwprd=password)
                print(regadd)
                return render(request,'register.html',{'regadd':regadd})
    else:
        usermess=UserForm()
    return render(request,'register.html',{'usermess':usermess,'Method':Method})
@csrf_exempt
def login(request):
    Method=request.method
    if Method=='POST':
        usermess=UserForm(request.POST)
        print(usermess)
        print(usermess.is_valid())
        if usermess.is_valid():
            username=usermess.cleaned_data['username']
            password=usermess.cleaned_data['password']
            print(password)
            userPassJude=User.objects.filter(username__exact=username,passwprd__exact=password)
            print(userPassJude)
            if userPassJude:
                response=HttpResponseRedirect('/index')
                response.set_cookie('cookie_username',username,8000)
                return response
            else:
                return render(request,'login.html')
    else:
        usermess=UserForm()
    return render(request,'login.html',{'usermess':usermess})
def index(request):
    username=request.COOKIES.get('cookie_username','')
    return render(request,'index.html',{'username':username})
def logout(request):
    response=HttpResponse('logout<br><a href="http://127.0.0.1/8000/register">register</a>')
    #Sresponse.delete_cookie('cookies_username')
    return response