import scrapy
import os


class ZillowspiderSpider(scrapy.Spider):
    name = "zillowspider"
    # allowed_domains = ["example.com"]
    # start_urls = ["https://example.com"]

    def start_requests(self):
        url = "https://www.zillow.com/"
        yield scrapy.Request(url)

    def parse(self, response):
        print(response)
