# ! /Users/mn/.pyenv/shims/python
# ! -*- coding:utf-8 -*-

import requests


class Line(object):
    """
    line
    """
    def __init__(self, l_url):
        self.l_url = l_url

    def notify_line(self):
        """
        line
        """
        line_notify_token = "vMB3CFS4U2HYidLFk3J5zDMDfe8M62Fu00jkT5IKiWX"
        line_notify_api = "https://notify-api.line.me/api/notify"
        message = "URL: "

        payload = {"message": message, "message": self.l_url}
        headers = {"Authorization": "Bearer " + line_notify_token}
        requests.post(line_notify_api, data=payload, headers=headers)
