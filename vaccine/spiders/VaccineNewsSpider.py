#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
import json
import re
import hashlib
from Crypto.Hash import MD5
from vaccine.items import VaccineNewsItem


class VaccineNewsSpider(scrapy.Spider):
    name = "spiderNews"
    allowed_domains = ['so.news.cn', 'm.xinhuanet.com']
    url_format = "http://so.news.cn/getNews?keyword=%s&curPage=%s&sortField=0&searchFields=1&lang=cn"

    def start_requests(self):
        keywords = set()
        try:
            f = open('vaccine/vaccine_name.txt', 'r')
            for line in f.readlines():
                line = line.strip('\n')  # 去除换行符号
                keywords.add(line)
        finally:
            if f:
                f.close()
        
        for keyword in keywords:
            print(keyword)
            url = self.url_format % (keyword, 1)
            print(url)
            yield scrapy.Request(url, self.parse_json)

        # yield scrapy.Request('http://so.news.cn/getNews?keyword=乙肝疫苗&curPage=%s&sortField=0&searchFields=1&lang=cn', self.parse_json)

    def parse_json(self, response):
        print("aa")
        print(response.body)
        newJson = json.loads(response.body) 
        print(newJson['code'])
        newContent = newJson['content']
        results = newContent['results']
        pageSize = newContent['pageCount']
        curPage = newContent['curPage']
        keyWord = newContent['keyword']
        newSets = set()
        for result in results:
            url = result['url']
            if 'm.xinhuanet.com' in url and result['des']:
                html_remove = re.compile(r'<[^>]+>', re.S)  # 构建匹配模式
                # dd = dr.sub('', string) # 去除html标签
                title = html_remove.sub('', result['title'])
                print("title"+title)
                vaccineNewsItem = VaccineNewsItem()
                vaccineNewsItem['title'] = title.lstrip()
                vaccineNewsItem['from_url'] = url
                # result['sitename']
                vaccineNewsItem['from_source'] = '新华网'
                vaccineNewsItem['summary'] = result['des'].lstrip()
                vaccineNewsItem['create_date'] = result['pubtime']
                vaccineNewsItem['md5'] = self.md5_str(str=title)
                vaccineNewsItem['keyword'] = keyWord
                newSets.add(vaccineNewsItem)
                yield vaccineNewsItem
        if curPage < pageSize:
            curPage = curPage+1
            url = self.url_format % (keyWord, curPage)
            print(url)
            yield scrapy.Request(url, callback=self.parse_json)
    
    def md5_str(self, str):
        m = MD5.new()
        m.update(str.encode("utf-8"))
        return m.hexdigest()

  




# title = scrapy.Field()
#    create_date = scrapy.Field()
#    update_date = scrapy.Field()
#    from_sorce = scrapy.Field()
#    from_url = scrapy.Field()
#    content = scrapy.Field()
#   summary = scrapy.Field()