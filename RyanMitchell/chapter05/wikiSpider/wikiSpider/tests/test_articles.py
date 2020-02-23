from os import getcwd
from unittest import TestCase, main
from scrapy import Item, Spider
#from scrapy.commands.parse import Command
from scrapy.commands.runspider import Command
from scrapy.loader import ItemLoader
from scrapy.http.headers import Headers
from scrapy.http.response import Request, Response
from scrapy.http.response.text import TextResponse
from scrapy.http.response.html import HtmlResponse
from scrapy.core.scraper import Scraper
from scrapy.crawler import Crawler, CrawlerRunner
#from artworks.items import ArtworksItem
#from artworks.spiders.trial import ArticleSpider, INSUNSH_URL_PART, SUMMERTIME_URL_PART
#from RyanMitchell.chapter05.wikiSpider.\
from wikiSpider.spiders.article import ArticleSpider


from scrapy.spidermiddlewares.offsite import OffsiteMiddleware, URLWarning



from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
from scrapy.http.response.xml import XmlResponse

WIKI_FOLDER_NAME = 'wikiSpider'
TESTS_FOLDER_NAME = 'tests'
TEST_DATA_FOLDER_NAME = 'test_data'
SPIDERS_FOLDER_NAME = 'spiders'
FIRST_HTML_FILE = 'python.mhtml'
SECOND_HTML_FILE = 'func.mhtml'
THIRD_HTML_FILE = 'monty.mhtml'

INSUNSH_HTML_FILE = '/browse/insunsh.html'
SPIDER_NAME = 'wiki_spider_1'
FILE_SYSTEM_PREFIX = 'file://'
SLASHE = '/'


class TestItems(TestCase):
    BROWSE = SLASHE + FIRST_HTML_FILE
    HTML_EXT = '.mhtml'

    @classmethod
    def get_path_to_test_data(cls):
        result = getcwd()
        if WIKI_FOLDER_NAME not in result:
            result += SLASHE + WIKI_FOLDER_NAME + SLASHE + WIKI_FOLDER_NAME
        if WIKI_FOLDER_NAME + SLASHE + WIKI_FOLDER_NAME not in result and WIKI_FOLDER_NAME in result:
            result += SLASHE + WIKI_FOLDER_NAME
        if TESTS_FOLDER_NAME not in result:
            result += SLASHE + TESTS_FOLDER_NAME
        if TEST_DATA_FOLDER_NAME not in result:
            result += SLASHE + TEST_DATA_FOLDER_NAME + SLASHE
        result = FILE_SYSTEM_PREFIX + result
        return result

    @classmethod
    def get_path_to_spider(cls, spider_name):
        result = getcwd()
        if WIKI_FOLDER_NAME not in result:
            result += SLASHE + WIKI_FOLDER_NAME
        if SPIDERS_FOLDER_NAME not in result:
            result += SLASHE + SPIDERS_FOLDER_NAME + SLASHE
        result = FILE_SYSTEM_PREFIX + result + spider_name + '.py'
        return result

    def start_requests(self):
        urls = [
            self.get_path_to_test_data() + FIRST_HTML_FILE,
            self.get_path_to_test_data() + SECOND_HTML_FILE,
            self.get_path_to_test_data() + THIRD_HTML_FILE
        ]
        #reqs = [Request('http://a.com/b.html'), Request('http://b.com/1')]
        #out = list(self.mw.process_spider_output(res, reqs, self.spider))
        '''
        runner = CrawlerRunner(None)
        crawler = runner.create_crawler(ArticleSpider)
        #self.spider = crawler._create_spider(**self._get_spiderargs())
        self.mw = OffsiteMiddleware.from_crawler(crawler)
        self.mw.spider_opened(self.spider)
        responses = [self.mw.process_spider_output(None, [Request(url=url)], self.spider)
                for url in urls]
        print(responses)
        for response in responses:
            for resp in list(response):
                print('===== single response ========')
                print(resp)
                yield self.spider.parse(resp)
        '''
        for url in urls:
            yield self.spider.parse(self.get_response_object(url))

    def setUp(self):
        self.spider = ArticleSpider(name=SPIDER_NAME)
        ArticleSpider.BROWSE = self.BROWSE
        ArticleSpider.HTML_EXT = self.HTML_EXT
        self.spider.start_requests = self.start_requests

    def test_urls(self):
        result = list(self.spider.start_requests())
        print(result)

    def get_response_object(self, url):
        path_to_file = url.replace(FILE_SYSTEM_PREFIX, '')
        f = open(path_to_file, 'rb')
        bytess = f.read()
        f.close()
        return HtmlResponse(url, 200, self.generate_response_headers(), bytess, None, Request(url), encoding='utf-8')

    def generate_response_headers(self):
        headers = Headers()
        headers.appendlist('Connection', 'keep-alive')
        headers.appendlist('Content-Encoding', 'gzip')
        headers.appendlist('Content-Type', 'text/html; charset=utf-8')
        headers.appendlist('Date', 'Thu, 20 Feb 2020 00:59:44 GMT')
        headers.appendlist('Server', 'nginx/1.14.0 (Ubuntu)')
        headers.appendlist('Transfer-Encoding', 'chunked')
        headers.appendlist('X-Upstream', 'toscrape-pstrial-2019-12-16_web')
        return headers

    def generate_request_headers(self):
        headers = Headers()
        headers.appendlist('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9')
        headers.appendlist('Accept-Encoding', 'gzip, deflate')
        headers.appendlist('Accept-Language', 'en-US,en;q=0.9,ru;q=0.8')
        headers.appendlist('Connection', 'keep-alive')
        headers.appendlist('Host', 'pstrial-2019-12-16.toscrape.com')
        headers.appendlist('Referer', 'http://pstrial-2019-12-16.toscrape.com/browse/')
        headers.appendlist('Upgrade-Insecure-Requests', '1')
        headers.appendlist('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36')
        return headers


if __name__ == '__main__':
    main()
