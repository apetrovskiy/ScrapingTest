from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
#from RyanMitchell.chapter05.wikiSpider.\
from wikiSpider.items import Article


class ArticlesSpider5555(CrawlSpider):
    name = 'articleItems5'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/'
                  'Benevolent_dictator_for_life']
    rules = [
        Rule(LinkExtractor(allow='^(/wiki/)((?!:).)*$'),
             callback='parse_items', follow=True)
    ]

    def parse_items(self, response):
        article = Article()
        article['url'] = response.url
        article['title'] = response.css('h1::text').extract_first()
        article['text'] = response.xpath('//div[@id="mw-content-text"]'
                                         '//text()').extract()
        lastUpdated = response.css('li#footer-info-lastmod'
                                   '::text').extract_first()
        lastUpdated = lastUpdated.replace('This page was '
            'last edited on ', ''
        )
        return article
