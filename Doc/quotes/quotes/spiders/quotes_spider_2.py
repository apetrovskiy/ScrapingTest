from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# URL = 'http://quotes.toscrape.com'
START_PAGE = '/tag/humor/'


class QuotesSpider2(CrawlSpider):
    name = 'quotes'
    URL = 'http://quotes.toscrape.com'
    start_urls = [
        URL + START_PAGE,
    ]
    Rule(LinkExtractor(allow='.*'),
         callback='parse', follow=True)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.xpath('//span/small/text()').get(),
            }
        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield self.get_response(response, self.URL + next_page)

    def get_response(self, response, url):
        return response.follow(url)
