#!/usr/bin/env python3
""" web cache module """
import redis
import requests
import time
from functools import wraps


def cache_with_expiration(time_in_seconds):
    """
    """
    def decorator(func):
        """
        """
        cache = {}

        @wraps(func)
        def wrapper(url):
            """
            """
            key = f"count:{url}"
            if key in cache and time.time() - cache[key][1] < time_in_seconds:
                return cache[key][0]

            result = func(url)
            cache[key] = (result, time.time())
            return result

        return wrapper

    return decorator


@cache_with_expiration(10)
def get_page(url):
    """
    """
    response = requests.get(url)
    return response.text
