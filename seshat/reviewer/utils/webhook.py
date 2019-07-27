import json


class WebHookParser:

    def __init__(self, data, vc):
        if isinstance(data, str):
            self._data = json.loads(data)
        else:
            raise ValueError

        if vc is 'bitbucket':
            self._bitbucket_parsing(self._data)
        else:
            raise ValueError('invalid vc, vc list [bitbucket, ]')

    def _bitbucket_parsing(self, _data):
        if self._data.get('pullrequest'):
            self.nickname = self._data['actor']['nickname']

    def _github_parsing(self, _data):
        raise NotImplementedError
