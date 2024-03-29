import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    '''
    # v 1
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    '''

    # v 2
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/'
    ]

    def save_file(self, filename: str, body: str):
        with open(filename, 'wb') as f:
            f.write(body)

    # v 1 & 2
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        self.save_file(filename, response.body)
        self.log(f'Saved file {filename}')
