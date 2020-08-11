import logging
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.contrib import messages

from shortener.forms import UrlCreateForm
from shortener.models import Url
from shortener.mixins import BaseView

from django.conf import settings


logger = logging.getLogger(__name__)


class UrlView(BaseView):
    def get(self, request, hash):
        logger.info('Request to get a site with a hash - {}'.format(hash))
        try:
            url = Url.objects.get(url_hash=hash)
            logger.info('Redirect to {} by hash - {}'.format(url.url, hash))
            return HttpResponseRedirect(url.url)
        except Url.DoesNotExist as e:
            logger.warning('{} - Request by hash {}'.format(e, hash))
        raise Http404


class UrlCreate(BaseView):
    def get(self, request):
        form = UrlCreateForm()
        return render(request, 'shortener/index.html', context={'form': form})

    def post(self, request):
        form = UrlCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                logger.info('Try get short url by request - {}'.format(cd['url']))
                url = Url.objects.get(url=cd['url'])
                logger.info('Response short url {} by request - {}'.format(url.url_short, cd['url']))
            except Url.DoesNotExist as e:
                logger.warning('{} - Does not exist site by url {}'.format(e, hash))
                url = Url.objects.create(url=cd['url'])
                logger.info('{} - Create site record with url {}'.format(e, cd['url']))
        else:
            return render(request, 'shortener/index.html', context={'form': form})
        messages.success(request, url.url_short)
        return render(request, 'shortener/index.html', context={'form': form})
