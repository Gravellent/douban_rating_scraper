# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Movie_rating(scrapy.Item):
    # define the fields for your item here like:
    user = scrapy.Field()
    rating_id = scrapy.Field()
    title = scrapy.Field()
    movie_id = scrapy.Field()
    url = scrapy.Field()
    rating = scrapy.Field()
    rating_date = scrapy.Field()
    rating_ts = scrapy.Field()
    comment = scrapy.Field()
    # pass
