# import scrapy
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule

# import re

# class UnsplashImageItem(scrapy.Item):
#     image_url = scrapy.Field()
#     image_name = scrapy.Field()
#     category = scrapy.Field()

# # //*[@class="oaSYM ZR5jm"] категория
# # //*[@class="WxXog"] фото
# # //*[@class="WxXog"]/img/@srcset LinkExtractor

# class UnsplashSpider(scrapy.Spider):
#     name = 'unsplash'
#     allowed_domains = ['unsplash.com']
#     start_urls = ['https://unsplash.com/']

#     def parse(self, response):
#         for category in response.xpath('//*[@class="oaSYM ZR5jm"]/@href').extract():
#             yield scrapy.Request(response.urljoin(category), self.parse_category)

#     def parse_category(self, response):
#         # Извлекаем ссылки на изображения и их разрешения из srcset
#         for image_url, image_name in zip(response.xpath('//*[@class="WxXog"]/img/@srcset').extract(), response.xpath('//*[@class="WxXog"]/img/@alt').extract()):
#             # Выводим элемент изображения
#             yield UnsplashImageItem(category=response.url.split('/')[-1], image_name=image_name, image_url=image_url)

#             # Скачиваем полную версию изображения
#             yield scrapy.Request(response.urljoin(image_url), self.save_image)

#     def save_image(self, response):
#         # Получаем имя файла изображения
#         filename = response.url.split('/')[-1]
#         # Сохраняем изображение в папку images
#         with open(f'images/{filename}', 'wb') as f:
#             f.write(response.body)
