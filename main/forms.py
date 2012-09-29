from django import forms

from webgljobs.main.models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('approved', 'filled',)


class TweetForm(forms.Form):
    # 140-characters for tweet
    # - 17 for "New #WebGL #Job: "
    # - 1 char for space after summary.
    # - 20 for t.co URL
    summary = forms.CharField(max_length=102, required=False)
