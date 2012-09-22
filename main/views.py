from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from webgljobs.main.models import Job



@staff_member_required
def approve(request, object_id):
    job = get_object_or_404(Job, pk=object_id)
    job.approved = True
    job.save()
    return HttpResponse("Job %s approved.  Not tweeted yet." % (job.id,))


@staff_member_required
def disapprove(request, object_id):
    job = get_object_or_404(Job, pk=object_id)
    job.delete()
    return HttpResponse("Job %s deleted." % (job.id,))