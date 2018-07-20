#!/usr/bin/env python3
from xml.etree import ElementTree

import requests
import tornado.web


class SearchEngine(tornado.web.RequestHandler):

    def get(self, id):

        r = self.get_datas(self.get_argument('query'))

        self.write({'r': r})

    def get_datas(self, query):

        key = '03.669487626:77de25eb7ee1a29c63a97b764c25ff07'
        user = 'francasix'
        lan = 'en'

        url = 'https://yandex.com/search/xml?l10n=' + lan + '&user=' + user + '&key=' + key + '&query=' + query

        return self.order_xml(requests.get(url).content)

    def order_xml(self, response):

        response_list = []
        root = ElementTree.fromstring(response)

        # through tree structure of response
        for element in root.iterfind('response/results/grouping/group/doc'):

            for sub_element in element:

                if sub_element.tag == "url":
                    response_list.append({'url': sub_element.text})

        return response_list
