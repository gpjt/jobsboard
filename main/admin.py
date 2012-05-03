from django.contrib import admin
from webgljobs.main.models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'contact_email')
    list_filter = ('approved',)

admin.site.register(Job, JobAdmin)
