#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker """
import redis
import requests
from typing import Callable
from functools import wraps

red = redis.Redis()


def data_cacher(fn: Callable) -> Callable:
    """ """
    @wraps(fn)
    def wrapper(url):
        """"""
        red.incr(f"count:{url}")
        response = red.get(f"cached:{url}")
        if response:
            return response.decode('utf-8')
        result = fn(url)
        red.setex(f"cached:{url}", 10, result)
        return result

    return wrapper


@data_cacher
def get_page(url: str) -> str:
    """
    """
    response = requests.get(url)
    return response.text
