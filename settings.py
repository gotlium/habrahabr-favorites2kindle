DEBUG = False

# Favorite page
USER = 'USERNAME'
HABRAHABR_USER_FAV = {
    'geektimes': 'http://geektimes.ru/users/%s/favorites/',
    'habrahabr': 'http://habrahabr.ru/users/%s/favorites/',
    'megamozg': 'http://megamozg.ru/users/%s/favorites/',
}

# Chrome extension emulation data
COOKIES = {
    'csrftoken': "",
    'readabilityToken': "",
    'kindleUserDetails': "",
    'production': "",
    '_ga': ""
}
'''
Cookies example:
COOKIES = {
    'csrftoken': '1CULFlW3by7I7diVXP0XlIG8lzuMpyEY',
    'kindleUserDetails': '%7B%22username%22%3A%20%22My-Kindle-Email%22%2C%20%22domain%22%3A%20%22kindle.com%22%7D',
    'production': '4b1b2fe3108ad4756e0d783bfd952f19',
    'readabilityToken': 'h5ATqD7d2w49L5NueapwB9s45gh3sUvbzWAU',
    '_ga': 'GA1.2.1287105590.1381711368'
}
'''

KINDLE_URL = "http://www.readability.com/api/session/v1/kindle/send/"
# BOOKMARKS_URL = "http://www.readability.com/api/session/v1/bookmarks/"

USER_AGENT = "ReadabilityChrome/3.0.15 Mozilla/5.0 (Macintosh; " \
             "Intel Mac OS X 10_9_5) AppleWebKit/537.36 " \
             "(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"

try:
    from local_settings import *
except ImportError:
    pass
