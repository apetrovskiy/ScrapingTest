from os import getcwd
from scrapy.http.headers import Headers
from scrapy.http.request import Request
from scrapy.http.response.html import HtmlResponse
from unittest import TestCase, main
# from Doc.tutorial.\
from Doc.tutorial.tutorial.spiders.quotes_spider_3 import QuotesSpider3


TUTS_FOLDER_NAME = 'tutorial'
TESTS_FOLDER_NAME = 'tests'
TEST_DATA_FOLDER_NAME = 'test_data'
FILE_SYSTEM_PREFIX = 'file://'
SLASHE = "/"


class QuotesSpider3Test(TestCase):
    SPIDER_NAME = 'quotes_test'

    @classmethod
    def get_path_to_test_data(cls):
        result = getcwd()
        result = QuotesSpider3Test \
            .build_path(result,
                        TUTS_FOLDER_NAME,
                        SLASHE + TUTS_FOLDER_NAME +
                        SLASHE + TUTS_FOLDER_NAME)
        result = QuotesSpider3Test \
            .build_path(result,
                        TUTS_FOLDER_NAME + '/' + TUTS_FOLDER_NAME,
                        SLASHE + TUTS_FOLDER_NAME)
        result = QuotesSpider3Test \
            .build_path(result,
                        TESTS_FOLDER_NAME,
                        SLASHE + TESTS_FOLDER_NAME)
        result = QuotesSpider3Test \
            .build_path(result,
                        TEST_DATA_FOLDER_NAME,
                        SLASHE + TEST_DATA_FOLDER_NAME)
        result = FILE_SYSTEM_PREFIX + result
        return result

    @classmethod
    def build_path(self, path, condition, addition):
        if condition not in path:
            return path + addition
        return path

    start_urls = [
        get_path_to_test_data() + '1/',
        get_path_to_test_data() + '2/',
    ]

    def setUp(self) -> None:
        self.spider = QuotesSpider3(name=self.SPIDER_NAME)

    def get_request(self, response, url):
        response = self.get_response_object(url)
        print("===========get_request TEST================")
        print("url: %s" % response.url)
        return response

    def get_response_object(self, url):
        path_to_file = url.replace(FILE_SYSTEM_PREFIX, '')
        if path_to_file[-1:] == SLASHE:
            path_to_file = path_to_file[:-1]
        if url[-1:] == SLASHE:
            url = url[:-1]
        f = open(path_to_file, 'rb')
        bytess = f.read()
        f.close()
        return HtmlResponse(url, 200, self.generate_response_headers(),
                            bytess, None, Request(url), encoding='utf-8')

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


if __name__ == '__main__':
    main()
