# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

class ItaliacasaItem(scrapy.Item):
    # define the fields for your item here like:
    content_id = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    plaats = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    provincie = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    woonoppervlak = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    perceel = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    prijs = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    latitude = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    longitude = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    soort = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    status = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    huis_url = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
    timestamp = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
