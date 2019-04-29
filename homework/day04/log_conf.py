#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       log_conf.py
#    Description :
#    Author :          SanYapeng
#    date：            2019-04-24
#    Change Activity: import logging, logging.config
import os
import logging, logging.config
log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),"conf/loging.conf")
logging.config.fileConfig(log_file)
logger = logging.getLogger("base")