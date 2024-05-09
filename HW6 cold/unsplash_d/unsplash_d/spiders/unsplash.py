import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

import re
import os
import scrapy
import os

class UnsplashImageItem(scrapy.Item):
 image_url = scrapy.Field()
 image_name = scrapy.Field()
 category = scrapy.Field()

class UnsplashSpider(scrapy.Spider):
 name = 'unsplash'
 allowed_domains = ['unsplash.com']
 start_urls = ['https://unsplash.com/']

 def parse(self, response):
    for category in response.xpath('//*[@class="oaSYM ZR5jm"]/@href').extract():
        yield scrapy.Request(response.urljoin(category), callback=self.parse_category)

 def parse_category(self, response):
    category = response.url.split('/')[-1]
    image_urls = response.xpath('//*[@class="WxXog"]/img/@src').extract()
    image_names = response.xpath('//*[@class="WxXog"]/img/@alt').extract()
    selector = scrapy.Selector(response=response, type='html')
    for image_url, image_name in zip(image_urls, image_names):
        yield UnsplashImageItem(category=category, image_name=image_name, image_url=image_url)
        yield scrapy.Request(response.urljoin(image_url), callback=self.save_image, meta={'category': category, 'image_name': image_name})

 def save_image(self, response):
    category = response.meta['category']
    image_name = response.meta['image_name']
    if not os.path.exists(f'images/{category}'):
        os.makedirs(f'images/{category}')
    with open(f'images/{category}/{image_name}.jpg', 'wb') as f:
        f.write(response.body)