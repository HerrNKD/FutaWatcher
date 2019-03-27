# ! /Users/mn/.pyenv/shims/python
# ! -*- coding:utf-8 -*-

import sys
import logging

log = logging.getLogger(__name__)


def exception(name):  # 引数付きデコレータ
    def _exception(func):  #
        def wrapper(*args, **kargs):
            try:
                return func(*args, **kargs)
            except Exception as _e:
                print("None" + _e)
            else:
                print("None")
        return wrapper
    return _exception


def exception5(name):
    def _exception(func):
        def wrapper(*args, **kargs):
            counter = 0
            while True:
                try:
                    return func(*args, **kargs)
                except Exception as _e:
                    counter += 1
                    if counter <= 5:
                        log.debug("retry urlopen in " + name)
                        continue
                    if counter >= 5:
                        log.debug("Error in " + name + " : " + str(_e))
                        print("None")
                        sys.exit()
                else:
                    counter = 0
                    break
        return wrapper
    return _exception
