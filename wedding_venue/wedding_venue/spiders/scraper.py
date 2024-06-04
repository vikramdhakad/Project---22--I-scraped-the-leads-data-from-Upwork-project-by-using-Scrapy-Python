import scrapy


class ScraperSpider(scrapy.Spider):
    name = "scraper"
    allowed_domains = ["www.wedmegood.com"]
    start_urls = ["https://www.wedmegood.com/vendors/jodhpur/wedding-venues/"]

    def parse(self, response):
        for url in response.xpath("//div[@class='vendor-card extra-radius']/a"):
            link = url.xpath("@href").get()
            ab_link = response.urljoin(link)
            yield response.follow(url=ab_link,callback=self.data_parse)
            
            
    def data_parse(self,response):
        yield{
            "Venue Name": response.xpath("//h1/text()").get(),
            "Veg Plate price": response.xpath("(//p[@class='h5 ']/text())[1]").get(),
            "Non-Veg Plate price": response.xpath("(//p[@class='h5 ']/text())[2]").get(),
            "Location": response.xpath("(//p[@class='text-tertiary']/text())[1]").get()
        }
