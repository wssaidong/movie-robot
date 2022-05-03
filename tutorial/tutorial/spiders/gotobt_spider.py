import scrapy
#from tutorial.items import RecruitItem

class RecruitSpider(scrapy.spiders.Spider):
    name = "gotobt"
    allowed_domains = ["gotobt.com"]
    start_urls = [
        "http://gotobt.com/s/dy/qs/Index.Html"
    ]
    def parse_detail(self,response):
        item = response.meta['item']
        magnet = response.xpath('//a[@target="_blank" and @href]')[1].xpath('./@href').extract()[0]
        item['magnet'] = magnet
        yield item

    def parse(self, response):
      for sel in response.xpath('//a[@target="_blank" and @href]'):
        name = sel.xpath('./text()').extract()[0]
        detailLink = sel.xpath('./@href').extract()[0]
        item = {} #RecruitItem()
        item['name']= name
        detail_url = "http://gotobt.com" + detailLink
        item['detail_url']= detail_url
        yield scrapy.Request(url=detail_url,callback=self.parse_detail,meta={'item':item})


