import datetime
import pytest
from freezegun import freeze_time

from forum.models import Topic
from forum.tests_factories import TopicFactory

@pytest.mark.django_db
def describe_topic():
    def exists():
        TopicFactory()

    @freeze_time(datetime.datetime.now())
    def saves_its_fields():
        topic = TopicFactory()

        sut = Topic.objects.get(pk=topic.id)

        assert sut.title == topic.title
        assert sut.created_by == topic.created_by
        assert sut.created_at == datetime.datetime.now(datetime.timezone.utc)

    def is_registered_in_the_django_admin():
        from django.contrib.admin.sites import site as admin_site
        assert admin_site.is_registered(Topic)
