from django.views.generic import View
from django.http import HttpResponse

from reviewer.utils.webhook import WebHookParser


class WebHookView(View):

    def post(self, request):
        hooked_data = request.POST.get('data')
        data = WebHookParser(hooked_data, 'bitbucket')
        return HttpResponse(data.nickname)
