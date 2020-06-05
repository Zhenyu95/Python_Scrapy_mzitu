# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from mzitu_pic.items import ImageItem


class MzituSpider(CrawlSpider):
    name = 'mzitu'
    start_urls = ['https://www.mzitu.com']

    rules = (
        Rule(LinkExtractor(allow=r'page/[1,2,3]',restrict_xpaths='//div[@class="pagination"]//a')),
        Rule(LinkExtractor(allow=r'.+com/\d{6}',restrict_xpaths='//div[@class="postlist"]//li//a'),follow=True,callback='parse_images'),
        Rule(LinkExtractor(allow=r'.+com/\d{6}/\d',restrict_xpaths='//div[@class="pagenavi"]/a'),follow=True,callback='parse_images'),   
    )

    def parse_images(self,response):
        
        # imgLink = response.xpath('//div[@class="main-image"]//img/@src').get()
        # item = MzituPicItem(name='name',link=imgLink)
        
        title = response.xpath('//div[@class="main-image"]//img/@alt').get()
        img_url = response.xpath('//div[@class="main-image"]//img/@src').get()
        item = ImageItem(title=title,image_urls=list(img_url.split(" ")),referer=response.url)
        yield item
