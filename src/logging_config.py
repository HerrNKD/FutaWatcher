# ! /Users/mn/.pyenv/shims/python
# ! -*- coding:utf-8 -*-

import sys
import logging
import logging.handlers
import logging.config

log = logging.getLogger(__name__)


def run(logfile):
    _root_logger = logging.getLogger('')
    _root_logger.setLevel(logging.DEBUG)

    _Formatter = logging.Formatter(
        fmt='%(asctime)s %(levelname)-8s %(module)-18s\
             %(funcName)-10s %(lineno)4s: %(message)s'
    )

    _consoleHandler = logging.StreamHandler(sys.stdout)
    _consoleHandler.setLevel(logging.DEBUG)
    _consoleHandler.setFormatter(_Formatter)
    _root_logger.addHandler(_consoleHandler)

    _fileHandler = logging.handlers.RotatingFileHandler(
        filename='../log/' + logfile,
        maxBytes=100000, backupCount=3,
        encoding='utf-8'
    )
    _fileHandler.setLevel(logging.INFO)
    _fileHandler.setFormatter(_Formatter)
    _root_logger.addHandler(_fileHandler)


def change_handler(logfile, _log):
    log.info("change")
    for hdlr in _log.handlers[:]:
        log.info(hdlr)
        _log.removeHandler(hdlr)
    _newfileHandler = logging.handlers.RotatingFileHandler(
        filename='../log/' + logfile,
        maxBytes=100000, backupCount=3,
        encoding='utf-8'
    )
    _log.addHandler(_newfileHandler)
