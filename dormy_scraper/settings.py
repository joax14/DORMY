# Scrapy settings for dormy_scraper project

BOT_NAME = 'dormy_scraper'

SPIDER_MODULES = ['dormy_scraper.spiders']
NEWSPIDER_MODULE = 'dormy_scraper.spiders'

# Remove Splash settings
# SPLASH_URL = 'http://localhost:8050'

# Remove Scrapy-Splash settings
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy_splash.SplashCookiesMiddleware': 723,
#     'scrapy_splash.SplashMiddleware': 725,
#     'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware': 100,
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
# }

# Remove Splash middleware
# SPIDER_MIDDLEWARES = {
#     'scrapy_splash.SplashDeduplicationMiddleware': 100,
# }

# Remove Splash dupe filter
# DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

# Remove Splash headers if added
# DEFAULT_REQUEST_HEADERS = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Language': 'en',
# }

# Enable cookies
COOKIES_ENABLED = True

# Optional: Configure delay if needed
# DOWNLOAD_DELAY = 2
