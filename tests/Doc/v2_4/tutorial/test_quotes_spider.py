import pytest
from pytest_mock import MockerFixture
from scrapy.http.response import Response
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
    # response = mocker.patch(Response)
    # response.url = 'http://localhost/1/'
    # response.body = 'body data'
    # response.rsplit = ""
    with mocker.patch.object(Response, 'rsplit', new=new_rsplit):
        obj = Response()
        obj.url = 'http://localhost/1/'
        obj.body = 'body data'
        spider = QuotesSpiderChild(obj.body)
        spider.parse(obj)
    # spider = QuotesSpiderChild(response.body)
    # spider.parse(response)
    # spider.save_file("filename", response.body)
