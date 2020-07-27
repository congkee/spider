import scrapy
from ..items import QsbkItem

from scrapy.http.response.html import HtmlResponse


class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/2/']
    base_url = "https://www.qiushibaike.com"

    def parse(self, response):
        duanzi_divs = response.xpath("//div[@class='col1 old-style-col1']/div")
        # items = []
        for duanzi_div in duanzi_divs:
            author = duanzi_div.xpath(".//h2//text()").get()
            content = duanzi_div.xpath(".//span//text()").getall()
            content = "".join(content).strip()
            item = QsbkItem(author=author, content=content)
            # items.append(item)
            yield item

        next_url = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
        if not next_url:
            return
        else:
            yield scrapy.Request(self.base_url + next_url, callback=self.parse)
