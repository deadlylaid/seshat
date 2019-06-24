from django.forms import ModelForm
from reviewer.models.reviewer import Reviewer


class ReviewerModelForm(ModelForm):

    class Meta:
        model = Reviewer
        fields = ['email', 'username', 'password']