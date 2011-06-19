# RedisConfigParser

A simple way to use redis as backend for python ConfigParser

## Requirements:

* redis-py - http://github.com/andymccurdy/redis-py
* simplejson - http://github.com/simplejson/simplejson

## Install:

    $ python setup.py build
    $ python setup.py install

## Usage:
### Connecting to redis:
    >>> import RedisConfigParser
    >>> config = RedisConfigParser.RedisConfigParser()
    >>> config.connect('server.example.org')

### Migrating from an oldconfig.cfg to redis
    >>> config.migrate('oldconfig.cfg', 'REDIS::CONFIG')

### Adding sections/options and writing to redis
    >>> config.add_section('redis')
    >>> config.set('redis', 'config', 'teste')
    >>> config.write('REDIS::CONFIG')

### Reading from redis
    >>> config.read('REDIS::CONFIG')
    >>> for section in config.sections():
    >>>     print config.items(section)
