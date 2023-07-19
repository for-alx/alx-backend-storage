#!/usr/bin/env python3
""" Redis basic @"""
import redis
from uuid import uuid4
from typing import Callable, Any, Optional, Union
from functools import wraps


class Cache:
    """ Comment
    """
    def __init__(self) -> None:
        """ Comment
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes,  int,  float]) -> str:
        """ Comment
        """
        key = str(uuid4())
        client = self._redis
        client.set(key, data)
        return key
