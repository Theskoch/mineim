from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render_to_response
from django.template import RequestContext


filter_time='-published_date'

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

#def post_list(request,filter_time='-published_date'):
 #   posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(filter_time)
 #   return render(request, 'blog/post_list.html', {'posts': posts})


def post_list(request):
    '''Show all news'''
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(filter_time)
    paginator = Paginator(posts, 1)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_list_sort_c(request,filt='#:C++'):
    posts = Post.objects.filter(text_id__contains=filt,published_date__lte=timezone.now()).order_by(filter_time)
    return render(request, 'blog/post_list.html', {'posts': posts})



def post_list_sort_c_operator(request):
    posts = Post.objects.filter(text_id__contains='#:C++_operators',published_date__lte=timezone.now()).order_by(filter_time)
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_list_sort_html(request):
    posts = Post.objects.filter(text_id__contains='#:Html',published_date__lte=timezone.now()).order_by(filter_time)
    return render(request, 'blog/post_list.html', {'posts': posts})