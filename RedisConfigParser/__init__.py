__version__ = '0.0.1'
VERSION = tuple(map(int, __version__.split('.')))
__all__ = ['RedisConfigParser']
__author__ = 'Juliano Martinez <juliano@martinez.io>'

import io
import redis
import simplejson
import ConfigParser

class RedisConfigParser(ConfigParser.RawConfigParser):

    __is_connected__ = False

    def __init__(self):
        ConfigParser.RawConfigParser.__init__(self)
        self._raw_write = getattr(ConfigParser.RawConfigParser, 'write')

    def connect(self, server='127.0.0.1', port=6379 db=6):
        self.redis = redis.Redis(server, port, db)
        self.__is_connected__ = True

    def read(self, namespace):
        if not self.__is_connected__:
            self.connect()
        self.readfp(io.BytesIO(simplejson.loads(self.redis.get(namespace))))

    def migrate(self, configfile, namespace):
        self.readfp(open(configfile))
        self.write(namespace, server)

    def write(self, namespace):
        if not self.__is_connected__:
            self.connect()

        config = io.BytesIO()
        self._raw_write(self, config)
        config.seek(0)
        self.redis.set(namespace, simplejson.dumps(config.read()))

