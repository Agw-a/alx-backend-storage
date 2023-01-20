#!/usr/bin/env python3
'''Defines Redis Storage
'''
import redis
import uuid
from typing import Union, Callable


class Cache:
    def __init__(self) -> None:
        '''Initialize Cache
        '''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, int, float, bytes]) -> str:
        '''store the input data in Redis using the random key and return key.
        '''
        keys = str(uuid.uuid4())
        self._redis.set(keys, data)
        return keys

    def get(self, key: str, fn: Callable = None
            ) -> Union[str, int, float, bytes]:
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        pass
