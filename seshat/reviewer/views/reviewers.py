from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from reviewer.models import Reviewer


class ReviewerListView(LoginRequiredMixin, ListView):
    login_url = 'joinus'
    model = Reviewer
    template_name = 'reviewer/list.html'
