import scrapy
# from scrapy import Request
from scrapy.http import HtmlResponse
from scrapy.spiders import Spider


class BasicSpider(Spider):
    name = 'basic'
    # allowed_domains = [
    #     'https://www.sainsburys.co.uk/shop/gb/groceries/meat-fish']
    allowed_domains = ['www.sainsburys.co.uk']
    start_urls = ['https://www.sainsburys.co.uk/shop/gb/groceries/meat-fish/']

    def parse(self, response: HtmlResponse):
        # urls = response.xpath(
        #     '//ul[@class="categories departments"]/li/a/@href').extract()
        urls = response.xpath('//ul[@class="categories departments"]/li/a')

        for url in urls:
            # yield Request(url, callback=self.parse_department_pages)
            yield response.follow(url, callback=self.parse_department_pages)

    def parse_department_pages(self, response: HtmlResponse):
        # product_grid = response.xpath('//ul[@class="productLister gridView"]')
        # if product_grid:
        #     for product in self.handle_product_listings(response):
        #         yield product

        pages = response.xpath('//ul[@class="categories shelf"]/li/a')
        if not pages:
            pages = response.xpath('//ul[@class="categories iasles"]/li/a')
        if not pages:
            # here is something fishy
            return

        for url in pages:
            yield response.follow(url, callback=self.parse_department_pages)
