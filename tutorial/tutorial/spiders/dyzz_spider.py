import scrapy
#from tutorial.items import RecruitItem

class RecruitSpider(scrapy.spiders.Spider):
    name = "dyzz"
    allowed_domains = ["www.ygdy8.net"]
    start_urls = [
        "https://www.ygdy8.net/html/gndy/dyzz/index.html"
    ]
    def parse_detail(self,response):
        item = response.meta['item']
        #magnet = response.xpath('/html/body/div[1]/div/div[3]/div[3]/div[1]/div[2]/div[2]/ul/div[1]/span/a').xpath('./@href').extract()[0]
        magnet = response.xpath('//a[@target="_blank" and @href]')[0].xpath('./@href').extract()[0]
        item['magnet'] = magnet
        yield item

    def parse(self, response):
      for sel in response.xpath('//*[@class="ulink"]'):
        name = sel.xpath('./text()').extract()[0]
        detailLink = sel.xpath('./@href').extract()[0]
        item = {} #RecruitItem()
        item['name']= name
        detail_url = "https://www.ygdy8.net/" + detailLink
        item['detail_url']= detail_url
        yield scrapy.Request(url=detail_url,callback=self.parse_detail,meta={'item':item})


