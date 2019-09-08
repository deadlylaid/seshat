import pytest
from .initial_values import *
from django.contrib.auth import get_user
from django.shortcuts import reverse
from reviewer.models import Reviewer, Service, Repository, Review


def test_model_object_create(access_db):
    reviewer = Reviewer.objects.create_user(
        email='test@test.com',
        username='test',
        password='test12',
    )
    assert isinstance(reviewer, Reviewer)
    service = Service.objects.create(
        name="Bitbucket",
    )
    assert isinstance(service, Service)
    repository = Repository.objects.create(
        name='gaia-finder',
        nickname='gaia'
    )
    review = Review.objects.create(
        reviewer=reviewer,
        repository=repository,
        title='first pullrequest',
        status='open',
    )
    assert isinstance(review, Review)


def test_login_view_get_status_200(client, user):
    resp = client.get(reverse('login'))
    assert resp.status_code == 200
    assert resp.context_data.get('form')


def test_login_view_post(client, user, access_db):
    resp = client.post(reverse('login'), data={'username': 'jadehan@test.com', 'password': 'test12'})
    user = get_user(client)
    assert resp.status_code == 302
    assert user.is_authenticated


def test_logout_view_status_302(client, user, access_db):
    client.post(reverse('login'), data={'username': 'test@test.com', 'password': 'test12'})
    resp = client.get(reverse('logout'))
    user = get_user(client)
    assert resp.status_code == 302
    assert not user.is_authenticated


def test_joinus_view_get_status_200(client, user):
    resp = client.get(reverse('joinus'))
    assert resp.status_code == 200
    assert resp.context_data.get('form')


def test_joinus_view_post_success(client, access_db):
    resp = client.post(reverse('joinus'), data={'email': 'joinus@test.com', 'username': 'joinus', 'password': 'joinus'})

    assert resp.status_code == 302
    assert resp.url == reverse('reviewers')
    assert Reviewer.objects.get(email='joinus@test.com')

    client.post(reverse('login'), data={'username': 'joinus@test.com', 'password': 'joinus'})
    user = get_user(client)
    assert user.is_authenticated


def test_reviewer_listview(client, user, access_db):
    resp = client.get(reverse('reviewers'))

    assert resp.status_code == 302
    assert resp.url == reverse('login') + '?next=/'

    client.login(email='jadehan@test.com', password='test12')

    resp = client.get(reverse('reviewers'))

    assert resp.status_code == 200
    _reviewer = resp.context_data.get('object_list')[0]
    assert _reviewer.username == 'jadehan'
    assert len(_reviewer.reviews()) == 1


@pytest.mark.parametrize('prq_status, bool_result, content, username, repository, prq_id, url',
                         [
                            (EX_OP_WH.prq_status, EX_OP_WH.bool_result, EX_OP_WH.content, EX_OP_WH.username, EX_OP_WH.repository, EX_OP_WH.prq_id, EX_OP_WH.url),
                            (EX_DC_WH.prq_status, EX_DC_WH.bool_result, EX_DC_WH.content, EX_DC_WH.username, EX_DC_WH.repository, EX_DC_WH.prq_id, EX_DC_WH.url),
                            (EX_MG_WH.prq_status, EX_MG_WH.bool_result, EX_MG_WH.content, EX_MG_WH.username, EX_MG_WH.repository, EX_MG_WH.prq_id, EX_MG_WH.url),
                            (UN_OP_WH.prq_status, UN_OP_WH.bool_result, UN_OP_WH.content, UN_OP_WH.username, UN_OP_WH.repository, UN_OP_WH.prq_id, UN_OP_WH.url),
                            (UN_DC_WH.prq_status, UN_DC_WH.bool_result, UN_DC_WH.content, UN_DC_WH.username, UN_DC_WH.repository, UN_DC_WH.prq_id, UN_DC_WH.url),
                            (UN_MG_WH.prq_status, UN_MG_WH.bool_result, UN_MG_WH.content, UN_MG_WH.username, UN_MG_WH.repository, UN_MG_WH.prq_id, UN_MG_WH.url),
                         ])
def test_webhook_status_200(prq_status, bool_result, content, username, repository, prq_id, url, client, user, access_db):

    # 먼저 기존 리뷰가 존재하는지 확인한다.
    exist_review = Review.objects.filter(repository__name=repository, pullrequest_id=prq_id).first()

    # WEBHOOK 을 가정한다.
    resp = client.post(reverse('webhook'), content.encode(), content_type="application/json")
    assert resp.status_code == 200

    # Reviewer 와의 외래키 연결을 확인한다.
    reviewer = Reviewer.objects.filter(username=username).first()
    assert bool(reviewer.review_set.filter(repository__name=repository, pullrequest_id=prq_id).first()) == bool_result

    review_after_webhook = Review.objects.filter(repository__name=repository, pullrequest_id=prq_id).first()

    if exist_review:
        if prq_status == 'OPEN':
            assert review_after_webhook.title == exist_review.title
            assert review_after_webhook.status == exist_review.status
            assert review_after_webhook.url == exist_review.url
        else:
            assert review_after_webhook.status == prq_status
            assert review_after_webhook.url == url
    else:
        if prq_status == 'OPEN':
            assert review_after_webhook.status == prq_status
            assert review_after_webhook.url == url
        else:
            assert review_after_webhook is None

