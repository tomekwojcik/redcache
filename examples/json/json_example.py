# -*- coding: utf-8 -*-
"""Example of using JSON to serialize cached objects."""

import json

from redcache import CacheManager, get_current_connection, use_connection


class JsonCacheManager(CacheManager):
    def before_save(self, data, **kwargs):
        return json.dumps(data)

    def after_load(self, data, **kwargs):
        return json.loads(data)

json_cache_manager = JsonCacheManager()


def test_json_cache_manager():
    @json_cache_manager.cache
    def cached(spam, eggs):
        return {'spam': spam, 'eggs': eggs}

    result = cached('spam', 'eggs')

    connection = get_current_connection()

    print connection.get('cache:cached:spam:eggs')
    connection.delete('cache:cached:spam:eggs')


if __name__ == '__main__':
    use_connection()
    test_json_cache_manager()
