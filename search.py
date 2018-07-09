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

            print(self.get_argument('query'))

            loop = asyncio.get_event_loop()
            task = loop.create_task(self.get_datas(self.get_argument('query')))

            await asyncio.wait([
                task
            ])

        except Exception as e:

            self.set_status(status.HTTP_417_EXPECTATION_FAILED)

        r = self.order_xml(task.result().content)

        self.set_status(status.HTTP_200_OK)
        self.write({'r': r})


        # finally:

            # loop.close()


    async def get_datas(self, query):

        key = '03.669487626:77de25eb7ee1a29c63a97b764c25ff07'
        user = 'francasix'
        lan = 'en'

        url = 'https://yandex.com/search/xml?l10n=' + lan + '&user=' + user + '&key=' + key + '&query=' + query

        try:

           await asyncio.sleep(0.01)

           return requests.get(url)

        except Exception:

            self.set_status(status.HTTP_400_BAD_REQUEST)


    @staticmethod
    @task(name="order_xml")
    def order_xml(response):


        response_list = []
        root = ElementTree.fromstring(response)

        try:

            # through tree structure of response
            for element in root.iterfind('response/results/grouping/group/doc'):

                for sub_element in element:

                    if sub_element.tag == "url":
                        response_list.append({'url': sub_element.text})

        except Exception:

            self.set_status(status.HTTP_500_INTERNAL_SERVER_ERROR)

        return response_list
