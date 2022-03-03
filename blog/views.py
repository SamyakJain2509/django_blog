from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Topic
from .forms import CreatePostForm, CommentForm

def home(request):
    return render(request, 'blog/home.html')

def post_list(request):
    object_list = Post.objects.all()
    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/posts.html', {'page': page, 'posts': posts,})

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    form = CommentForm()
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.commenter = request.user
            new_comment.save()
            return redirect('home')

    return render(request, 'blog/post.html',{'post': post, 'form': form, 'comments':comments})
    
def create_post(request):
    form = CreatePostForm()

    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)  
            new_post.creator = request.user
            new_post.save()
            return redirect('posts')
    return render(request, 'blog/create.html', {'form': form})

def topic_posts(request, pk):
    topic = Topic.objects.get(id=pk)
    posts = topic.topic_posts.all()

    return render(request, 'blog/topic.html', {'topic': topic, 'posts': posts})

def browse(request):
    topics = Topic.objects.all()
    
    return render(request, 'blog/browse.html', {'topics': topics})