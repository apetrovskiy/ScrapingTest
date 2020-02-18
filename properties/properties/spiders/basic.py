# -*- coding: utf-8 -*-
import datetime
import socket
from urllib.parse import urlparse, urljoin
from scrapy import Spider
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
from properties.items import PropertiesItem


class BasicSpider(Spider):
    name = 'basic'
    allowed_domains = ['web']
    start_urls = ['http://localhost:9312/properties/property_000000.html']

    def parse(self, response):
        loader = ItemLoader(item=PropertiesItem(), response=response)

        loader.add_xpath('title', '//*[@itemprop="name"][1]/text()',
                         MapCompose(str.strip, str.title))
        loader.add_xpath('price', '//*[@itemprop="price"][1]/text()',
                         MapCompose(lambda i: i.replace(',', ''), float),
                         re='[.0-9]+')
        loader.add_xpath('description',
                         '//*[@itemprop="description"][1]/text()',
                         MapCompose(str.strip, Join()))
        loader.add_xpath('address', '//*[@itemtype='
                         '"http://schema.org/Place"][1]/text()',
                         MapCompose(str.strip))
        loader.add_xpath('image_urls', '//*[@itemprop="image"][1]/@src',
                         MapCompose(lambda i: urljoin(response.url, i)))

        loader.add_value('url', response.url)
        loader.add_value('project', self.settings.get('BOT_NAME'))
        loader.add_value('spider', self.name)
        loader.add_value('server', socket.gethostname())
        loader.add_value('date', datetime.datetime.now())

        return loader.load_item()
