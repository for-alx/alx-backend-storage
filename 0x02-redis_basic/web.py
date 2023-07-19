#!/usr/bin/env python3
""" web cache module """

import redis
import requests
from typing import Callable
from functools import wraps
