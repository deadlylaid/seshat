from django.contrib.auth import get_user
from django.shortcuts import reverse
from reviewer.models import Reviewer, Service, Team, TeamMember


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
    team = Team.objects.create(
        name='JadeTeam',
    )
    assert isinstance(team, Team)
    team_member = TeamMember.objects.create(
        user=reviewer,
        team=team
    )
    assert isinstance(team_member, TeamMember)


def test_login_view_get_status_200(client, user):
    resp = client.get(reverse('login'))
    assert resp.status_code == 200
    assert resp.context_data.get('form')


def test_login_view_post(client, user, access_db):
    resp = client.post(reverse('login'), data={'username': 'test@test.com', 'password': 'test12'})
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

def test_reviewer_listview_only_loggined_user(client, user, access_db):
    resp = client.get(reverse('reviewers'))

    assert resp.status_code == 302
    assert resp.url == reverse('login') + '?next=/'

    client.login(email='test@test.com', password='test12')

    resp = client.get(reverse('reviewers'))

    assert resp.status_code == 200
    assert len(resp.context_data.get('object_list')) == 1
