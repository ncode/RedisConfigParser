# RedisConfigParser

A simple way to use redis as backend for python ConfigParser

## Requirements:

redis-py - http://github.com/andymccurdy/redis-py
simplejson - http://github.com/simplejson/simplejson

## Usage:

    >>> import RedisConfigParser
    >>> config = RedisConfigParser.RedisConfigParser()
    >>> config.connect('server.example.org')

    >>> import RedisConfigParser
    >>> config = RedisConfigParser.RedisConfigParser()
    >>> config.migrate('oldconfig.cfg', 'REDIS::CONFIG')

    >>> import RedisConfigParser
    >>> config = RedisConfigParser.RedisConfigParser()
    >>> config.add_section('redis')
    >>> config.set('redis', 'config', 'teste')
    >>> config.write('REDIS::CONFIG')

    >>> import RedisConfigParser
    >>> config = RedisConfigParser.RedisConfigParser()
    >>> config.read('REDIS::CONFIG')
    >>> for section in config.sections():
    >>>     print config.items(section)
