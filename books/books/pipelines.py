# -*- coding: utf-8 -*-

import pymysql as db
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BooksPipeline(object):
    def __init__(self):
        self.con = db.connect(user="root",passwd="biankun222",host="localhost",db="mysql",charset="utf8")
        self.cur = self.con.cursor()

    def process_item(self, item, spider):
        self.cur.execute(
            "insert into douban_books(id,book_name,book_star,book_pl,book_author,book_publish,book_date,book_price) values(NULL,%s,%s,%s,%s,%s,%s,%s)",
            (item['book_name'], item['book_star'], item['book_pl'], item['book_author'], item['book_publish'],
             item['book_date'], item['book_price']))
        self.con.commit()
        return item
