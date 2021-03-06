#!/usr/bin/env python
# -*- coding: utf-8 -*-

import optparse
import logging
import shelve
import time
import os

import grab
import settings


PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
LOG_FILE = os.path.join(PROJECT_PATH, 'habrahabr-favorites2kindle.log')
DB_FILE = os.path.join(PROJECT_PATH, 'db.shelve')

logger = logging.getLogger('habrahabr-favorites2kindle')
handler = logging.FileHandler(LOG_FILE)
if settings.DEBUG is True:
    handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

NEXT_PAGE_PATH = '//a[@id="next_page"]/@href'
PREVIOUS_PAGE_PATH = '//a[@id="previous_page"]/@href'
END_PAGE_PATH = u'//a[@title="Последняя страница"]/@href'
POSTS_URL_PATH = '//h1[@class="title"]/a[contains(@href, "/post/") or contains(@href, "/blog/")]/@href'


class HabrahabrFav2Kindle(object):
    def __init__(self):
        self.page = 1
        self.grab = grab.Grab()
        self.grab.setup(
            connect_timeout=5,
            timeout=5,
            hammer_mode=True,
            hammer_timeouts=((60, 70), (80, 90), (100, 110), (110, 120))
        )
        self.db = shelve.open(DB_FILE)
        self.arg = self.get_arguments()

    @staticmethod
    def get_arguments():
        parser = optparse.OptionParser()
        parser.add_option(
            "--gt", dest="geektimes", action="store_true", default=False)
        parser.add_option(
            "--mm", dest="megamozg", action="store_true", default=False)
        parser.add_option(
            "--reverse", dest="reverse", action="store_true", default=False)
        parser.add_option(
            "--page-limit", dest="limit", action="store", default=None)
        parser.add_option(
            "--username", dest="user", action="store", default=settings.USER)
        return parser.parse_args()[0]

    def get_page(self, url):
        self.grab.go(url)
        if self.grab.response.code != 200:
            logger.fatal("Site return http code %d" % self.grab.response.code)

    def get_next_page(self):
        next_page = self.grab.doc.select(NEXT_PAGE_PATH)
        if next_page.exists():
            return next_page.text()

    def get_previous_page(self):
        previous_page = self.grab.doc.select(PREVIOUS_PAGE_PATH)
        if previous_page.exists():
            return previous_page.text()

    def get_end_page(self):
        end_page = self.grab.doc.select(END_PAGE_PATH)
        if end_page.exists():
            return end_page.text()

    def get_posts(self):
        posts_urls = self.grab.doc.select(POSTS_URL_PATH)
        urls = []
        if posts_urls.exists():
            for url in posts_urls:
                urls.append(url.text())
        return urls

    def make_readability_request(self, post_url):
        logger.debug('Send: %s' % post_url)
        grab_lib = self.grab.clone()
        grab_lib.go(
            settings.KINDLE_URL, post=dict(url=post_url),
            cookies=settings.COOKIES, headers={
                'X-CSRFToken': settings.COOKIES['csrftoken']
            }, user_agent=settings.USER_AGENT
        )
        return grab_lib.response.code, grab_lib.response.body

    def send2kindle(self, post_url):
        if not self.db.get(post_url):
            code, body = self.make_readability_request(post_url)
            if code == 202:
                logger.debug("Sent: %s" % post_url)
                self.db[post_url] = True
                time.sleep(1)
                return
            logger.error("Error: %s" % body)
        else:
            logger.debug('Skip: %s' % post_url)

    def process_posts(self, url):
        logger.debug('Processing: %s' % url)
        logger.debug('')
        self.get_page(url)
        for post_url in self.get_posts():
            self.send2kindle(post_url)
            logger.debug('')

    def get_start_page(self, key):
        url = settings.HABRAHABR_USER_FAV.get(key) % self.arg.user
        if self.arg.reverse is True:
            self.get_page(url)
            url = self.get_end_page()
        return url

    def get_fav_url(self, key='habrahabr'):
        if self.arg.megamozg:
            key = 'megamozg'
        if self.arg.geektimes:
            key = 'geektimes'
        return self.get_start_page(key)

    def _get_next_page(self):
        if self.arg.reverse is True:
            return self.get_previous_page()
        return self.get_next_page()

    def run(self):
        logger.debug('Starting')
        logger.debug('Project path is %s' % PROJECT_PATH)

        self.process_posts(self.get_fav_url())

        while self._get_next_page():
            if self.arg.limit and int(self.arg.limit) == self.page:
                break
            self.process_posts(self._get_next_page())
            self.page += 1

        self.db.close()

    def __del__(self):
        self.db.close()


if __name__ == '__main__':
    HabrahabrFav2Kindle().run()
