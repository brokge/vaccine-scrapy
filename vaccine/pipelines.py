#!/usr/bin/python
#  -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import pymysql
import pymysql.cursors


class VaccinePipeline(object):
    def process_item(self, item, spider):
        return item


class MySQLPipeLine(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host="127.0.0.1",
            # 数据库地址
            port=3306,
            db="dbcontent",
            user='root',
            passwd='123456',
            charset='utf8',
            use_unicode=True
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        self.cursor.execute(
            """insert into news(title,from_source,create_date,from_url,md5,summary,keyword) value (%s,%s,%s,%s,%s,%s,%s)""",
            (item['title'], item['from_source'], item['create_date'], item['from_url'], item['md5'], item['summary'], item['keyword']))
        # 提交sql 语句
        self.connect.commit()
        return item  # 必须实现返回

    def close_spider(self, spider):
        self.connect.close()