from django.views.generic import CreateView
from reviewer.models import Reviewer
from reviewer.forms import ReviewerModelForm

class JoinUsView(CreateView):

    model = Reviewer
    template_name = "reviewer/joinus.html"
    form_class = ReviewerModelForm