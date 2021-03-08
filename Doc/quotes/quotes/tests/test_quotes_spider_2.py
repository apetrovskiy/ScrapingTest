from os import getcwd
from scrapy.commands.parse import Command
from scrapy.http.headers import Headers
from scrapy.http.request import Request
from scrapy.http.response.html import HtmlResponse
from unittest import TestCase, main
from Doc.quotes.quotes.spiders.quotes_spider_2 import QuotesSpider2


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
        #self.spider.get_request = self.get_request
        self.spider._follow_links = True

        self.spider.parse = self.parse
        #self.spider.parse_extract = self.parse_extract

        self.response = self.get_response_object(
            self.get_path_to_test_data() + START_HTML_FILE)
    '''
    def test_quotes_on_page_01(self):
        # When
        actual_result = list(self.spider._parse_response(
            self.response,
            callback=self.spider.parse,
            cb_kwargs={},
            follow=True))

        # Then
        assert EXPECTED_NUMBER_OF_QUOTES_PAGE_01 + 1 == len(actual_result)
        for res in actual_result:
            print(res)
    '''

    def test_quotes_on_page_02(self):
        # Given
        '''
        first_page_result = list(self.spider._parse_response(
            self.response,
            callback=self.spider.parse,
            cb_kwargs={},
            follow=True))
        '''
        first_page_result = list(self.spider.parse(self.response))
        response = first_page_result[-1:].pop(0)
        # print(response)

        for res in first_page_result:
            print(res)
        '''
        # When
        actual_result = list(self.spider.parse(response)),

        # Then
        #assert EXPECTED_NUMBER_OF_QUOTES_PAGE_02 == len(actual_result)
        print(len(actual_result))
        for res in actual_result:
            print(res)
        '''

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

    @classmethod
    def build_path(self, path, condition, addition):
        if condition not in path:
            return path + addition
        return path

    def parse(self, response):
        return self.parse_extract(response)

    def parse_extract(self, response):
        print("========================TEST parse_extract======================")
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
            yield response.follow(self.get_path_to_test_data() + next_page, self.parse_extract)
            # yield self.get_response(response, self.URL + nex#_page)

            #url = self.URL + next_page
            # yield self.get_request(response, url)

            # yield QuotesSpider2.get_request(response=response, url=url)
            # for resp in response:
            #    yield QuotesSpider2.get_request(response=resp, url=url)


if __name__ == '__main__':
    main()
