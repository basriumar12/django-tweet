from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from .models import Tweet

def index(request):
    return render(request, 'index.html')

def list(request):
    tweets = Tweet.objects.order_by('-created_at').all()
    return render(request, 'tweets.html', { 'tweets': tweets })

def create(request):
    tweet = Tweet()
    tweet.text = request.POST.get('tweet', None)
    tweet.save()

    return HttpResponseRedirect(reverse('tweets:list'))
