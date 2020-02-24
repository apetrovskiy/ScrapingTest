from scrapy import Field, Item


class Article(Item):
    url = Field()
    title = Field()
    text = Field()
    lastUpdated = Field()
