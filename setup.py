import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


dependency_path = 'http://linode.openhatch.org/~paulproteus/'

setup(
    name = "mysite",
    version = "3",
    packages = ['mysite',],
    url = 'https://openhatch.org/',
    license = 'AGPLv3',

    install_requires = ['setuptools',
                        'python-distutils-extra',
                        'twill==0.9.1-cc',
                        'invitation',
                        'celery==1.0',
                        'south==0.6-rc1',
                        'launchpadlib==1.5.3',
                        'django-assets==0.2',
                        'python-github2==0.1.1',
                        'pygeoip==0.1.3',
                        'django-debug-toolbar==0.8.1',
                        'pysolr',
                        'sisynala',
                        'django-haystack',
                        'hexagonit.recipe.download',
                        'django-voting',
                        'staticgenerator==1.4.1.2',
                       ],

    dependency_links = [dependency_path,
                        dependency_path + 'python_apt-0.6.17-py2.6-linux-i686.egg#egg=python-apt',
                        dependency_path + 'invitation-1.0.tar.gz#egg=invitation',
                        dependency_path + 'django-assets-0.2.tar.gz#egg=django-assets',
                        dependency_path + 'South-0.6_pre-py2.6.egg#egg=south',
                        'http://linode.openhatch.org/~paulproteus/python-github2-0.1.1.tar.gz#egg=python-github2',
                        'http://pygeoip.googlecode.com/files/pygeoip-0.1.3.zip#egg=pygeoip',
                        'http://linode.openhatch.org/~rafpaf/django-debug-toolbar-0.8.1.tar.gz#egg=django-debug-toolbar',
                        'http://linode.openhatch.org/~parker/django-voting-0.1.tar.gz#egg=django-voting',
                        dependency_path + 'staticgenerator-1.4.1.2.tar.gz#egg=staticgenerator',
                       ],

    zip_safe = False,
    include_package_data = True,

    description = "A website",

    author = 'The OpenHatch team <https://openhatch.org/about/>',
    author_email = 'all@openhatch.org',

    package_dir = {'': '.'},

)

