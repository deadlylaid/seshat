from django.contrib.auth import login, logout
from django.views.generic import CreateView, FormView, RedirectView
from django.shortcuts import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from reviewer.models import Reviewer
from reviewer.forms import ReviewerModelForm, LoginModelForm


class JoinUsView(CreateView):
    model = Reviewer
    template_name = "reviewer/joinus.html"
    form_class = ReviewerModelForm


class LogInView(FormView):
    template_name = "reviewer/login.html"
    form_class = LoginModelForm

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('reviewers')

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


class LogOutView(RedirectView):
    # permanent 가 true 이면 status code = 301
    # False 이면 status code = 302
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse('reviewers')
