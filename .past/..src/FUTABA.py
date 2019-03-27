# ! /Users/mn/.pyenv/shims/python
# ! -*- coding:utf-8 -*-

import GetHTML
import urllib
import os
import Output


class FUTABA(object):
    """
    futaba
    """

    # class var #
    url_catalog = "http://img.2chan.net/b/futaba.php?mode=cat&sort=1"

    # url_catalog = "https://img.2chan.net/9/futaba.php?mode=cat&sort=1"
    # constructor #
    def __init__(self):
        pass

    def get_thread_URL(self):
        """
        get thread url
        """

        # print "GetThreadURL"
        thread_links = GetHTML(self.url_catalog, "href", "a").get_links()
        for link in thread_links[:]:
            if "res" not in link:
                thread_links.remove(link)
        return thread_links

    def get_thumbnail_URL(self, thread_links):
        """
        get thumbnail url
        """

        # print "GetThumbnailURL"
        t_url = []
        for link in thread_links[:]:
            link = "http://img.2chan.net/b/" + link
            thumbnail_links = GetHTML(link, "href", "a").get_links()
            for i in thumbnail_links[:]:
                if "jpg" not in i:
                    if "png" not in i:
                        thumbnail_links.remove(i)
            for idx, thumbnail in enumerate(thumbnail_links):

                if len(thumbnail_links) != 0:
                    tpl = (link, "http://img.2chan.net" + thumbnail_links[0])
                    t_url.insert(idx, tpl)
        return t_url

    def get_katalog(self, t_url):
        """
        get catalog
        """

        # print "GetKatalog"
        k_urls = t_url[0::2]
        counter = 0
        for idx, k_url in enumerate(k_urls):
            while True:
                try:
                    getimg = urllib.request.urlopen(k_urls[idx][1])
                    localfile = open(os.path.basename(k_urls[idx][1]), 'wb')
                    localfile.write(getimg.read())
                    getimg.close()
                    localfile.close()
                except Exception as _e:
                    counter += 1
                    if counter <= 5:
                        print("retry  urlopen in GetKatalog...")
                        continue
                    if counter >= 5:
                        Output(_e, 0, "Error in GetKatalog").call_result()
                else:
                    counter = 0
                    break
        return k_urls
