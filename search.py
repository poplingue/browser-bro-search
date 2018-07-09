#!/usr/bin/env python3
import asyncio
import status

from xml.etree import ElementTree
import requests
import tornado.web
from celery.decorators import task


class SearchEngine(tornado.web.RequestHandler):

    SUPPORTED_METHODS = ("GET")

    async def get(self):

        try:
            # await asyncio.sleep(0.01)

            loop = asyncio.get_event_loop()
            task = loop.create_task(self.get_datas(self.get_argument('query')))

            await asyncio.wait([
                task
            ])

            r = self.order_xml(task.result().content)

            self.set_status(status.HTTP_200_OK)
            self.write({'r': r})

        except Exception as e:

            self.set_status(status.HTTP_417_EXPECTATION_FAILED)
            print('Error {}'.format(e))

        # finally:

            # loop.close()


    async def get_datas(self, query):
        print('get_datas')
        key = '03.669487626:77de25eb7ee1a29c63a97b764c25ff07'
        user = 'francasix'
        lan = 'en'

        url = 'https://yandex.com/search/xml?l10n=' + lan + '&user=' + user + '&key=' + key + '&query=' + query

        try:

           print('request url 0')
           await asyncio.sleep(0.01)
           print('request url 1')
           return requests.get(url)

        except Exception:

            raise Exception('Request error https://yandex.com/search/xml')

        # res = self.order_xml(response.content)
        # self.write({'result': res})

    @staticmethod
    @task(name="order_xml")
    def order_xml(response):
        print('order_xml')
        response_list = []
        root = ElementTree.fromstring(response)

        # through tree structure of response
        for element in root.iterfind('response/results/grouping/group/doc'):

            for sub_element in element:

                if sub_element.tag == "url":
                    response_list.append({'url': sub_element.text})

        return response_list
