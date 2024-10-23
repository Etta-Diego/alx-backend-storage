Curriculum <br>
**Short Specializations** <br>

# 0x02. Redis basic

`Back-end` `Redis` `Database`

## Resources

**Read or watch:**

* [Redis commands](https://www.redis.io/commands/)
* [Redis python client](https://www.redis-py.readthedocs.io/en/stable/)
* [How to Use Redis With Python](https://www.realpython.com/python-redis/)
* [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)

## Requirement

* Files intrepreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7) and `redis` (version 4.0.9)
* Files must end with a new line
* The first line of files should be exactly `#!/usr/bin/env python3`
* Code should use the `pycodestyle` style (Version 2.5.*)
* All modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* All functions and coroutines should be type-annotated
* Mandatory `README.md` file

## Install Redis on Ubuntu 18.04

```
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```


## Tasks

### 0. Writing Strings to Redis
- **File:** `exercise.py`
- Implement a `Cache` class that stores data in Redis using a randomly generated key.
- Type-annotate the method to handle `str`, `bytes`, `int`, or `float`.

### 1. Reading from Redis and Recovering Original Type
- **File:** `exercise.py`
- Create a `get` method that retrieves the stored data and applies an optional conversion function.

### 2. Incrementing Values
- **File:** `exercise.py`
- Implement a `count_calls` decorator to track how many times a method is called.

### 3. Storing Lists
- **File:** `exercise.py`
- Define a `call_history` decorator to store the history of inputs and outputs for a function.

### 4. Retrieving Lists
- **File:** `exercise.py`
- Implement a `replay` function to display the history of function calls in Redis.

## Author
**Onyinyechi Ikediego**  
ALX Software Engineering Cohort 22  
GitHub: [Onyinyechi-Ikediego](https://github.com/Onyinyechi-Ikediego)

## License
© 2024 ALX. All rights reserved.


