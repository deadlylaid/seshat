from django.shortcuts import reverse
from reviewer.models import Reviewer, Service, Team, TeamMember
from reviewer.forms import ReviewerModelForm


def test_model_object_create():
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


def test_user_create_view(client):
    resp = client.get(reverse('joinus'))
    assert resp.status_code == 200
    assert isinstance(resp.context_data.get('form'), ReviewerModelForm)


def test_root_page_is_reveiwers(client):
    resp = client.get(reverse('reviewers'))
    assert resp.status_code == 200
