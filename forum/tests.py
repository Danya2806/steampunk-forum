from django.test import TestCase
from django.contrib.auth.models import User
from .models import Topic, Post
from .templatetags.steampunk_tags import steampunk_rank


class SteampunkForumTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Tesla', password='steam_password')
        self.topic = Topic.objects.create(
            title='Паровой котел сверхвысокого давления',
            description='Схема распределения пара по трубам.'
        )

    def test_topic_creation(self):
        self.assertEqual(Topic.objects.count(), 1)
        self.assertEqual(self.topic.title, 'Паровой котел сверхвысокого давления')

    def test_post_creation(self):
        post = Post.objects.create(topic=self.topic, author=self.user, content='Идея опасная, одобряю.')
        self.assertEqual(self.topic.posts.count(), 1)
        self.assertEqual(post.author.username, 'Tesla')

    def test_steampunk_rank_progression(self):

        self.assertEqual(steampunk_rank(self.user), "Подмастерье у котла")


        for i in range(52):
            Post.objects.create(topic=self.topic, author=self.user, content=f'Флуд №{i}')

        self.assertEqual(steampunk_rank(self.user), "Часовщик-Испытатель")