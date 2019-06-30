from django.shortcuts import reverse
from reviewer.models import Reviewer, Service, Team, TeamMember
from reviewer.forms import ReviewerModelForm


def test_model_object_create(access_db):
    reviewer = Reviewer.objects.create_user(
        email='test@test.com',
        username='test',
        password='test12',
    )
    assert isinstance(reviewer, Reviewer)
    service = Service.objects.create(
        name="Bitbucket",
        api='https://api.bitbucket.org/2.0/'
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


def test_joinus_view_get_status_200(client, user):
    resp = client.get(reverse('joinus'))
    assert resp.status_code == 200
    assert resp.context_data.get('form')


def test_joinus_view_post_success(client, access_db):
    resp = client.post(reverse('joinus'), data={'email': 'joinus@test.com', 'username': 'joinus', 'password': 'joinus'})

    assert resp.status_code == 302
    assert resp.url == reverse('reviewers')
    assert Reviewer.objects.get(email='joinus@test.com')


def test_reviewer_listview_only_loggined_user(client, user, access_db):
    resp = client.get(reverse('reviewers'))

    assert resp.status_code == 302
    assert resp.url == reverse('joinus') + '?next=/'

    client.login(email='test@test.com', password='test12')

    resp = client.get(reverse('reviewers'))

    assert resp.status_code == 200
    assert len(resp.context_data.get('object_list')) == 1