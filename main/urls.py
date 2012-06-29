from django.conf.urls.defaults import patterns, include, url
from django.core.urlresolvers import reverse
from django.views.generic.simple import direct_to_template
from django.views.generic.create_update import create_object
from django.views.generic.list_detail import object_detail

from webgljobs.main.feeds import LatestEntriesFeed, UnapprovedEntriesFeed
from webgljobs.main.forms import JobForm
from webgljobs.main.models import Job

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
        create_object,
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
)
