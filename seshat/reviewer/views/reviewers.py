from django.views.generic import ListView
from reviewer.models import Reviewer


class ReviewerListView(ListView):

    model = Reviewer
    template_name = 'reviewer/list.html'