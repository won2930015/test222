#-------------------------------------------------------------------------------
# Name:        妯″潡1
# Purpose:
#
# Author:      Administrator
#
# Created:     09-02-2017
# Copyright:   (c) Administrator 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from xml.sax.handler import ContentHandler
from xml.sax import parse
class TestHandler(ContentHandler):
    def startElement(self,name,attrs):

        print(name,attrs.keys())

parse('website.xml',TestHandler())

