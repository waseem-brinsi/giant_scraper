import scrapy


class UdemycouponSpider(scrapy.Spider):
    name = "udemycoupon"
    allowed_domains = ["www.udemy.com"]
    start_urls = ["https://www.udemy.com"]

    def parse(self, response):
        pass
