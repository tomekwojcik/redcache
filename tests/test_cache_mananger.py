# -*- coding: utf-8 -*-

import cPickle
import inspect
from redis import Redis
import time
from unittest import TestCase

from redcache.cache_manager import CacheManager
from redcache.connection import get_current_connection, pop_connection, push_connection


class CacheManagerTestCase(TestCase):
    def setUp(self):
        push_connection(Redis())

    def tearDown(self):
        pop_connection()

    def test_decorator(self):
        cache_manager = CacheManager()

        @cache_manager.cache
        def testfunc(a):
            return u'Cached "%s"' % unicode(a)

        val = testfunc('TEST')
        cached = cPickle.dumps(val)
        key = 'cache:testfunc:TEST'

        connection = get_current_connection()
        assert connection.get(key) == cached

        connection.delete(key)

    def test_timeout(self):
        cache_manager = CacheManager(ttl=5)

        @cache_manager.cache
        def testfunc(a):
            return u'Cached "%s"' % unicode(a)

        val = testfunc('TEST')
        cached = cPickle.dumps(val)
        key = 'cache:testfunc:TEST'

        connection = get_current_connection()
        assert connection.get(key) == cached

        time.sleep(6)
        assert connection.get(key) == None

        connection.delete(key)

    def test_explicit_connection(self):
        my_connection = Redis()
        cache_manager = CacheManager(connection=my_connection)

        assert cache_manager.connection == my_connection
        assert cache_manager.connection != get_current_connection()


