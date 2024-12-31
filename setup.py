# -*- coding: utf-8 -*-

"""
`setup.py` for `django-multiupload-plus`.

For project information check out:
https://github.com/DmytroLitvinov/django-multiupload-plus

For `setup.py` information check out:
https://docs.python.org/3.11/distutils/setupscript.html
"""

import os

from setuptools import setup, find_packages

from multiupload_plus import __version__

REQUIREMENTS = [
    'django',
]

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Framework :: Django :: 3.2',
    'Framework :: Django :: 4.0',
    'Framework :: Django :: 4.1',
    'Framework :: Django :: 4.2',
    'Framework :: Django :: 5.0',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='django-multiupload-plus',
    version=__version__,
    description='Dead simple drop-in multi file upload field '
                'for django forms using HTML5\'s multiple attribute.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Dmytro Litvinov',
    author_email='me@dmytrolitvinov.com',
    url='https://github.com/DmytroLitvinov/django-multiupload-plus',
    packages=find_packages(),
    license='LICENSE.txt',
    platforms=['OS Independent'],
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    include_package_data=True,
    zip_safe=False,
)
