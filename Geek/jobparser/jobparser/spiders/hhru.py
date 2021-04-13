import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem


class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = [
        'https://izhevsk.hh.ru/search/vacancy?area=&st=searchVacancy&text=python']

    def parse(self, response: HtmlResponse):
        next_page = response.css(
            'a.HH-Pager-Controls-Next::attr(href)').extract_first()
        yield response.follow(next_page, callback=self.parse)

        # vacansy = response.css(
        #     'div.vacancy-serp div.vacancy-serp-item div.vacancy-serp-item__row_header a.bloko-link::attr(href)').extract()
        # body > div.HH-MainContent.HH-Supernova-MainContent > div > div.main-content > div.bloko-columns-wrapper > div > div.sticky-container > div >
        # div.vacancy-serp-wrapper.HH-SearchVacancyDropClusters-XsHiddenOnClustersOpenItem > div >
        # div.bloko-gap.bloko-gap_s-top.bloko-gap_m-top.bloko-gap_l-top > div > div > div:nth-child(2) >
        # div.vacancy-serp-item__row.vacancy-serp-item__row_header > div.vacancy-serp-item__info > span > span > span > a
        vacansy = response.css(
            'div.vacancy-serp-wrapper div.vacancy-serp-item__row.vacancy-serp-item__row_header a.bloko-link::attr(href)').extract()

        for link in vacansy:
            yield response.follow(link, callback=self.vacansy_parse)

    def vacansy_parse(self, response: HtmlResponse):
        # name = response.css(
        #     'div.vacancy-title h1.header::text').extract_first()
        # body > div.HH-MainContent.HH-Supernova-MainContent > div > div.main-content > div.bloko-columns-wrapper > div > div.sticky-container > div >
        # div.vacancy-serp-wrapper.HH-SearchVacancyDropClusters-XsHiddenOnClustersOpenItem > div >
        # div.bloko-gap.bloko-gap_s-top.bloko-gap_m-top.bloko-gap_l-top > div > div > div:nth-child(2) >
        # div.vacancy-serp-item__row.vacancy-serp-item__row_header > div.vacancy-serp-item__info > span > span > span > a
        name = response.css(
            'div.vacancy-serp-item__info > span > span > span > a::text').extract_first()
        # salary = response.css(
        #     'div.vacancy-title p.vacancy-salary::text').extract()
        # body > div.HH-MainContent.HH-Supernova-MainContent > div > div.main-content > div.bloko-columns-wrapper > div > div.sticky-container > div >
        # div.vacancy-serp-wrapper.HH-SearchVacancyDropClusters-XsHiddenOnClustersOpenItem > div >
        # div.bloko-gap.bloko-gap_s-top.bloko-gap_m-top.bloko-gap_l-top > div > div > div:nth-child(2) >
        # div.vacancy-serp-item__row.vacancy-serp-item__row_header > div.vacancy-serp-item__sidebar > span
        salary = response.css(
            'div.vacancy-serp-item__sidebar > span::text').extract()
        yield JobparserItem(name=name, salary=salary)
