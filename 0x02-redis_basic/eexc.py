#!/usr/bin/env python3

"""
Create a Cache class. In the __init__ method, store an instance of
the Redis client as a private variable named _redis
(using redis.Redis()) and flush the instance using flushdb.

Create a store method that takes a data argument and returns a
string. The method should generate a random key (e.g. using uuid),
store the input data in Redis using the random key and return the key.

Type-annotate store correctly.
"""

import redis 
import uuid
from typing import Union

class Cache(method: Callable) -> Callable:
    def __init__(self):
        """
        stores an instance of the Redis client as a private variable
        named _redis (using redis.Redis()) and flush the instance
        using flushdb.
        """

        self._redis = redis.Redis
                # Flush the Redis database
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the data in Redis with a random key and return the key.

        Args:
            data (Union[str, bytes, int, float]): The data to store.

        Returns:
            str: The randomly generated key.
        """
        # Generate a random key using uuid
        key = str(uuid.uuid4())
        # Store the data in Redis using the random key
        self._redis.set(key, data)
        # Return the generated key
        return key
