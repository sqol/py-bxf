#! /usr/bin/python

################################################################################
## 	py-bxf
##  py-bxf.py                                      
##  Python BXF implementation
##
##  sqol 30-dec-2016
################################################################################

## todo
# - watch folder, configurable read time, check for file completion
# - socket read/write
# - entries into database
# - ack/nack

import sys
import logging
import time
import pprint

#from bs4 import BeautifulSoup
from urllib import urlopen
import sqlite3
import xml.etree.ElementTree as ET

## variable holding pen
HandlerName = "pybxf"
BXFWatchDir = "C:/temp/bxf/input/"
BXFOutputDir = "C:/temp/bxf/output/"
BXFErrorDir = "C:/temp/bxf/error/"
BXFFileExt = ".bxf"


## logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("py-bxf started, " + time.strftime("%c"))

tree = ET.parse(BXFWatchDir + 'TransferRequestComplete' + BXFFileExt)
root = tree.getroot()
print "BxfMessageId: %s" % root.attrib['id'].strip("urn:uuid:")
print "Origin: %s" % root.attrib['origin']
print "Destination: %s" % root.attrib['destination']
print "MessageType1: %s" % root.attrib['messageType']
print "MessageType2: %s" % root[0][0].tag.split('}', 1)[-1] # remove the schema location from front