import scrapy


class LearnviralComSpider(scrapy.Spider):
    name = "learnviral_com"
    allowed_domains = ["udemycoupon.learnviral.com"]
    start_urls = ["https://udemycoupon.learnviral.com"]

    def parse(self, response):
        pass
