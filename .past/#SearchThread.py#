# ! /Users/mn/.pyenv/shims/python
# ! -*- coding:utf-8 -*-

import os
import TimeGetter
import LogChecker
import FUTABA
import TempleteMatching
import Output


def SearchThread():
    """
    main関数.
    """
    os.chdir("/Users/work/futaba/slstage/.result")
    START = TimeGetter().get_now_time()
    LogChecker().check_log()

    img = FUTABA()
    thread = img.get_thread_URL()
    thumbnail = img.get_thumbnail_URL(thread)
    catalog = img.get_catalog(thumbnail)
    TempleteMatching(catalog).judge_matching()

    Output("n", START, "There is no thread.").call_result()

if __name__ == '__main__':
    SearchThread()
