# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
from scrapy.exporters import JsonLinesItemExporter

"""
json
"""
# class QsbkPipeline:
#     def __init__(self):
#         self.fp = open('qsbk.json', 'w')
#
#     def open_spider(self, spider):
#         print('爬虫开始...')
#
#     def process_item(self, item, spider):
#         data = json.dumps(dict(item), ensure_ascii=False)
#         self.fp.write(data + '\n')
#
#     def close_spider(self, spider):
#         self.fp.close()
#         print('爬虫结束...')

"""
JsonLinesItemExporter 
"""


class QsbkPipeline:
    def __init__(self):
        self.fp = open('qsbk.json', 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False)

    def open_spider(self, spider):
        print('爬虫开始...')

    def process_item(self, item, spider):
        self.exporter.export_item(item)

    def close_spider(self, spider):
        self.fp.close()
        print('爬虫结束...')
