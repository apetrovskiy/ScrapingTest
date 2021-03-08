import pytest
from pytest_mock import MockerFixture
from scrapy.http.response import Response
from Doc.v2_4.tutorial.tutorial.spiders.quotes_spider import QuotesSpider


def test_quotes_spider(mocker: MockerFixture) -> None:
    response = mocker.patch.object(Response)
    response.url = 'http://localhost/1/'
    response.body = 'body data'
    spider = QuotesSpider()
