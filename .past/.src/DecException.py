# ! /Users/mn/.pyenv/shims/python
# ! -*- coding:utf-8 -*-


from OutputLogTime import OutputLogTime
# from Output import Output


def exception(name):  # 引数付きデコレータ
    def _exception(func):  #
        def wrapper(*args, **kargs):
            try:
                return func(*args, **kargs)
            except Exception as _e:
                OutputLogTime().call_result(_e, 0, name)
            else:
                OutputLogTime().call_result("a", 0, name)
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
                        print("retry urlopen in " + name)
                        continue
                    if counter >= 5:
                        OutputLogTime().call_result(_e, 0, "Error in " + name)
                else:
                    counter = 0
                    break
        return wrapper
    return _exception


