#!/usr/bin/env python3
'''
'''
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self) -> None:
        '''Initialize Cache
        '''
        self._redis = redis.Redis()

    def store(self, data: Union[str, int, float, bytes]) -> str:
        '''store the input data in Redis using the random key and return key.
        '''
        keys = str(uuid.uuid4())
        self._redis.set(keys, data)
        return keys