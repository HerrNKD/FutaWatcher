# ! /Users/mn/.pyenv/shims/python
# ! -*- coding:utf-8 -*-

import shutil
import os
import sys
import linecache
from datetime import datetime, timedelta


class OutputLogTime(object):
    """
    output
    """

    def __init__(self, _e, num, select):
        self._e = _e
        self.num = num
        self.select = select

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
            self(_e, 0, "Error in GetLogTime").call_result()

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
            self("a", 0, "Thread has already been searched.").call_result()

    def call_result(self):
        """
        call_result
        実行結果によってselectが変わり、出力するログが変わる。
        a = すでに取得済みの場合
        n = スレッドが存在しなかった場合
        g = スレッドが見つかった場合
        それ以外
        の４つ.
        実行後、.resultフォルダをクリーンしてプログラムを終了する.
        """
        print("***** << " + self.select + " >> *****")
        if (self._e != "a") and (self._e != "n") and (self._e != "g"):
            print(self._e)
            print("00:00")
            print("*****", end="")
            print(self.get_now_time())
        if self._e == "a":
            print(self.get_line())
            print("*****", end="")
            print(self.get_now_time())
        if self._e == "n":
            print("00:00")
            print("*****", end="")
            print(self.get_now_time(), end="")
            print(", delta = " + str(self.get_now_time() - self.num))
        if self._e == "g":
            print(self.num)
            print("*****", end="")
            print(self.get_now_time())
        shutil.rmtree('/Users/work/futaba/FutaWatcher/.result/')
        os.mkdir("/Users/work/futaba/FutaWatcher/.result")
        sys.exit(0)
