from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic, Post
from .forms import TopicForm, PostForm



def topic_list(request):
    topics = Topic.objects.all().order_by('-created_at')
    return render(request, 'forum/topic_list.html', {'topics': topics})



def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    posts = topic.posts.all()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            post = form.save(commit=False)
            post.topic = topic
            post.author = request.user
            post.save()
            return redirect('topic_detail', pk=topic.pk)
    else:
        form = PostForm()

    return render(request, 'forum/topic_list.html', {'topic': topic, 'posts': posts, 'form': form})


@login_required
def create_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save()
            return redirect('topic_detail', pk=topic.pk)
    else:
        form = TopicForm()
    return render(request, 'forum/create_topic.html', {'form': form})

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('topic_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})