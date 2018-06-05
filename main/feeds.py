from django.conf import settings
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed

from main.models import Job


# Keep Chrome happy as per http://stackoverflow.com/a/1081023/32846 -- thanks to
# David and Everyblock
class CorrectMimeTypeFeed(Rss201rev2Feed):
    mime_type = 'application/xml'


class LatestEntriesFeed(Feed):
    feed_type = CorrectMimeTypeFeed

    title = settings.JOBS_BOARD_TITLE
    link = "/"
    description = "An aggregator for " + settings.JOB_TYPE_DESCRIPTION

    description_template = 'feed_description.html'

    def author_name(self):
        return "Giles Thomas"

    def items(self):
        return Job.objects.filter(approved=True).order_by("-posted")[:20]

    def item_title(self, item):
        if item.filled:
            return "FILLED: " + item.title
        return item.title

    def item_description(self, item):
        return item.description

    def item_author_name(self, item):
        return item.company

    def item_pubdate(self, item):
        return item.posted


class UnapprovedEntriesFeed(Feed):
    feed_type = CorrectMimeTypeFeed

    title = settings.JOBS_BOARD_TITLE + " Approval list"
    link = "/"
    description = settings.JOB_TYPE_DESCRIPTION + " that have yet to be approved.  Spam has been filtered by Akismet if it's configured."

    description_template = 'unapproved_feed_description.html'

    def author_name(self):
        return "Giles Thomas"

    def items(self):
        return Job.objects.filter(approved=False).exclude(spam=True).order_by("-posted")

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_author_name(self, item):
        return item.company

    def item_pubdate(self, item):
        return item.posted