#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2012 Tomasz Wójcik <tomek@bthlabs.pl>. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#    1. Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#
#    2. Redistributions in binary form must reproduce the above copyright notice,
#       this list of conditions and the following disclaimer in the documentation
#       and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY TOMASZ WÓJCIK ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT
# SHALL TOMASZ WÓJCIK OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# The views and conclusions contained in the software and documentation are those
# of the authors and should not be interpreted as representing official policies,
# either expressed or implied, of Tomasz Wójcik.
#

import codecs
from setuptools import setup

version = '0.3'

desc_file = codecs.open('README.rst', 'r', 'utf-8')
long_description = desc_file.read()
desc_file.close()

setup(
    name="RedCache",
    version=version,
    packages=['redcache'],
    test_suite='nose.collector',
    zip_safe=False,
    platforms='any',
    install_requires=[
        'redis>=2.7.1',
    ],
    tests_require=[
        'nose',
    ],
    author=u'Tomasz Wójcik'.encode('utf-8'),
    author_email='tomek@bthlabs.pl',
    maintainer=u'Tomasz Wójcik'.encode('utf-8'),
    maintainer_email='tomek@bthlabs.pl',
    url='http://tomekwojcik.github.io/redcache/',
    download_url='https://github.com/tomekwojcik/redcache/tarball/v%s' % version,
    description='Lightweight and extensible caching framework for Python applications. It uses Redis as its storage backend.',
    long_description=long_description,
    license='https://github.com/tomekwojcik/redcache/blob/master/LICENSE',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)