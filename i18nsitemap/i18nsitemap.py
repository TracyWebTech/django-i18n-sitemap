# -*- coding: utf-8 -*-

from django.contrib.sites.models import Site
from django.conf import settings
from django.contrib.sitemaps import Sitemap
from django.core import paginator
from django.core.exceptions import ImproperlyConfigured
from django.utils import translation


class I18nSitemap(Sitemap):
    i18n = False
    __get = Sitemap._Sitemap__get

    def get_urls(self, page=1, site=None, protocol=None):
        # Determine protocol
        if self.protocol is not None:
            protocol = self.protocol
        if protocol is None:
            protocol = 'http'

        # Determine domain
        if site is None:
            if Site._meta.installed:
                try:
                    site = Site.objects.get_current()
                except Site.DoesNotExist:
                    pass
            if site is None:
                raise ImproperlyConfigured("To use sitemaps, either enable the sites framework or pass a Site/RequestSite object in your view.")
        domain = site.domain

        if self.__get('i18n', self):
            urls = []
            for lang_code, lang_name in settings.LANGUAGES:
                translation.activate(lang_code)
                urls += self.urls(page, protocol, domain)
        else:
            urls = self.urls(page, protocol, domain)

        return urls

    def urls(self, page, protocol, domain):
        urls = []

        for item in self.paginator.page(page).object_list:
            loc = "%s://%s%s" % (protocol, domain, self.__get('location', item))
            priority = self.__get('priority', item, None)
            url_info = {
                'item':       item,
                'location':   loc,
                'lastmod':    self.__get('lastmod', item, None),
                'changefreq': self.__get('changefreq', item, None),
                'priority':   str(priority if priority is not None else ''),
            }
            urls.append(url_info)
        return urls
