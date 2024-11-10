import scrapy


class FoagroupSpider(scrapy.Spider):
    name = "foagroup"
    allowed_domains = ["www.foagroup.com"]
    start_urls = ["https://www.foagroup.com/customer/account/login/"]

    def parse(self, response):
        token= response.xpath(".//input[@name='form_key']/@value").extract_first()
        # print(token)
        yield scrapy.FormRequest('https://www.foagroup.com/customer/account/loginPost/',
                                 formdata={'form_key':token,
                                           # form_key: yqVixmlhRp8k6I2r
                                           "login[username]": "avijit4000@gmail.com",
                                           "login[password]": "Biswas.123",
                                           "send": ""
                                           },
                                 callback=self.startscraper)

    def startscraper(self.response):
        yield scrapy.Request("https://www.foagroup.com/customer/account/" , callback =self.verifylogin)

    def verifylogin(self,response):
        print(response.test)