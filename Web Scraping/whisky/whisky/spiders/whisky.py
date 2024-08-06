from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy

class CrawlingSpider(CrawlSpider):
    name = "mycrawler"
    allowed_domains = ["belanjakomputer.com"]
    start_urls = ["https://www.belanjakomputer.com/"]

    rules = (
        Rule(LinkExtractor(allow="product"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        yield {
            "product_title": response.css('.product-title a::text').get(),
            "price": response.css('.price .woocommerce-Price-amount.amount bdi::text').get(),
            "brand": response.css('.products-page-brands a::text').get(),
            "details": ' '.join(response.css('.text-center.product-details *::text').getall()).strip()
        }
