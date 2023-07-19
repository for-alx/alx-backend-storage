#!/usr/bin/env python3
""" Redis basic @"""
import redis
import sys
from uuid import uuid4
from typing import Callable, Any, Optional, Union
from functools import wraps


Types = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    """
    key = method.__qualname__
    i = "".join([key, ":inputs"])
    o = "".join([key, ":outputs"])

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        """
        self._redis.rpush(i, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(o, str(res))
        return res

    return wrapper


class Cache:
    """Cache
    """

    def __init__(self):
        """Initialize
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Types) -> str:
        """Stores data in redis with randomly generated uuid key
        """
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) \
            -> Types:
        """
        correct data type
        """
        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_int(self: bytes) -> int:
        """bytes to integers
        """
        return int.from_bytes(self, sys.byteorder)

    def get_str(self: bytes) -> str:
        """bytes to string
        """
        return self.decode("utf-8")
