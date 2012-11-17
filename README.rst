RedCache
========

RedCache is a lightweight and extensible caching framework for Python
applications. It uses Redis as its storage backend.

Quickstart
----------

Suppose we have a function that loads data from a remote source::

    def load_something_from_somewhere():
        # Load the data...
        return data

Now let's use it in a Flask view::

    @app.route('/something/')
    def get_something():
        data = load_something_from_somewhere()
        # Do something with the data...
        return jsonify(data=data)

The problem here is that the view will wait until the data is fetched. If the
view is called often it'll generate significant traffic between our server and
the remote source. This isn't pretty.

What if we cached the loaded data for some time and refresh it only when the
cache expires? That would be pretty.

There are many caching solutions, e.g.
`Beaker <http://beaker.readthedocs.org/en/latest/>`_. RedCache is similar to
(and inspired by) Beaker but provides only one storage backend - Redis.

So, how do you cache *load_something_from_somewhere* using Redis and RedCache?

First setup Redis connection before starting the app::

    from redcache import use_connection
    use_connection()

Then make the function cached::

    from redcache import default_cache

    @default_cache.cache(ttl=5)
    def load_something_from_somewhere():
        # Load the data...
        return data

Next time *load_something_from_somewhere* is called RedCache will try to load
its last return value from Redis. If it's not found then the function will be
executed and its return value stored in Redis for 5 seconds.

``redcache.default_cache`` is an instance of
``redcache.cache_manager.DefaultCacheManager`` which gives convenient
access to caching mechanism which uses cPickle behind
the scenes. By default the keys will be stored infinitely. Use *ttl* keyword
argument in the decorator to define different TTL.

Extending and advanced use
--------------------------

RedCache can be easily extended to utilize Redis' datatypes and features.

By overriding ``redcache.cache_manager.CacheManager.after_load`` and
``redcache.cache_manager.CacheManager.before_save`` you can perform
additional operations on data. This way you can e.g. store JSON strings instead
of pickled objects.

By overriding
``redcache.cache_manager.CacheManager.load`` and
``redcache.cache_manager.CacheManager.save`` you can change the way data
is loaded and saved. This way you can e.g. store lists of individual objects
and retrieve them according to pagination options.

Consult examples to see how to integrate RedCache with SQLAlchemy and to see
how to use JSON instead of cPickle.

Author, credits and license
---------------------------

RedCache is developed by `BTHLabs <http://www.bthlabs.pl/>`_.

RedCache is licensed under BSD License.
See `LICENSE <https://github.com/tomekwojcik/redcache/blob/master/LICENSE>`_
for more details.

This project uses Redis connection management code from
`RQ <http://python-rq.org/>`_.

This project uses context-local objects code from
`Werkzeug <http://werkzeug.pocoo.org/>`_.

Source code
-----------

Source code is available from
`project repository <https://github.com/tomekwojcik/redcache/>`_ on GitHub.