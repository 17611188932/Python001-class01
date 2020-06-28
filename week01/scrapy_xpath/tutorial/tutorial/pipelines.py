# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class TutorialPipeline(object):
    def process_item(self, item, spider):
        film_name = item['film_name']
        film_gener = item['film_gener']
        plan_time = item['plan_time']
        with open('movie.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, )
            writer.writerow([film_name, film_gener, plan_time])
        return item
