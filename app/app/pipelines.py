# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from scrapy.exceptions import DropItem


class MysqlPipeline(object):
	"""
	本机 localhost；公司 etl2.innotree.org；服务器 etl1.innotree.org
	"""

	def __init__(self):
		self.conn = pymysql.connect(host='etl2.innotree.org', port=3308, user='spider', password='spider', db='spider',
		                            charset='utf8', cursorclass=pymysql.cursors.DictCursor)
		self.cursor = self.conn.cursor()

	def process_item(self, item, spider):
		sql = """replace into yingyb(appId, iconUrl, pkgName, appName, isOfficial, averageRating, ratingCount, appDownCount, fileSize, 
				categoryId, categoryName, images, versionName, apkPublishTime, authorId, authorName, description, sameList, crawl_time) 
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
		args = (
			item['appId'], item['iconUrl'], item['pkgName'], item['appName'], item['isOfficial'], item['averageRating'],
			item['ratingCount'],
			item['appDownCount'], item['fileSize'], item['categoryId'], item['categoryName'], item['images'],
			item['versionName'],
			item['apkPublishTime'], item['authorId'], item['authorName'], item['description'], item['sameList'],
			item['crawl_time']
		)
		self.cursor.execute(sql, args=args)
		self.conn.commit()
		print(str(item['appId']))
		return item


class DuplicatesPipeline(object):
	def __init__(self):
		self.ids_seen = set()

	def process_item(self, item, spider):
		if item['appId'] in self.ids_seen:
			raise DropItem("Duplicate item found: %s" % item['appId'])
		else:
			self.ids_seen.add(item['appId'])
			return item
