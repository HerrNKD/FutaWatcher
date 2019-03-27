# ! /Users/mn/.pyenv/shims/python
# ! -*- coding:utf-8 -*-

import subprocess


class Image(object):
    """
    Image
    """

    def __init__(self, i_urls):
        self.i_urls = i_urls

    def refresh_image(self):
        """
        refresh image
        """
        command = "/usr/local/Cellar/imagemagick/7.0.8-8/bin/convert"
        for i_url in self.i_urls:
            image = i_url[1].replace("http://img.2chan.net/b/src/",
                                     "/Users/work/futaba/slstage/.result/")
            if image.endswith(".png") is True:
                subprocess.run((command, "-quiet", image, "-strip", image))
