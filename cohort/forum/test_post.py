import datetime

import factory.django
import pytest
from freezegun import freeze_time
from django.contrib.auth.models import User

from forum.models import Post
from forum.tests_factories import PostFactory


@pytest.mark.django_db
def describe_post():
    def exists():
        PostFactory()

    @freeze_time(datetime.datetime.now())
    def saves_its_fields():
        post = PostFactory()

        sut = Post.objects.get(pk=post.id)

        assert sut.comment == post.comment
        assert sut.created_by == post.created_by
        assert sut.created_at == datetime.datetime.now(datetime.timezone.utc)
        assert sut.topic == post.topic

    def is_registered_in_the_django_admin():
        from django.contrib.admin.sites import site as admin_site
        assert admin_site.is_registered(Post)
