# -*- coding: utf-8 -*-

import redis
from unittest import TestCase

import redcache.connection


class ConnectionTestCase(TestCase):
    def test_connect(self):
        redcache.connection.use_connection()
        connection = redcache.connection.get_current_connection()

        assert connection.echo('I work') == 'I work'

    def test_use_connection(self):
        r = redis.Redis()
        redcache.connection.use_connection(r)
        connection = redcache.connection.get_current_connection()

        assert connection == r
        assert connection.echo('I work') == 'I work'
