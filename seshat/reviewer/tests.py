import pytest
from .models import Reviewer


@pytest.mark.django_db
def test_reviewer_object_create():
    reviewer = Reviewer.objects.create_user(
        email='test@test.com',
        username='test',
        password='test12',
    )

    assert isinstance(reviewer, Reviewer)
