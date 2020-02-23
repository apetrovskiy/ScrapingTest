from os import getcwd
from unittest import TestCase, main
from scrapy.http.headers import Headers
from scrapy.http.response import Request
from scrapy.http.response.html import HtmlResponse
#from RyanMitchell.chapter05.wikiSpider.\
from wikiSpider.spiders.article import ArticleSpider


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


class TestArticle(TestCase):
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

        for url in urls:
            yield self.spider.parse(self.get_response_object(url))

    def setUp(self):
        self.spider = ArticleSpider(name=SPIDER_NAME)
        ArticleSpider.BROWSE = self.BROWSE
        ArticleSpider.HTML_EXT = self.HTML_EXT
        self.spider.start_requests = self.start_requests

    def test_urls(self):
        actual_results = list(self.spider.start_requests())
        print(actual_results)
        for result_tuple in actual_results:
            assert self.get_path_to_test_data() in result_tuple[0]

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
