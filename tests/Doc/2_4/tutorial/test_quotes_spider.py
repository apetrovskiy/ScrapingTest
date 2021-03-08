import pytest
from pytest_mock import MockerFixture


def test_quotes_spider(mocker: MockerFixture)-> None:
    response = mocker.patch.