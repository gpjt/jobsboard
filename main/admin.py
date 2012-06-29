from django.contrib import admin
from webgljobs.main.models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('approved', 'filled', 'title', 'contact_email')
    list_filter = ('approved', 'filled')

admin.site.register(Job, JobAdmin)
