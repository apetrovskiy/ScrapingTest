import pytest
from pytest_mock import MockerFixture
# from scrapy.http.response import Response
from scrapy.http.response.html import HtmlResponse
from Doc.v2_4.tutorial.tutorial.spiders.quotes_spider import QuotesSpider


class QuotesSpiderChild(QuotesSpider):
    body = ""

    def __init__(self, body: str):
        self.body = body

    def save_file(self, filename: str, body: str):
        assert self.body == body


def new_rsplit(data: str, number: int):
    return ""


def test_quotes_spider(mocker: MockerFixture) -> None:
    # v 1
    # response = mocker.patch(Response)
    # response.url = 'http://localhost/1/'
    # response.body = 'body data'
    # response.rsplit = ""
    # spider = QuotesSpiderChild(response.body)
    # spider.parse(response)

    # v 2
    # with mocker.patch.object(Response, 'rsplit', new=new_rsplit):
    #     obj = Response()
    #     obj.url = 'http://localhost/1/'
    #     obj.body = 'body data'
    #     spider = QuotesSpiderChild(obj.body)
    #     spider.parse(obj)

    url = 'http://localhost/1/'
    body = b"body data"
    response = HtmlResponse(url=url, body=body)
    spider = QuotesSpiderChild(response.body)
    spider.parse(response)

    # spider.save_file("filename", response.body)
