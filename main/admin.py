from django.contrib import admin
from webgljobs.main.models import Job, Retweeter

class JobAdmin(admin.ModelAdmin):
    list_display = ('approved', 'filled', 'title', 'contact_email')
    list_display_links = ('title',)
    list_filter = ('approved', 'filled')

admin.site.register(Job, JobAdmin)


class RetweeterAdmin(admin.ModelAdmin):
    list_display = ('username',)
    list_display_links = ('username',)

admin.site.register(Retweeter, RetweeterAdmin)