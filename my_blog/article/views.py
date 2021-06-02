from django.http import HttpResponse
from django.shortcuts import render
# from my_blog.article.models import ArticlePost

# 导入数据模型
from .models import ArticlePost

# Create your views here.
def article_list(request):
    # return HttpResponse("hello,world!")
    # 取出所有文章
    articles=ArticlePost.objects.all()
    # 需要传递给模板的对象
    context={'articles':articles}
    # render函数：载入模板，并返回context对象
    return render(request, 'article/list.html', context)

def article_detail(request,id):
    # 取出相应的文章
    article=ArticlePost.objects.get(id=id)
    # 需要传递给模板的对象
    context={'article':article}
    # 载入模板，并返回context对象
    return render(request,'article/detail.html',context)

