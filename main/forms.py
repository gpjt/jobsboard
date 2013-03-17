from django import forms
from django.conf import settings

from jobsboard.main.models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('approved', 'filled', 'posted_from_ip')


class TweetForm(forms.Form):
    # 140-characters for tweet
    # - 1 char for space after summary.
    # - 20 for t.co URL
    # - 6 - hashtag length for "New (hashtags): "
    summary = forms.CharField(max_length=113 - len(settings.TWITTER_HASHTAGS), required=False)
