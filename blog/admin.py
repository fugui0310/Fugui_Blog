from django.contrib import admin
from blog.models import *
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(ArticleDetail)
admin.site.register(Comment)
admin.site.register(CommentUp)
admin.site.register(ArticleUp)
admin.site.register(Tag)
admin.site.register(Article2Tag)
admin.site.register(SiteCategory)
admin.site.register(SiteArticlecategory)


