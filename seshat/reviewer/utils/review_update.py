from reviewer.models import Review, Reviewer, Repository


def review_update(parsed_data):
    _repository, is_exist = Repository.objects.get_or_create(
        name=parsed_data.repository,
        defaults={'nickname': parsed_data.repository},
    )

    if parsed_data.status == 'OPEN':
        for reviewer in parsed_data.reviewers:
            _reviewer = Reviewer.objects.get(username=reviewer)
            Review.objects.create(
                reviewer=_reviewer,
                repository=_repository,
                title=parsed_data.title,
                status=parsed_data.status,
                branch=parsed_data.branch
            )
    elif parsed_data.status == 'DECLINED' or parsed_data.status == 'MERGED':
        review = Reviewer.objects.filter(
            branch=parsed_data.branch,
            status='OPEN'
        )
        if review:
            review[0].status = parsed_data.status
            review[0].save()
