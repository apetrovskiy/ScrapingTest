from scrapy import Spider, Request


class QuotesSpider3(Spider):
    name = "quotes3"

    '''
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield Request(url=url, callback=self.parse)
    '''
    start_urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]

    def parse(self, response):
        filename = self.get_file_name(response)
        self.write_to_file(filename, response.body)
        self.write_to_log(filename)

    def get_file_name(self, response):
        page = response.url.split("/")[-2]
        print("==============================================")
        print(response.url)
        print(page)
        filename = 'quotes-%s.html' % page
        return filename

    def write_to_log(self, filename):
        self.log('Saved file %s' % filename)

    def write_to_file(self, filename, text):
        with open(filename, 'wb') as f:
            f.write(text)
