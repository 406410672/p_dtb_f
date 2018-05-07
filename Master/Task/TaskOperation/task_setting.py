#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/20 11:36
# @Author  : HT
# @Site    : 
# @File    : task_setting.py
# @Software: PyCharm Community Edition
# @Describe: Desc
# @Issues  : Issues


#任务描述
'''
task_id : 1
淘宝商品分类获取_数码家电 一级分类
获取的任务格式 主要数据
{
   "task_name": "淘宝商品信息获取",
    "task_id" : '',   #任务id
    'items' ： [{'url':''}],
    'task_nums' : 1 #返回的任务个数   如果没有任务，则为0
}
上传的格式
{

    'client_id'：'',
    'request_time'：    #时间戳的形式,
    'task_id' :'' ,     #任务id
    'items' :[{'url': '',
                'data':[{'category':'',url:''}]}]

    }
'''
'''
task_id : 2
淘宝商品分类获取_数码家电 二级分类
获取的任务格式 主要数据
{
   "task_name": "淘宝商品二级分类",
    "task_id" : '2',  
    'items' ： [{'url':'','category_name':'[]'}],
    'task_nums' : 1 #返回的任务个数   如果没有任务，则为0
}
上传的格式
{
    'client_id'：'',
    'request_time'：    #时间戳的形式,
    'task_id' :'' ,     #任务id
    'items' :[{'url': '',
                'category_name',''
                'data':[{},{}]}]

    }
'''
'''
task_id : 3
淘宝商品详情获取
获取的任务格式 主要数据
{
   "task_name": "淘宝商品详情获取",
    "task_id" : '3',  
    'items' ： [{'url':'','category_name':'[]'}],
    'task_nums' : 1 #返回的任务个数   如果没有任务，则为0
}
上传的格式
{
    'client_id'：'',
    'request_time'：    #时间戳的形式,
    'task_id' :'' ,     #任务id
    'items' :[{'nid': '',
                'category_name',''
                'data':[{},{}]}]

    }
'''




from Master.Task import Const as C
# get_task = ['_get_task_1','_get_task_2']
get_task = ['_get_task_3']




#任务ID对应解析规则
task_parse_rule = {
    '1' : [{
      "type" : "xpath",
      "priority" : 1 ,
      "pattern" : '//*[text()="家电办公" or text()="手机数码"]',
      "content" : {"category_name":'../ul/li/div/*[@class="category-name"]/text()',
                   "url":'../ul/li/div/*[@class="category-name"]/@href'}}],
    '2' : [{
      "type" : "regular",
      "priority" : 1 ,
      "pattern" : 'g_page_config = ({.*})',
      "content" : {}}]}

#任务ID对应存储规则
task_storage_rule = {'1' : {
                             "handler" : "master",
                             "target" : "mongodb",
                             "db" : "taobao",
                             "table":"taobao_seed"
                            },
                    '2' : {
                             "handler" : "master",
                             "target" : "mongodb",
                             "db" : "taobao",
                             "table":"taobao_item"
                            }
}