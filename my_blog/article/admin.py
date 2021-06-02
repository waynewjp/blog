from django.contrib import admin

# 导入模型中的类
from .models import  ArticlePost
# Register your models here.

# 注册articlepost到admin中
admin.site.register(ArticlePost)