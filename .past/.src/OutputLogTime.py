# ! /Users/mn/.pyenv/shims/python
# ! -*- coding:utf-8 -*-

import shutil
import os
import sys
import linecache
from datetime import datetime, timedelta
from DecException import exception


class OutputLogTime(object):
    """
    output
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
        log = "/Users/work/futaba/FutaWatcher/output.txt"
        # 変えられるようにするべき
        num_lines = sum(1 for line in open(log))
        line = linecache.getline(log, (int(num_lines)-1)).rstrip()
        linecache.clearcache()
        return line

    @exception("GetLogTime")
    def get_log_time(self):
        """
        get log time
        """
        finish_string = datetime.now().strftime("%Y-%m-%d ")
        log_line = self.get_line()
        finish_line = finish_string + log_line
        finish = datetime.strptime(finish_line, "%Y-%m-%d %H:%M")
        return finish

    # @exception("Thread has already been searched.")
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
            Output().call_result("a", 0, "Thread has already been searched.")

    def call_result(self, _e, num, select):
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
        print("***** << " + select + " >> *****")
        if (_e != "a") and (_e != "n") and (_e != "g"):
            print(_e)
            print("00:00")
            print("*****", end="")
            print(self.get_now_time())
        if _e == "a":
            print(self.get_line())
            print("*****", end="")
            print(self.get_now_time())
        if _e == "n":
            print("00:00")
            print("*****", end="")
            print(self.get_now_time(), end="")
            print(", delta = " + str(self.get_now_time() - num))
        if _e == "g":
            print(num)
            print("*****", end="")
            print(self.get_now_time())
        shutil.rmtree('/Users/work/futaba/FutaWatcher/.result/')
        os.mkdir("/Users/work/futaba/FutaWatcher/.result")
        sys.exit(0)
