import scrapy


class PostsSpider(scrapy.Spider):
    name = "posts"

    start_urls = [
        # 'https://blog.scrapinghub.com/page/1/',
        # 'https://blog.scrapinghub.com/page/2/',
        'https://www.zyte.com/blog/scrapy-update-better-broad-crawl-performance/',
        'https://www.zyte.com/blog/automatic-extraction-data-extractor-review/'

    ]

    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = 'posts-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
