from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from webgljobs.main.models import Job


def approve(request, object_id):
    job = get_object_or_404(Job, pk=object_id)
    return HttpResponse("Approve %s" % (job.id,))


def disapprove(request, object_id):
    job = get_object_or_404(Job, pk=object_id)
    return HttpResponse("Disapprove %s" % (job.id,))