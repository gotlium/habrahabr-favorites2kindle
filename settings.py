DEBUG = False

# Favorite page
HABRAHABR_USER_FAV = "http://habrahabr.ru/users/USERNAME/favorites/"

# Chrome extension emulation data
COOKIES = {
    'csrftoken': "",
    'kindleUserDetails': "",
    'production': "",
    '_ga': ""
}
KINDLE_URL = "http://www.readability.com/api/session/v1/kindle/send/"
# BOOKMARKS_URL = "http://www.readability.com/api/session/v1/bookmarks/"

USER_AGENT = "ReadabilityChrome/3.0.15 Mozilla/5.0 (Macintosh; " \
             "Intel Mac OS X 10_9_5) AppleWebKit/537.36 " \
             "(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"

try:
    from local_settings import *
except ImportError:
    pass
