from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.sites.models import Site

from webgljobs.main.forms import TweetForm
from webgljobs.main.models import Job



@staff_member_required
def approve(request, object_id):
    job = get_object_or_404(Job, pk=object_id)
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            job.approved = True
            job.save()
            site = Site.objects.all()[0]
            job_url = "http://%s%s" % (site.domain, job.get_absolute_url())
            tweet = "New #WebGL #Job: %s %s" % (form.cleaned_data["summary"], job_url)
            return render(request, "job_approve_done.html", { "job": job, "tweet": tweet })
    else:
        form = TweetForm()

    return render(request, "job_approve_confirm.html", { "job": job, "form": form })


@staff_member_required
def disapprove(request, object_id):
    job = get_object_or_404(Job, pk=object_id)
    if request.method == "GET":
        return render(request, "job_disapprove_confirm.html", { "job": job })
    if request.POST["confirmed"] != "yes":
        return HttpResponse("Erroneous form submission, should never happen...")
    job.delete()
    return render(request, "job_disapprove_done.html")
