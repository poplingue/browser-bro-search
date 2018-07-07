#!/usr/bin/env python3

from xml.etree import ElementTree
import requests
import tornado.web
from celery.decorators import task


class SearchEngine(tornado.web.RequestHandler):

    def get(self):
        self.get_datas(self.get_argument('query'))

    def get_datas(self, query):
        key = '03.669487626:77de25eb7ee1a29c63a97b764c25ff07'
        user = 'francasix'
        lan = 'en'

        url = 'https://yandex.com/search/xml?l10n=' + lan + '&user=' + user + '&key=' + key + '&query=' + query

        try:

            response = requests.get(url)

        except Exception:

            raise Exception('Request error https://yandex.com/search/xml')

        res = self.order_xml(response.content)
        self.write({'result': res})

    @staticmethod
    @task(name="order_xml")
    def order_xml(response):
        response_list = []
        root = ElementTree.fromstring(response)

        # through tree structure of response
        for element in root.iterfind('response/results/grouping/group/doc'):

            for sub_element in element:

                if sub_element.tag == "url":
                    response_list.append({'url': sub_element.text})

        return response_list
