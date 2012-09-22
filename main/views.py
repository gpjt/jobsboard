from django.http import HttpResponse


def approve(request, object_id):
    return HttpResponse("Approve %s" % (object_id,))


def disapprove(request, object_id):
    return HttpResponse("Disapprove %s" % (object_id,))