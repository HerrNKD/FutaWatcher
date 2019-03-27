# ! /Users/mn/.pyenv/shims/python
# ! -*- coding:utf-8 -*-

import urllib
import Output
from bs4 import BeautifulSoup


class GetHTML(object):
    """
    GetHTML
    """

    def __init__(self, url, attr, tag):
        self.url = url
        self.attr = attr
        self.tag = tag

    def Get_links(self):
        """
        Get_links
        """
        counter = 0
        while True:
            try:
                html = urllib.request.urlopen(self.url)
                html.read().decode('utf-8', 'ignore')
            except Exception as _e:
                counter += 1
                if counter <= 5:
                    print("retry urlopen in GetLinks...")
                    continue
                if counter >= 5:
                    print(_e)
                    Output(_e, 0, "Error in GetLinks").call_result()
            else:
                counter = 0
                break
        soup = BeautifulSoup(html, "html.parser")
        return [a.get(self.attr) for a in soup.find_all(self.tag)]
