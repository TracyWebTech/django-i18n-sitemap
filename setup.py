
import os
import codecs

from setuptools import setup


def read(*parts):
    return codecs.open(os.path.join(os.path.dirname(__file__), *parts),
                       encoding='utf8').read()

setup(
    name='django-i18n-sitemap',
    description='Adds the possibility to have i18n urls in your sitemap',
    version='0.1',
    long_description=read('README.rst'),
    packages=['i18nsitemap'],
    author='Luan Pablo',
    author_email='luan@tracy.com.br',
    url='https://github.com/TracyWebTech/django-i18n-sitemap',
    license='GNU General Public License v2 (GPLv2)',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        ],
)
