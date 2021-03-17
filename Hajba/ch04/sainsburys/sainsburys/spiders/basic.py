import re
# import scrapy
from scrapy.http import HtmlResponse
from scrapy.spiders import Spider
from sainsburys.items import SainsburysItem


reviews_pattern = re.compile("Reviews \((\d+)\)")
item_code_pattern = re.compile("Item code: (\d+)")


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
        product_grid = response.xpath('//ul[@class="productLister gridView"]')
        if product_grid:
            for product in self.handle_product_listings(response):
                yield product

        pages = response.xpath('//ul[@class="categories shelf"]/li/a')
        if not pages:
            pages = response.xpath('//ul[@class="categories aisles"]/li/a')
        if not pages:
            # here is something fishy
            return

        for url in pages:
            yield response.follow(url, callback=self.parse_department_pages)

    def handle_product_listings(self, response: HtmlResponse):
        urls = response.xpath(
            '//ul[@class="productLister gridView"]//li[@class="gridItem"]//h3/a')
        for url in urls:
            yield response.follow(url, callback=self.parse_product_detail)

        next_page = response.xpath('//ul[@class="pages"]/li[@class="next"]/a')
        if next_page:
            yield response.follow(next_page, callback=self.handle_product_listings)

    def parse_product_detail(self, response: HtmlResponse):
        item = SainsburysItem()
        item['url'] = response.url
        # item['product_name'] = response.xpath('//h1/text()').extract()[0].strip()
        item['product_name'] = "" if response.xpath('//h1/text()').extract() == [] else response.xpath('//h1/text()').extract()[0].strip()
        # product_image = response.urljoin(response.xpath('//div[@id="productImageHolder"]/img/@src').extract()[0])
        # product_image = response.urljoin(response.xpath('//div[@class="pd__left skipto-content"]/img/@src').extract()[0])
        # product_image = response.urljoin(response.xpath('//div[@class="productInfo"]//img/@src').extract()[0])
        item['product_image'] = "" if response.xpath('//div[@class="pd__left skipto-content"]//img/@src').extract() == "" else response.urljoin(response.xpath('//div[@class="pd__left skipto-content"]//img/@src').extract()[0])

        # price_per_unit = response.xpath('//div[@class="pricing"]/p[@class="pricePerUnit"]/text()').extract()[0].strip()
        item['price_per_unit'] = response.xpath(
            '//div[@class="pd__price-wrapper"]//div[@class="pd__cost__total undefined"]/text()').extract()[0].strip()
        # units = response.xpath('//div[@class="pricing"]/span[@class="pricePerUnitUnit"]').extract()
        # units = response.xpath('//div[@class="pricing"]//span[@class="pricePerUnitUnit"]').extract()
        units = response.xpath(
            '//div[@class="pd__price-wrapper"]//span[@class="pd__cost__per-unit"]').extract()
        if units:
            item['unit'] = units[0].strip()

        # ratings = response.xpath('//label[@class="numberOfReviews"]/img/@alt').extract()
        # ratings = response.xpath('//a[@class="numberOfReviews"]/img/@alt').extract()
        ratings = response.xpath('//div[@class="star-rating"]').extract()
        if ratings:
            item['rating'] = ratings[0]
        # reviews = response.xpath('//label[@class="numberOfReviews"]').extract()
        reviews = response.xpath(
            '//a[@class="star-rating-link"]/span[@class="pd__reviews__read"]').extract()
        if reviews:
            reviews = reviews_pattern.findall((reviews[0]))
            if reviews:
                item['product_reviews'] = reviews[0]

        # item_code = item_code_pattern.findall(response.xpath('//p[@class="itemCode"]/text()').extract()[0].strip())[0]
        item['item_code'] = item_code_pattern.findall(response.xpath(
            '//span[@id="productSKU"]/text()').extract()[0].strip())[0]

        nutritions = {}
        # for row in response.xpath('//table[@class="nutritionTable"]/tr'):
        for row in response.xpath('//table[@class="nutritionTable"]//tr'):
            th = row.xpath('./th/text()').extract()
            if not th:
                th = ['Energy kcal']
            td = row.xpath('./td[1]/text()').extract()[0]
            nutritions[th[0]] = td
        item['nutritions'] = nutritions

        item['product_origin'] = ' '.join(response.xpath(
            './/h3[@class="productDataItemHeader" and text()="Country of Origin"]/following-sibling::div[1]/p/text()').extract())

        yield item
