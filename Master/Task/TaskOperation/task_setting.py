#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/20 11:36
# @Author  : HT
# @Site    : 
# @File    : task_setting.py
# @Software: PyCharm Community Edition
# @Describe: Desc
# @Issues  : Issues




task = ['get_taobao_task']




#任务ID对应解析规则
task_parse_rule = {'1' : [{
      "type" : "xpath",
      "priority" : 1 ,
      "pattern" : '//*[text()="家电办公" or text()="手机数码"]',
      "content" : {"category_name":'../ul/li/div/*[@class="category-name"]/text()',
                   "category_url":'../ul/li/div/*[@class="category-name"]/@href'}}]
                  }
#任务ID对应存储规则
task_storage_rule = {'1' : {
                             "handler" : "master",
                             "target" : "mongodb",
                             "db" : "taobao",
                             "table":"taobao_seed"
                            }
}