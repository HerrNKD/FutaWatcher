# ! /Users/mn/.pyenv/shims/python
# ! -*- coding:utf-8 -*-

import cv2
import os
import webbrowser
import subprocess
import requests
import logging
from datetime import datetime
from DecException import exception5

log = logging.getLogger(__name__)

# ################################################################# #
# ### method ###
# ##############


def notify_line(url):
    """
    line
    """
    line_notify_token = "vMB3CFS4U2HYidLFk3J5zDMDfe8M62Fu00jkT5IKiWX"
    line_notify_api = "https://notify-api.line.me/api/notify"
    message = "URL: "

    payload = {"message": message, "message": url}
    headers = {"Authorization": "Bearer " + line_notify_token}
    requests.post(line_notify_api, data=payload, headers=headers)


def get_now_time():
    """
    get now time
    """
    now_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return datetime.strptime(now_string, "%Y-%m-%d %H:%M:%S")


def get_thread(thread):
    """
    get thread
    """
    app = '"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" %s'
    browser = webbrowser.get(app)
    browser.open(thread)
    noti = "'display notification "" with title \"Get Deresute Thread!!!\"'"
    os.system("osascript -e" + noti)
    notify_line(thread)


def refresh_image(urls):
    """
    refresh image
    """
    command = "/usr/local/Cellar/imagemagick/7.0.8-8/bin/convert"

    for url in urls:
        image = url[1].replace("http://img.2chan.net/b/src/",
                               "/Users/work/futaba/FutaWatcher/.result/")
        # (wish) 切り替えるようClient側から維持れるようにする.

        if image.endswith(".png") is True:
            subprocess.run((command, "-quiet", image, "-strip", image))


# ################################################################# #
# ### class ###
# #############
class TempleteMatching(object):
    """
    TempleteMatching
    """
    def __init__(self, m_urls, image):
        self.m_urls = m_urls
        self.image = image

    @exception5("judge_matching")
    def judge_matching(self):
        """
        judge
        0.78 = magick number
        """
        # テンプレート
        # 入力画像とテンプレート画像を取得
        log.info("/Users/work/futaba/FutaWatcher/.seed/" + self.image)
        temp = cv2.imread("/Users/work/futaba/FutaWatcher/.seed/" + self.image)

        # グレースケール変換
        temp = cv2.cvtColor(temp, cv2.COLOR_RGB2GRAY)

        # テンプレート画像の高さ・幅
        height, width = temp.shape

        refresh_image(self.m_urls)

        for i, m_url in enumerate(self.m_urls):
            name = m_url[1].replace("http://img.2chan.net/b/src/",
                                    "/Users/work/futaba/FutaWatcher/.result/")
            # print("m_url[0] =", m_url[0])
            # print("m_url[1] =", m_url[1])
            # print("name     =", name)
            imag = cv2.imread(name)
            # Resize image
            image = cv2.resize(imag, (400, 400), interpolation=cv2.INTER_AREA)
            # グレースケール変換
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            # テンプレートマッチング
            match = cv2.matchTemplate(gray, temp, cv2.TM_CCOEFF_NORMED)
            min_value, max_value, min_pt, max_pt = cv2.minMaxLoc(match)
            point = max_pt
            if max_value >= 0.78:
                print(name, end="")
                print(" = {:.5f}".format(max_value))
                os.chdir("/Users/work/futaba/FutaWatcher/icons/")
                # テンプレートマッチングの結果を出力
                cv2.rectangle(image, (point[0], point[1]),
                              (point[0]+width, point[1]+height),
                              (0, 0, 200), 3)
                cv2.imwrite(str(get_now_time()) + ".png", imag)
                get_thread(m_url[0])
                return m_url[0]

        return "None"
