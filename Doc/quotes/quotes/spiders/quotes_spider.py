from scrapy import Spider

# URL = 'http://quotes.toscrape.com'
START_PAGE = '/tag/humor/'


class QuotesSpider(Spider):
    name = 'quotes'
    URL = 'http://quotes.toscrape.com'
    start_urls = [
        URL + START_PAGE,
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.xpath('//span/small/text()').get(),
            }
        print("============= next page =================")
        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            print("============= next page is not None ===========")
            print(self.URL + next_page)
            yield response.follow(self.URL + next_page, self.parse)
