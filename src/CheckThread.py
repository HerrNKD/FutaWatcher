# ! /Users/mn/.pyenv/shims/python
# ! -*- coding:utf-8 -*-

import urllib
import logging
from DecException import exception5

# Threadに何も入っていない
# ->まだ探していない、探しても見つからなかった
# ThreadにUrlが入っている
# 　そのUrlでスレッドが見れた-> すでに見つかっている = 終了
# 　スレッドが存在しなかった-> サーチ開始
# #######
# ・Thread変数は状態遷移する
#   中身がUrl : 中身がNone
# initはNone
# Logはurlを参照する
# ->時間をいちいちおわなくていい
#

log = logging.getLogger(__name__)


@exception5("first")
def first(Thread):
    log.info(Thread)
    if Thread == "None":  # LogにThreadのURLが見つからなかったとき
        log.info("Start Search Thread")
        return 0
    Open = urllib.request.urlopen(Thread)
    if Open is True:  # LogにThreadのURLが見つかったとき
        log.info("Thread is already searched.")
        print(Thread)
        return 1


def finish(Thread):
    if Thread is "None":  # Threadが探しても見つからなかったとき
        log.info("There is no thread in Catalog.")
        log.info(Thread)
        # print(Thread)
    else:  # Threadを探して見つかったとき
        log.info("Get Thread")
        log.info(Thread)
        # print(Thread)
