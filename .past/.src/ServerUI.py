# ! /Users/mn/.pyenv/shims/python
# ! -*- coding:utf-8 -*-

import os
from OutputLogTime import OutputLogTime
from GetCatalogImages import GetCatalogImages
from TempleteMatching import TempleteMatching


class ServerUI(object):
    """
    プログラムの大元.
    cronでこいつが呼ばれる.
    """
    def __init__(self):
        pass

    def SearchThread(self):
        """
        Search Thread
        """

        catalog = GetCatalogImages()
        catalog.get_catalog()
        print(catalog)
        TM = TempleteMatching(catalog)
        TM.judge_matching()
        print(TM)


if __name__ == '__main__':
    os.chdir("/Users/work/futaba/slstage/.result")
    START = OutputLogTime().get_now_time()
    OutputLogTime().check_log()
    Server = ServerUI()
    Server.SearchThread()
    OutputLogTime().call_result("n", START, "There is no thread.")
