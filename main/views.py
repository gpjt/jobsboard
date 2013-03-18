from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.sites.models import Site
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

import tweepy

from jobsboard.main.forms import JobForm, TweetForm
from jobsboard.main.models import Job, Retweeter


def post_job(request, **kwargs):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            new_job = form.save()
            new_job.posted_from_ip = request.META.get('REMOTE_ADDR', None)
            new_job.save()
            new_job.check_spam()
            return redirect("/add/thanks", new_job)
    else:
        form = JobForm()

    return render(request, "create_new_job.html", { "form": form })


def tweet_and_retweet(tweet):
    auth = tweepy.OAuthHandler(settings.APP_CONSUMER_KEY, settings.APP_CONSUMER_SECRET)
    auth.set_access_token(settings.OWN_TWITTER_ACCOUNT_ACCESS_KEY, settings.OWN_TWITTER_ACCOUNT_ACCESS_SECRET)
    api = tweepy.API(auth)
    status = api.update_status(tweet)

    retweet_errors = []
    for retweeter in Retweeter.objects.all():
        try:
            auth = tweepy.OAuthHandler(settings.APP_CONSUMER_KEY, settings.APP_CONSUMER_SECRET)
            auth.set_access_token(retweeter.access_key, retweeter.access_secret)
            api = tweepy.API(auth)
            api.retweet(status.id)
        except Exception, e:
            retweet_errors.append("Retweet by %s failed due to %s" % (retweeter.username, e))
    return retweet_errors


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
            tweet = "New %s: %s %s" % (settings.TWITTER_HASHTAGS, form.cleaned_data["summary"], job_url)
            retweet_errors = tweet_and_retweet(tweet)
            return render(
                request,
                "job_approve_done.html",
                {
                    "job": job,
                    "tweet": tweet,
                    "retweet_errors": retweet_errors
                }
            )
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


def retweeter_setup_oath(request):
    auth = tweepy.OAuthHandler(settings.APP_CONSUMER_KEY, settings.APP_CONSUMER_SECRET)
    redirect_url = auth.get_authorization_url()
    request.session["request_token"] =  (auth.request_token.key, auth.request_token.secret)
    return HttpResponseRedirect(redirect_url)


def retweeter_oauth_callback(request):
    verifier = request.GET['oauth_verifier']
    auth = tweepy.OAuthHandler(settings.APP_CONSUMER_KEY, settings.APP_CONSUMER_SECRET)
    token = request.session["request_token"]
    request.session["request_token"] = ""
    auth.set_request_token(token[0], token[1])
    auth.get_access_token(verifier)
    users_access_key = auth.access_token.key
    users_access_secret = auth.access_token.secret

    auth = tweepy.OAuthHandler(settings.APP_CONSUMER_KEY, settings.APP_CONSUMER_SECRET)
    auth.set_access_token(users_access_key, users_access_secret)
    api = tweepy.API(auth)
    username = api.me().screen_name

    try:
        retweeter = Retweeter.objects.get(username=username)
    except Retweeter.DoesNotExist:
        retweeter = Retweeter(username=username)
    retweeter.access_key = users_access_key
    retweeter.access_secret = users_access_secret
    retweeter.save()

    return render(request, "retweeter_oauth_done.html", { "username": username })
