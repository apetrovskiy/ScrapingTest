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
    #Rule(LinkExtractor(allow='.*'),
    #    callback='probe', follow=True)

    def parse(self, response):
        return self.parse_extract(response)

    def get_request(self, response, url):
        print("===========get_request PROD================")
        print("url: %s" % response.url)
        return response

    def parse_extract(self, response):
        print("========================PROD parse======================")
        print("response: %s" % response)
        print("url: %s" % response.url)
        response = self.get_request(response, response.url)
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.xpath('//span/small/text()').get(),
            }
        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(self.URL + next_page, self.parse_extract)
            # yield self.get_response(response, self.URL + nex#_page)

            #url = self.URL + next_page
            #yield self.get_request(response, url)

            #yield QuotesSpider2.get_request(response=response, url=url)
            #for resp in response:
            #    yield QuotesSpider2.get_request(response=resp, url=url)
