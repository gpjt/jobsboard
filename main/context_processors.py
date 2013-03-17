from django.conf import settings

def settings_for_templates(request):
    return {
        "JOBS_BOARD_TITLE": settings.JOBS_BOARD_TITLE,
        "JOB_TYPE_DESCRIPTION": settings.JOB_TYPE_DESCRIPTION ,
    }