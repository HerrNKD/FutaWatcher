# ! /Users/mn/.pyenv/shims/python
# ! -*- coding:utf-8 -*-

import linecache
from datetime import timedelta
import TimeGetter
import Output


class LogChecker(object):
    """
    log check
    """
    log = "/Users/work/futaba/slsatge/output.txt"

    def __init__(self):
        pass

    def get_line(self):
        """
        get line
        """
        num_lines = sum(1 for line in open(self.log))
        line = linecache.getline(self.log, (int(num_lines)-1)).rstrip()
        linecache.clearcache()
        return line

    def check_log(self):
        """
        check log
        """
        log_time = TimeGetter().get_log_time()
        now_time = TimeGetter().get_now_time()

        if log_time.hour == 00 and log_time.minute != 00:
            if not log_time.hour == now_time.hour:
                log_time = log_time + timedelta(days=1)

        time = log_time - now_time
        if time.total_seconds() > 0:
            Output("a", 0, "Thread has already been searched.").call_result()
