from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_detail

from jobsboard.main.feeds import LatestEntriesFeed, UnapprovedEntriesFeed
from jobsboard.main.forms import JobForm
from jobsboard.main.models import Job
from jobsboard.main.views import approve, disapprove, post_job, retweeter_oauth_callback, retweeter_setup_oath

urlpatterns = patterns("",

    url(
        r"^$",
        direct_to_template,
        {
            "template": "main_page.html",
            "extra_context": {
                "jobs": lambda: Job.objects.all().filter(filled=False).filter(approved=True).order_by("-id")
            }
        },
        name="main_page"
    ),

    url(
        r'^(?P<object_id>\d+)/$',
        object_detail,
        {
            "queryset": Job.objects.all(),
            "template_name": "job_detail.html",
            "template_object_name": "job"
        },
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
        direct_to_template,
        {
            "template": "about.html",
        },
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
        direct_to_template,
        {
            "template": "create_new_job_thanks.html",
        },
        name="create_new_job_thanks"
    ),

    url(
        r"^retweeter/intro$",
        direct_to_template,
        {
            "template": "retweeter_intro.html",
        },
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


)
