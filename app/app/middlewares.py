# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import base64
from random import choice

# 代理服务器
proxyServer = "http://proxy.abuyun.com:9020"

# 1
# proxyUser = "H3E0I8FIV5N3130D"
# proxyPass = "5B75712BA415792F"

# 2
# proxyUser = "H256J792G0477J3D"
# proxyPass = "A978AA975C1C8E59"

# 3
# proxyUser = "HDJYRWK2113M79ED"
# proxyPass = "0FE38BB4282AFC2B"

# 4
proxyUser = "H9269C63N6C305PD"
proxyPass = "B4BA11856FD0D4E3"

# 5
# proxyUser = "H245OL3592LCHU6D"
# proxyPass = "3C0CEF6238CAF281"


# for Python3
proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")


class ProxyMiddleware(object):
	def process_request(self, request, spider):
		request.meta["proxy"] = proxyServer
		request.headers["Proxy-Authorization"] = proxyAuth


class RetryMiddleware(object):
	def process_response(self, request, response, spider):
		if response.status == 429:
			# print('wrong status: %s, retrying~~' % response.status, request.url)
			return request.replace(url=request.url)
		else:
			return response

	def process_exception(self, request, exception, spider):
		return request.replace(url=request.url)


class RotateUserAgentMiddleware(object):
	"""Middleware used for rotating user-agent for each request"""

	def __init__(self, agents):
		self.agents = agents

	@classmethod
	def from_crawler(cls, crawler):
		return cls(crawler.settings.get('USER_AGENT_CHOICES', []))

	def process_request(self, request, spider):
		request.headers.setdefault('User-Agent', choice(self.agents))




