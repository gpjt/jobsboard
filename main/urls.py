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
                "jobs": lambda: Job.objects.all().filter(approved=True)
            }
        },
        name="main_page"
    ),
    url(
        r"^about/$",
        direct_to_template,
        {
            "template": "about.html",
        },
        name="about_page"
    ),
)
