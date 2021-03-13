import scrapy
# from scrapy import Request


class BasicSpider(scrapy.Spider):
    name = 'basic'
    # allowed_domains = [
    #     'https://www.sainsburys.co.uk/shop/gb/groceries/meat-fish']
    allowed_domains = ['www.sainsburys.co.uk']
    start_urls = ['https://www.sainsburys.co.uk/shop/gb/groceries/meat-fish/']

    def parse(self, response):
        # urls = response.xpath(
        #     '//ul[@class="categories departments"]/li/a/@href').extract()
        urls = response.xpath('//ul[@class="categories departments"]/li/a')

        for url in urls:
            # yield Request(url, callback=self.parse_department_pages)
            yield response.follow(url, callback=self.parse_department_pages)
