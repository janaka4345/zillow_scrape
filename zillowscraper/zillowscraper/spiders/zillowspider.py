import scrapy


class ZillowspiderSpider(scrapy.Spider):
    name = "zillowspider"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response):
        pass
