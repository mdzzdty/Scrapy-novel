import scrapy

from tutorial.items import MinuItem,NameItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    #allowed_domains = ["dmoz.org"]
    start_urls = [
        "https://www.80txt.com"
    ]

    def parse(self,response):
        item = MinuItem()
        """
        for classname,url in \
            response.xpath("//div[@id='menu']/div/ul/li/a/text()").extract(), \
            response.xpath("//div[@id='menu']/div/ul/li/a/@href").extract():

            yield scrapy.Request(self_urls[0]+url,callback=self.getName)
        """

        item['novelClass'] = response.xpath("//div[@id='menu']/div/ul/li/a/text()").extract()
        item['novelClassUrl'] = response.xpath("//div[@id='menu']/div/ul/li/a/@href").extract()
        
        yield scrapy.Request(self_urls[0]+item['novelUrl'][0],callback=self.getName)

    def getName(self,response):
        for name,url in \
            response.xpath("//div[@class='book_bg']/a/text()").extract(), \
            response.xpath("//div[@class='book_bg']/a/@href").extract()
            print(name)
            print(url)



