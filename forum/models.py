from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название механики (Темы)")
    description = models.TextField(verbose_name="Описание чертежа")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Изобретатель")
    content = models.TextField(verbose_name="Текст донесения")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Правка от {self.author.username} в {self.topic.title}"