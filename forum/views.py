from django.shortcuts import render, get_object_or_404, redirect  # Исправлено тут
from .models import Topic, Post
from django.contrib.auth.decorators import login_required


def index(request):
    topics = Topic.objects.all().order_by('-created_at')
    return render(request, 'forum/index.html', {'topics': topics})


def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)  # И исправлено тут
    posts = topic.posts.all().order_by('created_at')

    if request.method == 'POST' and request.user.is_authenticated:
        content = request.POST.get('content')
        if content:
            Post.objects.create(topic=topic, author=request.user, content=content)
            return redirect('topic_detail', topic_id=topic.id)

    return render(request, 'forum/topic_detail.html', {'topic': topic, 'posts': posts})