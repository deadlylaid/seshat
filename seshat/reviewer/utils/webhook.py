import json

from collections import namedtuple

ParsedData = namedtuple('ParsedData', ('reviewers', 'repository', 'title', 'status', 'branch'))


class WebHookParser:

    def __init__(self, data, vc):
        if isinstance(data, bytes):
            self._data = json.loads(data)
        else:
            raise ValueError('data must be \'bytes\' type')

        if vc is 'bitbucket':
            self.data = self._bitbucket_parsing(self._data)
        else:
            raise ValueError('invalid vc, vc list [bitbucket, ]')

    def _bitbucket_parsing(self, _data):
        if self._data.get('pullrequest'):
            reviewers = self._data['pullrequest']['reviewers']
            repository = self._data['repository']['name']
            title = self._data['pullrequest']['title']
            status = self._data['pullrequest']['state']
            branch = self._data['pullrequest']['source']['branch']['name']
            return ParsedData(reviewers, repository, title, status, branch)

    def _github_parsing(self, _data):
        raise NotImplementedError
