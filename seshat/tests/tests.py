from reviewer.models import Reviewer, Service, Team, TeamMember


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
