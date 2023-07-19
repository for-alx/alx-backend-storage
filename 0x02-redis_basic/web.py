#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker """
import redis
import requests
from typing import Callable
from functools import wraps


def data_cacher(method: Callable) -> Callable:
    """
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """
        """
        client = redis.Redis()
        client.incr(f'count:{url}')
        cached_page = client.get(f'{url}')
        if cached_page:
            return cached_page.decode('utf-8')
        response = method(url)
        client.set(f'{url}', response, 10)
        return response
    return wrapper


@data_cacher
def get_page(url: str) -> str:
    """ Returns the content of a URL after caching
    """
    response = requests.get(url)
    return response.text
