from django.contrib import admin

# Register your models here.
from myblog.models import Blog,Tag,Category,Comment,User
#筛选器
class BlogAdmin(admin.ModelAdmin):
    list_display=['title','content','create_time','flash_time','click_nums']
    list_filter = ['tag']#过滤器,一般是多对多关系
    search_fields = ['title']#搜索框,一般是文本等文件
    #date_hierarchy = ['create_time']


class  CommentAdmin(admin.ModelAdmin):
    list_display=['name','comment','create_time']
    list_editable = ['comment']
class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(Blog,BlogAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment,CommentAdmin)
admin.site.register(User,UserAdmin)