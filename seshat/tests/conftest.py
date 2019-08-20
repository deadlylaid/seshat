import pytest
from reviewer.models import Reviewer, Service, Repository, Review


@pytest.fixture
def access_db(db):
    pass


# db fixture 는 이미 function 수준의 scope를 갖고 있기 때문에
# 다른 scope를 fixture로 설정하면 에러를 반환한다.
# 그렇기 때문에 django_db_blocker를 사용한다.
# 하지만 django_db_blocker는 unblock 함수를 실행할 경우
# 계속해서 db 접근 상태를 열어놓기 때문에, test를 진행하는 동안 데이터가 변경되기도 한다.
# 때문에 되도록 django_db_blocker 를 사용할 경우 테스트 간에 데이터를 변경하지 말아야한다.
@pytest.fixture(scope='module')
def user(django_db_blocker):
    with django_db_blocker.unblock():
        reviewer = Reviewer.objects.create_user(
            email='jadehan@test.com',
            username='jadehan',
            password='test12'
        )
        service = Service.objects.create(
            name='github',
        )
        repository = Repository.objects.create(
            name='data',
            nickname='data',
        )
        review = Review.objects.create(
            reviewer=reviewer,
            repository=repository,
            title='first pullrequest',
            status='OPEN',
            branch='feature/abcd'
        )
        decliend_review = Review.objects.create(
            reviewer=reviewer,
            repository=repository,
            title='decliend pullrequest',
            status='DECLIEND',
            branch='feature/fail'
        )

