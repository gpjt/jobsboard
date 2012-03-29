from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

from webgljobs.main.models import Job

urlpatterns = patterns("",
    url(
        r"^$",
        direct_to_template,
        {
            "template": "main_page.html",
            "extra_context": {
                "jobs": Job.objects.all
            }
        },
        name="main_page"
    ),
)
