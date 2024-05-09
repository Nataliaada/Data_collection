# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class UnsplashCsvPipeline:

    def open_spider(self, spider):
        self.file = open('unsplash_images.csv', 'w', newline='')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['image_url', 'local_path', 'image_name', 'category'])

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        image_url = item['image_url']
        local_path = item['image_url'].split('/')[-1]
        image_name = item['image_name']
        category = item['category']

        self.writer.writerow([image_url, local_path, image_name, category])

        return item


from scrapy.pipelines.images import ImagesPipeline

class AnimalsImagesPipeline(ImagesPipeline): 
    def get_media_requests(self, item, info):
        for image_url in item.get('image_urls', []):
            yield scrapy.Request(image_url)

def file_path(self, request, response=None, info=None, *,item=None ):
              return f"{item['category']}_{item['image_url']}.jpg"