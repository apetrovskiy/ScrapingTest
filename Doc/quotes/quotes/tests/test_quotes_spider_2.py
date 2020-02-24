from os import getcwd
from scrapy.http.headers import Headers
from scrapy.http.response.html import HtmlResponse
from scrapy.http.request import Request
from unittest import TestCase, main
from quotes.quotes.spiders.quotes_spider import QuotesSpider2

START_PAGE = '/tag/humor/'
QUOTES_FOLDER_NAME = 'quotes'
TESTS_FOLDER_NAME = 'tests'
TEST_DATA_FOLDER_NAME = 'test_data'
SPIDERS_FOLDER_NAME = 'spiders'
START_HTML_FILE = '/quotes.mhtml'
SPIDER_NAME = 'quotes_test_spider'
FILE_SYSTEM_PREFIX = 'file://'
SLASHE = "/"
EXPECTED_NUMBER_OF_QUOTES_PAGE_01 = 10
EXPECTED_NUMBER_OF_QUOTES_PAGE_02 = 2


class QuotesSpiderTest(TestCase):
    @classmethod
    def get_path_to_test_data(cls):
        result = getcwd()
        result = QuotesSpiderTest \
            .build_path(result,
                        QUOTES_FOLDER_NAME,
                        SLASHE + QUOTES_FOLDER_NAME +
                        SLASHE + QUOTES_FOLDER_NAME)
        result = QuotesSpiderTest \
            .build_path(result,
                        QUOTES_FOLDER_NAME + '/' + QUOTES_FOLDER_NAME,
                        SLASHE + QUOTES_FOLDER_NAME)
        result = QuotesSpiderTest \
            .build_path(result,
                        TESTS_FOLDER_NAME,
                        SLASHE + TESTS_FOLDER_NAME)
        result = QuotesSpiderTest \
            .build_path(result,
                        TEST_DATA_FOLDER_NAME,
                        SLASHE + TEST_DATA_FOLDER_NAME)
        result = FILE_SYSTEM_PREFIX + result
        return result

    @classmethod
    def get_path_to_spider(cls, spider_name):
        result = getcwd()
        result = QuotesSpiderTest \
            .build_path(result,
                        QUOTES_FOLDER_NAME,
                        SLASHE + QUOTES_FOLDER_NAME +
                        SLASHE + QUOTES_FOLDER_NAME)
        result = QuotesSpiderTest \
            .build_path(result,
                        QUOTES_FOLDER_NAME + SLASHE + QUOTES_FOLDER_NAME,
                        SLASHE + QUOTES_FOLDER_NAME)
        result = QuotesSpiderTest \
            .build_path(result,
                        SPIDERS_FOLDER_NAME,
                        SLASHE + SPIDERS_FOLDER_NAME + SLASHE)
        result = FILE_SYSTEM_PREFIX + result + spider_name + '.py'
        return result

    def setUp(self) -> None:
        QuotesSpider2.URL = self.get_path_to_test_data()
        start_urls = [self.get_path_to_test_data() + START_HTML_FILE]
        self.spider = QuotesSpider2(name=SPIDER_NAME)
        self.spider.start_urls = start_urls
        self.spider.get_response = self.get_response

    def test_quotes_on_page_01(self):
        # Given
        response = self.get_response_object(
            self.get_path_to_test_data() + START_HTML_FILE)

        # When
        actual_result = list(self.spider.parse(response))

        # Then
        assert EXPECTED_NUMBER_OF_QUOTES_PAGE_01 + 1 == len(actual_result)
        for res in actual_result:
            print(res)

    def test_quotes_on_page_02(self):
        # Given
        first_page_result = list(self.spider.parse(
            self.get_response_object(
                self.get_path_to_test_data() + START_HTML_FILE)))
        response = first_page_result[-1:].pop(0)

        # When
        actual_result = list(self.spider.parse(response))

        # Then
        assert EXPECTED_NUMBER_OF_QUOTES_PAGE_02 == len(actual_result)
        for res in actual_result:
            print(res)

    def get_response(self, response, url):
        response = self.get_response_object(url)
        return response

    def get_response_object(self, url):
        path_to_file = url.replace(FILE_SYSTEM_PREFIX, '')
        if path_to_file[-1:] == SLASHE:
            path_to_file = path_to_file[:-1]
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

    @classmethod
    def build_path(self, path, condition, addition):
        if condition not in path:
            return path + addition
        return path


if __name__ == '__main__':
    main()
