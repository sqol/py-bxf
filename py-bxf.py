#! /usr/bin/python

################################################################################
## 	py-bxf
##  py-bxf.py                                      
##  Python BXF implementation
##
##  sqol 30-dec-2016
################################################################################

import sys
import logging
import time
import pprint

## logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("py-bxf started, " + time.strftime("%c"))