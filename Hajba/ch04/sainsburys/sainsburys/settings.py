# -*- coding: utf-8 -*-

BOT_NAME = 'sainsburys'

SPIDER_MODULES = ['sainsburys.spiders']
NEWSPIDER_MODULE = 'sainsburys.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'

ROBOTSTXT_OBEY = True

CONCURRENT_REQUESTS = 1
