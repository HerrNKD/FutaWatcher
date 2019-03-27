# ! /Users/mn/.pyenv/shims/python
# ! -*- coding:utf-8 -*-

import linecache
from datetime import datetime, timedelta
from Output import Output


class LogandTime(object):
    """
    Check Log
    get Log time line
    get Log time
    get now time
    """
    def __init__(self):
        pass

    def get_now_time(self):
        """
        get now time
        """
        now_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return datetime.strptime(now_string, "%Y-%m-%d %H:%M:%S")

    def get_line(self):
        """
        get line
        """
        num_lines = sum(1 for line in open(self.log))
        line = linecache.getline(self.log, (int(num_lines)-1)).rstrip()
        linecache.clearcache()
        return line

    def get_log_time(self):
        """
        get log time
        """
        finish_string = datetime.now().strftime("%Y-%m-%d ")
        log_line = self.get_line()
        finish_line = finish_string + log_line
        try:
            finish = datetime.strptime(finish_line, "%Y-%m-%d %H:%M")
        except Exception as _e:
            Output(_e, 0, "Error in GetLogTime").call_result()

        return finish

    def check_log(self):
        """
        check log
        """
        log_time = self.get_log_time()
        now_time = self.get_now_time()

        if log_time.hour == 00 and log_time.minute != 00:
            if not log_time.hour == now_time.hour:
                log_time = log_time + timedelta(days=1)

        time = log_time - now_time
        if time.total_seconds() > 0:
            Output("a", 0, "Thread has already been searched.").call_result()
