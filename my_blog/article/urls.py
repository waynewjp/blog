from django.urls import  path
from . import views

# 正在部署的应用的名称
app_name='article'

urlpatterns=[
    # path函数将url映射到视图
    # 映射文章列表view
    path('article-list/', views.article_list, name='article_list'),
    # 映射文章内容viewl里的函数
    # 要多一个 / 不然就找不到了
    # path('article-detail/<int:id>',views.article_detail,name='article_detail'),
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),

    ]