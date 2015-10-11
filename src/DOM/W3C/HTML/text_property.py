#!/usr/bin/env python

import bs4 as BeautifulSoup

import logging

from DOM import dom_logging

def text_property(readonly = False, tag = None):
    def getter(self):
        return str(self.tag.string) if self.tag.string else "" 
    
    def setter(self, text):
        if tag == 'innerHTML':
            dom_logging(log, "set innerHTML to", text)
        #if self.tag.string:
        #    self.tag.contents[0] = BeautifulSoup.NavigableString(text)
        #else:
        #   self.tag.append(text)
        #
        #self.tag.string = self.tag.contents[0]
        self.tag.string = text
        
    return property(getter) if readonly else property(getter, setter)

