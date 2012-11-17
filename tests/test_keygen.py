# -*- coding: utf-8 -*-

from unittest import TestCase

from redcache.cache_manager import CacheManager


class KeygenTestCase(TestCase):
    def test_no_args(self):
        cache_manager = CacheManager()

        def testfunc():
            pass

        assert cache_manager.key(testfunc, []) == 'cache:testfunc'

    def test_functions(self):
        cache_manager = CacheManager()

        def testfunc(a, b, c=None):
            pass

        args = [1, 2]
        assert cache_manager.key(testfunc, args) == 'cache:testfunc:1:2'

        args = ['a', 'b']
        assert cache_manager.key(testfunc, args) == 'cache:testfunc:a:b'

        def testfunc2(self, a, b, c=None):
            pass

        args = [None, 1, 2]
        assert cache_manager.key(testfunc2, args) == 'cache:testfunc2:1:2'

        def testfunc3(cls, a, b, c=None):
            pass

        args = [None, 1, 2]
        assert cache_manager.key(testfunc3, args) == 'cache:testfunc3:1:2'
