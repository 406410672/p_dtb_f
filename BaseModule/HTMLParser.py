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
from Exceptions.ParserException import TaoBaoItemParserException
from Master.Task.TaskOperation import task_setting as ts
from BaseModule.StrHandle import *

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
        elif task_id == '3':
            items = cls._parser_id_3(content, task_info)
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

    @classmethod
    def _parser_id_3(cls, html, task_info):
        def _get_field_name(regex, content):
            result = re.findall(regex, content)
            if len(result) > 0:
                return result[0]
            else:
                return ''

        g_config = re.findall(r'g_config =([\s\S]*?};)', html)
        valItemInfo = re.findall(r'valItemInfo\s*:([\s\S]*?)}\);', html)
        if len(g_config) == 0 and len(valItemInfo) == 0:
            raise TaoBaoItemParserException()

        item_config = dict()
        if len(g_config) > 0:
            content = g_config[0]
            # sibUrl = re.findall(r"sibUrl\s*?:\s'(.*)',", content)[0]
            sibUrl = _get_field_name(r"sibUrl\s*?:\s'(.*)',", content)
            descUrl = _get_field_name(r"descUrl\s*?:\s(.*)',", content)
            counterApi = _get_field_name(r"counterApi\s*:\s'(.*)',", content)
            rateCounterApi = _get_field_name(r"rateCounterApi\s*:\s'(.*)',", content)
            shopName = _get_field_name(r"shopName\s*?:\s'(.*)',", content)
            shopName = convert_unicodestr2str(shopName)
            title = _get_field_name(r"title\s*?:\s'(.*)',", content)
            title = convert_unicodestr2str(title)
            itemId = _get_field_name(r"itemId\s*?:\s'(.*)',", content)
            item_config['descUrl'] = descUrl
            item_config['sibUrl'] = sibUrl
            item_config['counterApi'] = counterApi
            item_config['rateCounterApi'] = rateCounterApi
            item_config['shopName'] = shopName
            item_config['title'] = title
            item_config['itemId'] = itemId

        try:
            if len(valItemInfo) > 0:
                tree = etree.HTML(html)
                content = valItemInfo[0]
                skuMap = _get_field_name(r"skuMap\s*:\s(.*)", content)
                skuMap = json.loads(skuMap)
                propertyMemoMap = _get_field_name(r"propertyMemoMap[\s\S]*:\s(.*)", content)
                item_config['skuMap'] = skuMap
                item_config['propertyMemoMap'] = json.loads(propertyMemoMap)

                for data_id, info in skuMap.items():
                    try:
                        data_id = data_id.replace(';', '')
                        xpath = '//*[@data-value="{}"]'.format(data_id)
                        elements = tree.xpath(xpath)
                        if len(elements) > 0:
                            element = elements[0]
                            info['title'] = element.xpath('.//span/text()')[0]
                            info['background'] = element.xpath('./a/@style')[0]
                    except Exception as error:
                        print('子类图片与文字解析出错')
                # print('有子类')
                print('子类数量,', len(skuMap))
        except Exception as error:
            print('没有子类或者解析出错', error)
        return item_config


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