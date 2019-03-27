# ! /Users/mn/.pyenv/shims/python
# ! -*- coding:utf-8 -*-

import logging
from GetCatalogImages import GetCatalogImages
from TempleteMatching import TempleteMatching

log = logging.getLogger(__name__)


class ServerUI(object):
    """
    プログラムの大元.
    cronでこいつが呼ばれる.
    """
    def __init__(self, logfile, image):
        self.logfile = logfile
        self.image = image

    def SearchThread(self):
        """
        Search Thread
        """
        # log.debug("test")
        log.info(self.logfile + " : " + self.image)
        Catalog = GetCatalogImages().get_catalog()
        TM = TempleteMatching(Catalog, self.image)
        return TM.judge_matching()
