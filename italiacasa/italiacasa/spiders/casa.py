import scrapy
from ..items import ItaliacasaItem
from scrapy.loader import ItemLoader
# from scrapy.crawler import CrawlerProcess

class CasaSpider(scrapy.Spider):
    name = 'casa'
    allowed_domains = ['italiacasa.nl']
    start_urls = []

    def __init__(self, *args, **kwargs):
        url = 'https://italiacasa.nl/aanbod/?start='

        for page in range(100, 890, 10): # 940
            self.start_urls.append(url + str(page))

    def parse(self, response):
        for link in response.css('#searchWrapper > div > div::attr(data-link)'):
            yield response.follow(link.get(), callback=self.parse_casas)

    def parse_casas(self, response):
        for casas in response.css('html'):
            l = ItemLoader(item = ItaliacasaItem(), selector=casas)

            latitude_raw = casas.css('body > script::text').re(r'\d{1,2}\.\d{1,2}')[0]
            longitude_raw = casas.css('body > script::text').re(r'\d{1,2}\.\d{1,2}')[1]
            soort_raw = casas.css('body > div > div > section > div > div > div.panel.list > ul > li ::text').get()
            status_raw = casas.css('body > div > div > section > div > div > div.panel.list > ul > li ::text').getall()[-1]
            perceel_raw = casas.css('body > div > div > section > div > div > span.icon.icon-boom ::text').get()

            l.add_css('content_id', 'body > div > div > section > div > div > span.ref > span')
            l.add_css('plaats', 'body > div > div > section.house.video-visual > div > div > h1')
            l.add_css('provincie', 'body > div > div > section.house.video-visual > div > div > h2')
            l.add_css('woonoppervlak', 'body > div > div > section > div > div > span.icon.icon-huis')
            l.add_value('perceel', perceel_raw)
            l.add_css('prijs', 'body > div > div > section > div > div.medium-4.medium-push-8.columns > div.panel.info > span')
            l.add_value('latitude', latitude_raw)
            l.add_value('longitude', longitude_raw)
            l.add_value('soort', soort_raw)
            l.add_value('status', status_raw)
            l.add_css('huis_url', 'body > div > div > header > nav > section > ul.right.show-for-large-up.langselect > li > ul > li > a::attr(href)')
            l.add_css('timestamp', 'head > meta[property="og:updated_time"] ::attr(content)')

            yield l.load_item()

# process = CrawlerProcess()
# process.crawl(CasaSpider)
# process.start()
