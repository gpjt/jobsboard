from django import forms

from webgljobs.main.models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('approved', 'filled',)