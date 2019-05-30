# encoding: utf-8
# scrapy runspider npr_transcript.py -o npr_transcript.jl
import scrapy
import re, json, sys, traceback, math, random, urllib, time
from scrapy.selector import Selector
from scrapy.utils.serialize import ScrapyJSONEncoder
from scrapy.utils.python import to_bytes

import json
import logging
logger = logging.getLogger(__name__)

class DownloadTimeMeasure(object):
    def process_request(self, request, spider):
        request.meta['time_used'] = time.time()

    def process_response(self, request, response, spider):
        request.meta['time_used'] = time.time() - request.meta['time_used']
        #  logger.info('Fetched %s in %f seconds.' % (request.url, request.meta['time_used']))
        return response

from scrapy.conf import settings
settings.set('DOWNLOAD_TIMEOUT', 5)
settings.set('HTTPERROR_ALLOW_ALL', True)
settings.set('COOKIES_ENABLED', False)
settings.set('USER_AGENT', "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36")
settings.set('DOWNLOADER_MIDDLEWARES', {
    'npr_transcript.DownloadTimeMeasure':100
    })

class LanguageFolderVerifier(scrapy.Spider):
    name = "LanguageFolderVerifier"

    def start_requests(self):
      yield scrapy.Request("https://www.google.com/search?hl=en&as_q=&as_epq=inurl%3Atranscript+php&as_oq=&as_eq=&as_nlo=&as_nhi=&lr=&cr=&as_qdr=d&as_sitesearch=www.npr.org&as_occt=any&safe=images&as_filetype=&as_rights=", callback=self.parseUrl,
              meta={'dont_redirect': True}, dont_filter=True)

    def parseUrl(self, response):
      for u in response.xpath('//div[@class="rc"]//a'):
        yield {"url": u.xpath('.//@href').extract()[0], "title": u.xpath('.//h3/text()').extract()[0]}
