from django.urls import path
from django.views.generic.base import TemplateView

from main.feeds import LatestEntriesFeed, UnapprovedEntriesFeed
from main.forms import JobForm
from main.views import (
    approve, disapprove, front_page, job_detail, post_job,
    retweeter_oauth_callback, retweeter_setup_oath
)

urlpatterns = [

    path(
        "",
        front_page,
        name="main_page"
    ),

    path(
        '<int:object_id>/',
        job_detail,
        name="view_job"
    ),
    path(
        '<int:object_id>/approve$',
        approve,
        name="approve_job"
    ),
    path(
        '<int:object_id>/disapprove$',
        disapprove,
        name="disapprove_job"
    ),

    path(
        'feed/',
        LatestEntriesFeed(),
        name="feed"
    ),
    path(
        'unapproved_feed/',
        UnapprovedEntriesFeed(),
        name="unapproved_feed"
    ),

    path(
        "about/",
        TemplateView.as_view(template_name="about.html"),
        name="about_page"
    ),

    path(
        "add/",
        post_job,
        {
            "form_class": JobForm,
            "template_name": "create_new_job.html",
            "post_save_redirect": "/add/thanks",
        },
        name="create_new_job"
    ),
    path(
        "add/thanks",
        TemplateView.as_view(template_name="create_new_job_thanks.html"),
        name="create_new_job_thanks"
    ),

    path(
        "retweeter/intro",
        TemplateView.as_view(template_name="retweeter_intro.html"),
        name="retweeter_intro"
    ),
    path(
        "retweeter/setup_oauth",
        retweeter_setup_oath,
        name="retweeter_setup_oauth"
    ),
    path(
        "retweeter/oauth_callback",
        retweeter_oauth_callback,
        name="retweeter_oauth_callback"
    ),

]
