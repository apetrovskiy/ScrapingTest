import scrapy


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['https://www.sainsburys.co.uk/shop/gb/groceries/meat-fish']
    start_urls = ['http://https://www.sainsburys.co.uk/shop/gb/groceries/meat-fish/']

    def parse(self, response):
        pass
