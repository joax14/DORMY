import scrapy

class DormySpider(scrapy.Spider):
    name = "dormy"
    start_urls = ['https://www.dormy.ph/']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        amenities = response.css('div.w-\\[100px\\].border-2.rounded-\\[15px\\] p::text').getall()
        print("Amenities:", amenities)
        for amenity in amenities:
            yield {
                'amenity': amenity.strip(),
            }
