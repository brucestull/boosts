from django import forms
from django.forms import ModelForm

from boosts.models import Statement


class StatementForm(ModelForm):
    """
    ModelForm for the Statement model. This form uses bootstrap.
    """
    class Meta:
        model = Statement
        fields = ["body"]
        widgets = {
            "body": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "What's your inspiration for today?",
                    "rows": 3,
                }
            )
        }
        labels = {
            "body": "Inspirational Statement",
        }
