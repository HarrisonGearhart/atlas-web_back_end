#!/usr/bin/env python3
"""
Redis-based Cache System
"""

import uuid
import redis
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that tracks how many times a method is called.
    The count is stored in Redis using the method's qualified name.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator that logs the input arguments and return values
    of a method to Redis lists.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))

        return result
    return wrapper


def replay(method: Callable):
    """
    Displays the number of times a method was called,
    along with the inputs and outputs from each call.
    """
    redis_client = method.__self__._redis
    method_name = method.__qualname__
    inputs = redis_client.lrange(f"{method_name}:inputs", 0, -1)
    outputs = redis_client.lrange(f"{method_name}:outputs", 0, -1)

    print(f"{method_name} was called {len(inputs)} times:")
    for inp, outp in zip(inputs, outputs):
        print(f"{method_name}(*{inp.decode()}) -> {outp.decode()}")


class Cache:
    """
    Cache class for storing and retrieving data using Redis.
    Tracks usage statistics and call history for the `store` method.
    """

    def __init__(self):
        """
        Initializes the Redis client and clears any existing data.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the given data in Redis under a randomly generated UUID key.

        Args:
            data: The data to store (str, bytes, int, or float).

        Returns:
            A string UUID key used to store the data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieves a value from Redis by key, optionally applying a conversion function.

        Args:
            key: Redis key to look up.
            fn: Optional function to convert the retrieved data.

        Returns:
            The value stored in Redis, converted if fn is provided.
        """
        value = self._redis.get(key)
        return fn(value) if value is not None and fn else value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves a string from Redis by key.

        Args:
            key: Redis key to retrieve.

        Returns:
            The decoded string or None if not found.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves an integer from Redis by key.

        Args:
            key: Redis key to retrieve.

        Returns:
            The integer value or None if not found.
        """
        return self.get(key, fn=int)
