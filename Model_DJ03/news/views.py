from django.shortcuts import render, get_object_or_404
from .models import News_post

# Create your views here.
def news(request):
    posts = News_post.objects.all()
    return render(request, 'news/news.html', {'posts' : posts})

def news_detail(request, post_id):
    post = get_object_or_404(News_post, id=post_id)
    return render(request, 'news/news_detail.html', {'post': post})