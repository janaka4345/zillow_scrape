import scrapy
import json

from scrapy.http import Response
from zillowscraper.items import ZillowscraperItem


class ZillowspiderSpider(scrapy.Spider):
    name = "zillowspider"
    allowed_domains = ["scrapeops.io", "zillow.com"]
    home_url = "https://www.zillow.com/homes"
    # start_urls = ["https://example.com"]

    def start_requests(self):
        url = "https://www.zillow.com/homes/Los-Angeles,-CA_rb/"
        yield scrapy.Request(url)

    def parse(self, response):
        file = response.xpath('//script[@id="__NEXT_DATA__"]/text()').get()
        json_data = json.loads(file)

        homes = json_data["props"]["pageProps"]["searchPageState"]["cat1"][
            "searchResults"
        ]["listResults"]

        home_item = ZillowscraperItem()
        for home in homes:
            home_item["address"] = home.get("address", None)
            home_item["beds"] = home.get("beds", None)
            home_item["baths"] = home.get("baths", None)
            home_item["floorSize"] = home.get("area", None)
            home_item["url"] = home.get("detailUrl", None)
            home_item["images"] = home.get("carouselPhotos", None)
            home_item["price"] = home.get("unformattedPrice", None)
            yield home_item

        next_page = json_data["props"]["pageProps"]["searchPageState"]["cat1"][
            "searchList"
        ]["pagination"]["nextUrl"]
        next_url = f"{self.home_url}{next_page}"
        yield response.follow(next_url, callback=self.parse)
