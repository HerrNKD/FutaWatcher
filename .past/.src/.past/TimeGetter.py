# ! /Users/mn/.pyenv/shims/python
# ! -*- coding:utf-8 -*-

from datetime import datetime
from LogChecker import LogChecker
from Output import Output


class TimeGetter(object):
    """
    TimeGetter
    """

    def __init__(self):
        pass

    def get_now_time(self):
        """
        get now time
        """
        now_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return datetime.strptime(now_string, "%Y-%m-%d %H:%M:%S")

    def get_log_time(self):
        """
        get log time
        """
        finish_string = datetime.now().strftime("%Y-%m-%d ")
        log_line = LogChecker().get_line()
        finish_line = finish_string + log_line
        try:
            finish = datetime.strptime(finish_line, "%Y-%m-%d %H:%M")
        except Exception as _e:
            Output(_e, 0, "Error in GetLogTime").call_result()

        return finish
