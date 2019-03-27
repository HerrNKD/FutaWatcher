# ! /Users/mn/.pyenv/shims/python
# ! -*- coding:utf-8 -*-

import TimeGetter
import LogChecker
import shutil
import os
import sys


class Output(object):
    """
    output
    """

    def __init__(self, _e, num, select):
        self._e = _e
        self.num = num
        self.select = select

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
            print(TimeGetter().get_now_time())
        if self._e == "a":
            print(LogChecker().get_line())
            print("*****", end="")
            print(TimeGetter().get_now_time())
        if self._e == "n":
            print("00:00")
            print("*****", end="")
            print(TimeGetter().get_now_time(), end="")
            print(", delta = " + str(TimeGetter().get_now_time() - self.num))
        if self._e == "g":
            print(self.num)
            print("*****", end="")
            print(TimeGetter().get_now_time())
        shutil.rmtree('/Users/work/futaba/slstage/.result/')
        os.mkdir("/Users/work/futaba/slstage/.result")
        sys.exit(0)
