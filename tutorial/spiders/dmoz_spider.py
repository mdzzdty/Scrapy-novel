import scrapy

from tutorial.items import MinuItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    #allowed_domains = ["dmoz.org"]
    start_urls = [
        "https://www.80txt.com"
    ]

    def parse(self,response):
        item = MinuItem()
        item['novelName'] = response.xpath("//div[@id='menu']/div/ul/li/a/text()").extract()
        item['novelUrl'] = response.xpath("//div[@id='menu']/div/ul/li/a/@href").extract()
        
