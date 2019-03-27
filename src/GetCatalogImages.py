# ! /Users/mn/.pyenv/shims/python
# ! -*- coding:utf-8 -*-

import urllib
import os
from bs4 import BeautifulSoup
import logging
from DecException import exception5

log = logging.getLogger(__name__)


class GetCatalogImages(object):
    """
    get catalog url,
    get catalog html source,
    get thread url,
    get thread html source,
    get thread-thumbnail image
    """

    # class var "
    url_catalog = "http://img.2chan.net/b/futaba.php?mode=cat&sort=1"
    # (wish) urlはClientServer側で指名されるべき.

    # constructor "
    def __init__(self):
        pass

    @exception5("Get Html")
    def get_html(self, url, attr, tag):
        """
        get html source
        """
        html = urllib.request.urlopen(url)
        html = html.read().decode('utf-8', 'ignore')
        soup = BeautifulSoup(html, "html.parser")
        return [a.get(attr) for a in soup.find_all(tag)]

    def get_thread_URL(self):
        """
        get thread urls
        """
        thread_links = self.get_html(self.url_catalog, "href", "a")
        for link in thread_links[:]:
            if "res" not in link:
                thread_links.remove(link)
        return thread_links

    def get_thumbnail_URL(self):
        """
        get thumbnail urls
        """
        thread_links = self.get_thread_URL()
        t_url = []
        for link in thread_links[:]:
            link = "http://img.2chan.net/b/" + link
            thumbnail_links = self.get_html(link, "href", "a")
            for i in thumbnail_links[:]:
                if "jpg" not in i:
                    if "png" not in i:
                        thumbnail_links.remove(i)
            for idx, thumbnail in enumerate(thumbnail_links):
                if len(thumbnail_links) != 0:
                    tpl = (link, "http://img.2chan.net" + thumbnail_links[0])
                    t_url.insert(idx, tpl)

        return t_url

    @exception5("Get Catalog")
    def get_catalog(self):
        """
        get catalog images
        """
        t_url = self.get_thumbnail_URL()
        c_urls = t_url[0::2]
        for idx, k_url in enumerate(c_urls):
            getimg = urllib.request.urlopen(c_urls[idx][1])
            localfile = open(os.path.basename(c_urls[idx][1]), 'wb')
            localfile.write(getimg.read())
            getimg.close()
            localfile.close()

        log.info("success")

        return c_urls
