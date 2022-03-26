# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class ItaliacasaPipeline:
    def __init__(self):
        self.con = sqlite3.connect('italiacasas.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS casas(
        content_id REAL,
        plaats TEXT,
        provincie TEXT,
        woonoppervlak TEXT,
        perceel REAL,
        prijs TEXT,
        latitude TEXT,
        longitude TEXT,
        soort TEXT,
        status TEXT,
        huis_url TEXT,
        timestamp TEXT,
        PRIMARY KEY(content_id, status)
        )""")

    def process_item(self, item, spider):
        self.cur.execute("""INSERT OR IGNORE INTO casas VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
                             (item['content_id'], item['plaats'], item['provincie'], item['woonoppervlak'],
                              item['perceel'], item['prijs'], item['latitude'], item['longitude'], item['soort'],
                              item['status'], item['huis_url'], item['timestamp'],))
        self.con.commit()
        return item
