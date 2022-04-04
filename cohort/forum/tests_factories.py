from django.contrib.auth.models import User
import factory.django

from forum.models import Topic, Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker('email')
    username = factory.Faker('user_name')


class TopicFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Topic

    title = factory.Faker('sentence')
    created_by = factory.SubFactory(UserFactory)


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    comment = factory.Faker('sentence')
    created_by = factory.SubFactory(UserFactory)
    topic = factory.SubFactory(TopicFactory)
