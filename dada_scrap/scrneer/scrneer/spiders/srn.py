import scrapy


class SrnSpider(scrapy.Spider):
    name = "srn"
    allowed_domains = ["www.screener.in"]
    start_urls = ["https://www.screener.in/company/BDL/"]

    def parse(self, response):
        box=response.xpath('//li[@class="flex flex-space-between"]')
        # print(len(box))
        for bo in box:
            nem=bo.xpath("./span[1]/text()").getall()
            # value=bo.xpath("./span[2]/span/text()").getall()
            yield {
                "nem":nem
                "value":value
            }