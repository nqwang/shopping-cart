import yaml
import codecs
import records
import requests
import urllib3

import scrapy

from urllib import parse
import time
import re
import json

from bs4 import BeautifulSoup
from loguru import logger

Headers = {
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 "
                  "(KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}


def get_product(name, url):
    logger.info('Current product name is %s.' % name)
    logger.info('Current product url is %s' % url)

    try:
        html = requests.get(url, headers=Headers).text
        soap = BeautifulSoup(html, features='lxml')
        for item in soap.select('script'):
            if '_DATA_Detail' in item.text:
                data = item.text[19:-1]
                data = json.loads(data)
                price = data['mock']['price']['price']['priceText']
                logger.info('Current product price is %s' % price)

                break

    except Exception as err:
        pass


if __name__ == '__main__':
    with codecs.open('config.yml', 'r', encoding='utf-8') as yml:
        content = yaml.load(yml)
        for p in content['products']:
            get_product(p['name'], p['url'])
