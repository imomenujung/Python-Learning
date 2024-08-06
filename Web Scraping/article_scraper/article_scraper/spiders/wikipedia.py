import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from article_scraper.items import Article


class WikipediaSpider(CrawlSpider):
    name = "wikipedia"
    allowed_domains = ["https://www.whiskyshop.com"]
    start_urls = ["https://www.whiskyshop.com/newreleases"]
             

    def parse_info(self, response):
        article = Article()
        article['title']= response.xpath('//*[@id="firstHeading"]/span').get() or response.xpath('//h1/i/text()').get()
        article['url']= response.url
        article['lastUpdated'] = response.xpath('//li[@id="footer-info-lastmod"]/text()').get()
        return article
    
