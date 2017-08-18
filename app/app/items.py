# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AppItem(scrapy.Item):
    appId = scrapy.Field()
    iconUrl = scrapy.Field()
    pkgName = scrapy.Field()
    appName = scrapy.Field()
    isOfficial = scrapy.Field()
    averageRating = scrapy.Field()
    ratingCount = scrapy.Field()
    appDownCount = scrapy.Field()
    fileSize = scrapy.Field()
    categoryId = scrapy.Field()
    categoryName = scrapy.Field()
    images = scrapy.Field()
    versionName = scrapy.Field()
    apkPublishTime = scrapy.Field()
    authorId = scrapy.Field()
    authorName = scrapy.Field()
    description = scrapy.Field()
    sameList = scrapy.Field()
    crawl_time = scrapy.Field()

