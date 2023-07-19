#!/usr/bin/env python3
""" Redis basic @"""
import redis
from uuid import uuid4
from typing import Callable, Any, Optional, Union
from functools import wraps


class Cache:
    """Cache
    """
    def __init__(self) -> None:
        """Initialize
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes,  int,  float]) -> str:
        """ Stores data in redis with randomly generated uuid key
        """
        key = str(uuid4())
        client = self._redis
        client.set(key, data)
        return key

    def get_str(self, data: bytes) -> str:
        """bytes to string
        """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """bytes to integers
        """
        return int(data)

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """correct data type
        """
        client = self._redis
        value = client.get(key)
        if not value:
            return
        if fn is int:
            return self.get_int(value)
        if fn is str:
            return self.get_str(value)
        if callable(fn):
            return fn(value)
        return value
