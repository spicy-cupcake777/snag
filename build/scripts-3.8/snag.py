#!/data/data/com.termux/files/usr/bin/python

from requests import get
from bs4 import BeautifulSoup

_URL = ''
_SOUP = None

def set_soup(url):
    _URL = url
    source = get(url).content
    _SOUP = BeautifulSoup(source)

def S(pattern):
    if pattern.startswith('.'):
        return _SOUP.find_all(class_=pattern[1:]))
