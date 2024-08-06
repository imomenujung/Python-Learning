import scrapy


class IetfSpider(scrapy.Spider):
    name = "ietf"
    allowed_domains = ["pythonscraping.com"]
    start_urls = ["https://pythonscraping/linkedin/ietf.html.com"]

    def parse(self, response):
        #title = response.css('span.title::text').get()
        title = response.xpath('//span[@class="title"]/text()').get()
        return {"title":title}
