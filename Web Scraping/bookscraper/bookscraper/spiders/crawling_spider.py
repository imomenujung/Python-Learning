from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CrawlingSpider(CrawlSpider):
    name = "mycrawler"
    allowed_domains =["https://books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/index.html"]

rules =(
    Rule(LinkExtractor(allow="catalogue/category")),
    Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_item")
)

def parse_item(self,response):
    yield{
        "title": response.css(".product_main h1::text").get(),
        "price": response.css(".price_color::text").get(),
        "availibility": response.css(".availibility::text")[2].get()

    }