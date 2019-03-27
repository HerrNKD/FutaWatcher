# ! /Users/mn/.pyenv/shims/python
# ! -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import os
import webbrowser
import Line
import Output


class Thread(object):
    """
    Thread
    """

    def __init__(self, thread):
        self.thread = thread

    def get_thread(self):
        """
        get thread
        """

        print(self.thread)
        print("=====body=====\n\n")
        seed = requests.get(self.thread)
        soup = BeautifulSoup(seed.content, "html.parser")
        # body = soup.find_all("span")
        body = soup.find_all("span", class_="cntd")
        print(body)
        # del body[0:4]
        # body.pop()
        # body.pop()
        # body.pop()
        print("-----after body -----\n\n")
        print(body)
        end = body[0].text
        end = end.replace(u"頃消えます", "")
        if len(end) > 5:
            end = end[(len(end)-5):]
        gabage = '"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" %s'
        browser = webbrowser.get(gabage)
        browser.open(self.thread)
        noti = "'display notification "" with title \"Get Deresute Thread!!!\"'"
        os.system("osascript -e" + noti)
        Line(self.thread).notify_line()
        Output("g", end, "Get Thread!!!").call_result()
