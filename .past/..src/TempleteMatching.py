# ! /Users/mn/.pyenv/shims/python
# ! -*- coding:utf-8 -*-

import cv2
import os
import Image
import TimeGetter
import Thread


class TempleteMatching(object):
    """
    TempleteMatching
    """
    def __init__(self, m_urls):
        self.m_urls = m_urls

    def judge_matching(self):
        """
        judge
        0.78 = magick number
        """
        # テンプレート
        # 入力画像とテンプレート画像を取得
        temp = cv2.imread("/Users/work/futaba/slstage/.seed/s.png")
        # temp = cv2.imread("/Users/work/futaba/slstage/.seed/test.png")
        temp2 = cv2.imread("/Users/work/futaba/slstage/.seed/n-tar.png")

        # グレースケール変換
        temp = cv2.cvtColor(temp, cv2.COLOR_RGB2GRAY)
        temp2 = cv2.cvtColor(temp2, cv2.COLOR_RGB2GRAY)

        # テンプレート画像の高さ・幅
        height, width = temp.shape
        height2, width2 = temp2.shape

        Image(self.m_urls).refresh_image()
        for i, m_url in enumerate(self.m_urls):
            name = m_url[1].replace("http://img.2chan.net/b/src/",
                                    "/Users/work/futaba/slstage/.result/")

            print("m_url[0] =", m_url[0])
            print("m_url[1] =", m_url[1])
            print("name     =", name)

            imag = cv2.imread(name)
            # Resize image
            image = cv2.resize(imag, (400, 400), interpolation=cv2.INTER_AREA)
            # グレースケール変換
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            # テンプレートマッチング
            match = cv2.matchTemplate(gray, temp, cv2.TM_CCOEFF_NORMED)
            match2 = cv2.matchTemplate(gray, temp2, cv2.TM_CCOEFF_NORMED)
            min_value, max_value, min_pt, max_pt = cv2.minMaxLoc(match)
            min_value2, max_value2, min_pt2, max_pt2 = cv2.minMaxLoc(match2)
            point = max_pt
            point2 = max_pt2
            # print("[{:2d}] s={:.5f}, tar={:>.5f}".format(i, max_value,
            #                                                max_value2) )
            if max_value >= 0.78:
                print(name, end="")
                print(" = {:.5f}".format(max_value))
                os.chdir("/Users/work/futaba/slstage/.icons/")
                # テンプレートマッチングの結果を出力
                cv2.rectangle(image, (point[0], point[1]),
                              (point[0]+width, point[1]+height),
                              (0, 0, 200), 3)
                cv2.imwrite(str(TimeGetter().get_now_time()) + ".png", imag)
                Thread(m_url[0]).get_thread()
                break
            if max_value2 >= 0.78:
                print(name, end="")
                print(" = {:.5f}".format(max_value2))
                os.chdir("/Users/work/futaba/slstage/.icons/")
                # テンプレートマッチングの結果を出力
                cv2.rectangle(image, (point2[0], point2[1]),
                              (point2[0]+width2, point2[1]+height2),
                              (0, 0, 200), 3)
                cv2.imwrite(str(TimeGetter().get_now_time()) + ".png", imag)
                Thread(m_url[0]).get_thread()
                break
