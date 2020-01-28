#!/usr/bin/env python3

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
