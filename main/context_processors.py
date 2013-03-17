from django.conf import settings

def settings_for_templates(request):
    return {
        "JOBS_BOARD_TITLE": settings.JOBS_BOARD_TITLE,
        "JOB_TYPE_DESCRIPTION": settings.JOB_TYPE_DESCRIPTION,
        "EMAIL_SITE_ADDRESS": settings.EMAIL_SITE_ADDRESS,
        "OWN_TWITTER_ACCOUNT_ID": settings.OWN_TWITTER_ACCOUNT_ID,
    }