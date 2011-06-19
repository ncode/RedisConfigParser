# RedisConfigParser

A simple way to use redis as backend for python ConfigParser

## Requirements:

* redis-py - http://github.com/andymccurdy/redis-py
* simplejson - http://github.com/simplejson/simplejson

## Usage:
### Connecting to redis server:
    >>> import RedisConfigParser
    >>> config = RedisConfigParser.RedisConfigParser()
    >>> config.connect('server.example.org')

### Migrating data from a old config file to redis
    >>> import RedisConfigParser
    >>> config = RedisConfigParser.RedisConfigParser()
    >>> config.migrate('oldconfig.cfg', 'REDIS::CONFIG')

### Adding sections/options and writing to redis
    >>> import RedisConfigParser
    >>> config = RedisConfigParser.RedisConfigParser()
    >>> config.add_section('redis')
    >>> config.set('redis', 'config', 'teste')
    >>> config.write('REDIS::CONFIG')

### Reading your config from redis
    >>> import RedisConfigParser
    >>> config = RedisConfigParser.RedisConfigParser()
    >>> config.read('REDIS::CONFIG')
    >>> for section in config.sections():
    >>>     print config.items(section)
