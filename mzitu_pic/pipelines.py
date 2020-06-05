# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
from scrapy.pipelines.images import ImagesPipeline
from urllib.parse import urlparse
from scrapy.http import Request

class MzituImagesPipeline(ImagesPipeline):
    default_headers = {
        'accept': 'image/webp,image/*,*/*;q=0.8',
        'referer': 'https://www.mzitu.com/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    def get_media_requests(self,item,info):
        for image_url in item['image_urls']:
            self.default_headers['referer'] = item['referer']
            yield Request(image_url,meta={'title':item['title']},headers=self.default_headers)
    def file_path(self, request, response=None, info=None):
        path = 'images/' + ''.join(request.meta['title']) + '/' + os.path.basename(urlparse(request.url).path)
        return path 
