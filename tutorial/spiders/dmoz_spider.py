import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "https://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/examples.html"
    ]

    def parse(self,response):
        filename = response.xpath("//div/p/text()|//div/p/a/text()").extract
        with open("test.txt",'wb') as f:
            print(type(filename))