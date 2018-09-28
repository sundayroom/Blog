from django.db import models
from django.utils import  timezone
# Create your models here.
class Category(models.Model):
    name=models.CharField(verbose_name='文章类别',max_length=20)
    class Meta:
        verbose_name='文章类别'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(verbose_name='文章标签',max_length=20)
    class Meta:
        verbose_name='文章标签'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name
class Blog(models.Model):
    title=models.CharField(verbose_name='文章标题',max_length=100)
    content=models.TextField(verbose_name='内容',default='')
    create_time=models.DateTimeField(verbose_name='创建时间',default=timezone.now())
    flash_time=models.DateTimeField(verbose_name='更新时间',auto_now=True)
    click_nums=models.IntegerField(verbose_name='点击率',default=0)
    category=models.ForeignKey(Category,verbose_name='文章类别',on_delete=models.CASCADE,)
    tag=models.ManyToManyField(Tag,verbose_name='文章标签')
    class Meta:
        verbose_name='我的文章'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.title
class Comment(models.Model):
    name=models.CharField(verbose_name='姓名',max_length=20,default='佚名')
    comment=models.TextField(verbose_name='评论',max_length=100)
    create_time=models.DateTimeField(verbose_name='创建时间',default=timezone.now())
    blog=models.ForeignKey(Blog,verbose_name='博客',on_delete=models.CASCADE,)
    class Meta:
        verbose_name='博客评论'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.comment[:10]

class User(models.Model):
    username=models.CharField(max_length=20)
    passwprd=models.CharField(max_length=20)
    def __str__(self):
        return self.username