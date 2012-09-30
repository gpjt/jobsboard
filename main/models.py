from django.db import models

class Job(models.Model):

    posted = models.DateTimeField(auto_now_add=True)

    approved = models.BooleanField(default=False)

    filled = models.BooleanField(default=False)

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


class Retweeter(models.Model):

    username = models.CharField(max_length=32)

    access_key = models.CharField(max_length=70)

    access_secret = models.CharField(max_length=70)


    def __unicode__(self):
        return self.username
