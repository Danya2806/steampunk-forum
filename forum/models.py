from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок чертежа")
    description = models.TextField(verbose_name="Суть замысла")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Ветка обсуждения"
        verbose_name_plural = "Ветки обсуждений"

    def __str__(self):
        return self.title

class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    content = models.TextField(verbose_name="Текст послания")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return f"Послание от {self.author.username} в {self.topic.title}"