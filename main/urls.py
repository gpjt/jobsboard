from django.conf.urls import url
from django.views.generic.base import TemplateView

from main.feeds import LatestEntriesFeed, UnapprovedEntriesFeed
from main.forms import JobForm
from main.views import (
    approve, disapprove, front_page, job_detail, post_job,
    retweeter_oauth_callback, retweeter_setup_oath
)

urlpatterns = [

    url(
        r"^$",
        front_page,
        name="main_page"
    ),

    url(
        r'^(?P<object_id>\d+)/$',
        job_detail,
        name="view_job"
    ),
    url(
        r'^(?P<object_id>\d+)/approve$',
        approve,
        name="approve_job"
    ),
    url(
        r'^(?P<object_id>\d+)/disapprove$',
        disapprove,
        name="disapprove_job"
    ),

    url(
        r'^feed/$',
        LatestEntriesFeed(),
        name="feed"
    ),
    url(
        r'^unapproved_feed/$',
        UnapprovedEntriesFeed(),
        name="unapproved_feed"
    ),

    url(
        r"^about/$",
        TemplateView.as_view(template_name="about.html"),
        name="about_page"
    ),

    url(
        r"^add/$",
        post_job,
        {
            "form_class": JobForm,
            "template_name": "create_new_job.html",
            "post_save_redirect": "/add/thanks",
        },
        name="create_new_job"
    ),
    url(
        r"^add/thanks$",
        TemplateView.as_view(template_name="create_new_job_thanks.html"),
        name="create_new_job_thanks"
    ),

    url(
        r"^retweeter/intro$",
        TemplateView.as_view(template_name="retweeter_intro.html"),
        name="retweeter_intro"
    ),
    url(
        r"^retweeter/setup_oauth$",
        retweeter_setup_oath,
        name="retweeter_setup_oauth"
    ),
    url(
        r"^retweeter/oauth_callback$",
        retweeter_oauth_callback,
        name="retweeter_oauth_callback"
    ),

]
