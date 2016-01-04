'''
Created on Dec 2, 2015

@author: Yamaan
'''
import urllib.request
from html.parser import HTMLParser
thisurl = "http://aljazeera.com/"

handle = urllib.request.urlopen(thisurl)

html_gunk = handle.read()

print(html_gunk)


'''

this is a git test

'''


