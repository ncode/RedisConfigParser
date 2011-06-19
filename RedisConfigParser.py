#!/usr/bin/python

import os
import sys
import redis
import simplejson
import ConfigParser

class RedisConfigParser(ConfigParser.RawConfigParser):

    __is_connected__ = False

    def connect(self, server):
        self.redis = redis.Redis(server)
        self.__is_connected__ = True

    def read(self, namespace, server='127.0.0.1'):
        self.connect(server)
        data = self.redis.get(namespace)
        if data == None:
            self.data = {}
        else:
            config = simplejson.loads(data)
            for section in config:
                self.add_section(section)
                for option, value in config[section].iteritems():
                    self.set(section, option, value)

    def migrate(self, configfile, namespace, server='127.0.0.1'):
        self.readfp(open(configfile))
        self.write(namespace, server)

    def write(self, namespace, server='127.0.0.1'):
        if not self.__is_connected__:
            self.connect(server)

        config = {}
        for section in self.sections():
            config.update({section: {}})
            for option, value in self.items(section):
                config[section].update({option: value})
        self.redis.set(namespace, simplejson.dumps(config))

