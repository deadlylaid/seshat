from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from reviewer.utils.webhook import WebHookParser
from reviewer.utils.review_update import review_update


class WebHookView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        hooked_data = request.body
        parser = WebHookParser(hooked_data, 'bitbucket')
        review_update(parser.data)
        return HttpResponse(parser.data.reviewers)
