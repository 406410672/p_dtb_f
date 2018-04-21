#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 10:36
# @Author  : HT
# @Site    : 
# @File    : HTMLParser.py
# @Software: PyCharm Community Edition
# @Describe: Desc
# @Issues  : Issues

from lxml import etree
from Socket.SocketProtocol import *
from Master.Task.TaskOperation import task_setting as ts
import re
import json



class HTMLParser(object):

    @classmethod
    def parser(cls, content, task_info):
        '''
        :param content:
        :param task_info:
        :return:
        '''
        task_id = task_info['task_id']
        items = list()
        if task_id == '1':
            items = cls._parser_id_1(content, task_info)
        elif task_id == '2':
            items = cls._parser_id_2(content, task_info)
        return items


    @classmethod
    def _parser_id_1(cls, html, task_info):
        parser_rule = ts.task_parse_rule.get('1')[0]
        pattern = parser_rule['pattern']
        parse_content = parser_rule['content']
        items = list()
        e_tree = etree.HTML(html)
        sub_elements = e_tree.xpath(pattern)

        for sub_element in sub_elements:

            c_n_pattern = parse_content['category_name']
            c_url_pattern = parse_content['url']
            c_ns = sub_element.xpath(c_n_pattern)
            c_urls = sub_element.xpath(c_url_pattern)
            for i in range(len(c_ns)):
                data = dict()
                data['category_name'] = c_ns[i]
                data['url'] = c_urls[i]
                items.append(data)

        return items

    @classmethod
    def _parser_id_2(cls, html, task_info):
        parser_rule = ts.task_parse_rule.get('2')[0]
        pattern = parser_rule['pattern']
        parse_content = parser_rule['content']
        try:
            result = re.findall(pattern, html.decode('utf-8'))[0]
        except Exception as error:
            print(error)
            print(html)
        result_dict = json.loads(result)

        page_name = result_dict['pageName']
        print(page_name)
        if page_name == 'spulist':
            spul = result_dict['mods']['grid']['data']['spus']
            return spul
        else:
            print('未处理:{}'.format(page_name))
            return []
        # return items



        # @classmethod
    # def _parser_xpath(cls, html, parser_rule):
    #     pattern = parser_rule['pattern']
    #     parse_content = parser_rule['content']
    #     items = list()
    #     e_tree = etree.HTML(html)
    #     e_trees = e_tree.xpath(pattern)
    #     print(e_trees)
    #     for element in e_trees:
    #         data = dict()
    #         for key, value in parse_content.items():
    #             try:
    #                 p_v = element.xpath(value)[0]
    #             except Exception as error:
    #                 p_v = ''
    #
    #             data[key] = p_v
    #         items.append(data)
    #     return items



if __name__ == '__main__':
    pass