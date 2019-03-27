# ! /Users/mn/.pyenv/shims/python
# ! -*- coding:utf-8 -*-

import linecache
import logging
log = logging.getLogger(__name__)


class Log(object):
    """
    output
    """

    def __init__(self, directory):
        self.directory = directory

    def get_line(self):
        """
        get line
        """
        logname = "/Users/work/futaba/FutaWatcher/log/" + self.directory
        log.info(logname)
        num_lines = sum(1 for line in open(logname))
        line = linecache.getline(logname, (int(num_lines))).rstrip()
        linecache.clearcache()
        log.info(line)
        return line
