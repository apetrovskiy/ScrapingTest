from datetime import datetime
#from RyanMitchell.chapter05.wikiSpider.\
from wikiSpider.items import Article
from string import whitespace


class WikispiderPipeline(object):
    def process_item(self, article, spider):
        dateStr = article['lastUpdated']
        article['lastUpdated'] = article['lastUpdated']\
            .replace('This page was last edited on', '')
        article['lastUpdated'] = article['lastUpdated'].strip()
        article['lastUpdated'] = datetime.strptime(
            article['lastUpdated'], '%d %B %Y, at %H:%M.')
        article['text'] = [line for line in article['text']
                           if line not in whitespace]
        article['text'] = ''.join(article['text'])
        return article
