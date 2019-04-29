#encoding=utf-8
"""
@version: 1
@author: Duke
@file:verify.py
@time:2019/4/28 5:23 PM
"""


class SubcommandLengthError(Exception):
    def __str__(self):
        return "command length error"


def args_count(argv_length):
    def decorator(func):
        def wrapper(*argv):
            if len(argv) != argv_length:
                raise SubcommandLengthError
            func(argv)
        return wrapper
    return decorator
