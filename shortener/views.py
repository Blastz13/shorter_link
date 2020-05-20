from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.views import View

from shortener.forms import UrlCreateForm
from shortener.models import Url


class UrlView(View):
    def get(self, request, hash):
        url = get_object_or_404(Url, url_hash=hash)
        return HttpResponseRedirect(url.url)


class UrlCreate(View):
    def get(self, request):
        form = UrlCreateForm()
        return render(request, 'shortener/index.html', context={'form': form})

    def post(self, request):
        form = UrlCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                url = Url.objects.get(url=cd['url'])
            except Url.DoesNotExist:
                url = Url.objects.create(url=cd['url'])
        else:
            return render(request, 'shortener/index.html', context={'form': form})
        messages.success(request, url.url_short)
        return render(request, 'shortener/index.html', context={'form': form})
