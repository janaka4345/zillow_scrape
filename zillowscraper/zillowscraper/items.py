# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZillowscraperItem(scrapy.Item):
    # define the fields for your item here like:

    beds = scrapy.Field()
    baths = scrapy.Field()
    address = scrapy.Field()
    floorSize = scrapy.Field()
    url = scrapy.Field()
    images = scrapy.Field()
    price = scrapy.Field()
