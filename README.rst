django-i18n-sitemap
===================

Usage
-----

Add ``i18nsitemap`` to your ``INSTALLED_APPS``

In your Sitemap class who supports i18n inherit from i18nsitemap.I18nSitemap instead from django.

Set ``i18n = True``

That's it. And there is no problem on using ``I18nSitemap`` on any Sitemap class, no needs to add or remove anything.

Here it follows an example

::

    class BlogSitemap(I18nSitemap):
        changefreq = "never"
        priority = 0.5
        i18n = True

        def items(self):
            return Entry.objects.filter(is_draft=False)

        def lastmod(self, obj):
            return obj.pub_date
