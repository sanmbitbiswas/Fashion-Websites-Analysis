import scrapy
from urllib.parse import urlparse

class TextSpider(scrapy.Spider):
    name = 'text_spider'
    custom_settings = {
        'CONCURRENT_REQUESTS': 1,
        'DOWNLOAD_DELAY': 3,
        'USER_AGENT': 'custom user agent' 'http://www.example.com',  # Add the desired user agent string
    
    }

    def __init__(self, start_url='', *args, **kwargs):
        super(TextSpider, self).__init__(*args, **kwargs)
        self.start_urls = [start_url]
        self.allowed_domains = [urlparse(start_url).netloc]
        self.file = open('website_text.txt', 'w')

    def parse(self, response):
        # Get all text content within specified tags
        text_elements = response.css('p::text, h1::text, h2::text, h3::text, h4::text, h5::text, h6::text, a::text, li::text, span::text, strong::text, em::text').getall()
        
        for text in text_elements:
            self.file.write(text + '\n')

        # Recursive call to follow links
        for href in response.css('a::attr(href)'):
            yield response.follow(href, self.parse)

    def close(self, reason):
        self.file.close()




# You can instantiate the Spider with the website you want to scrape
# spider = TextSpider(start_url='https://example.com')
# spider.start_requests()
# scrapy runspider text_spider.py -a start_url=https://www.perniaspopupshop.com/


