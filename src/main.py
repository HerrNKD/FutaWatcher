# ! /Users/mn/.pyenv/shims/python
# ! -*- coding:utf-8 -*-

import os
import logging_config
import logging
from CheckThread import first
from CheckThread import finish
from Log import Log
from ServerUI import ServerUI

logging_config.run("main.log")
log = logging.getLogger(__name__)

if __name__ == "__main__":
    os.chdir("/Users/work/futaba/FutaWatcher/.result")
    Dict = {"slstage.log": "s.png",
            "Imgtoon.log": "ink.png"}
    # "DJ_dra.log": "dra.png",
    # "Metron.log": "metron.png"

    for logfile, image in Dict.items():
        logging_config.change_handler(logfile, log)
        Thread = Log(logfile).get_line()
        log.info(logfile)
        log.info(log.handlers)
        log.info(Thread)
        if first(Thread) == 1:
            continue
        Server = ServerUI(logfile, image)
        Thread = Server.SearchThread()
        log.info(Thread)
        finish(Thread)
