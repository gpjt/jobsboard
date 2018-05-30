import markdown

from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.utils.safestring import mark_safe


class Job(models.Model):

    posted = models.DateTimeField(auto_now_add=True)

    approved = models.BooleanField(default=False)

    filled = models.BooleanField(default=False)

    spam = models.BooleanField(default=False)

    posted_by_user_agent = models.CharField(max_length=1024, default="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.172 Safari/537.22")

    posted_from_ip = models.IPAddressField(blank=True, null=True)

    title = models.CharField(max_length=1024)

    JOB_TYPE_CHOICES = (
        ("PT", "Part-time"),
        ("FT", "Full-time"),
        ("FL", "Freelance"),
        ("VL", "Volunteer"),
        ("OT", "Other"),
    )
    job_type = models.CharField(max_length=2, choices=JOB_TYPE_CHOICES)

    salary = models.CharField(max_length=128, blank=True)

    url = models.CharField(max_length=1024, blank=True)

    location = models.CharField(max_length=1024, blank=True)

    company = models.CharField(max_length=512, blank=True)


    description = models.TextField()

    contact_email = models.EmailField(max_length=254, blank=True)

    experience = models.CharField(max_length=128, blank=True)

    @models.permalink
    def get_absolute_url(self):
        return ('view_job', [str(self.id)])


    def __unicode__(self):
        return self.title


    def check_spam(self):
        if not settings.USE_AKISMET:
            return
        from akismet import Akismet
        site = Site.objects.all()[0]
        api = Akismet(key=settings.AKISMET_KEY, blog_url=site.domain)
        try:
            api.verify_key()
            self.spam = api.comment_check(
                self.description,
                data={
                    "user_ip": self.posted_from_ip,
                    "user_agent": self.posted_by_user_agent,
                    'comment_type': 'job-posting',
                    'comment_author': self.company,
                    'comment_author_email': self.contact_email,
                    'comment_author_url': self.url,
                }
            )
            self.save()
        except:
            pass


    def description_rendered(self):
        html = markdown.markdown(
            self.description,
            safe_mode='escape'
        )
        return mark_safe(html)


class Retweeter(models.Model):

    username = models.CharField(max_length=32, unique=True)

    access_key = models.CharField(max_length=70)

    access_secret = models.CharField(max_length=70)


    def __unicode__(self):
        return self.username





