import requests
from bs4 import BeautifulSoup
import yaml
import logging
import json

log = logging.getLogger(__name__)


class Mathem:

    def __init__(self, config_file=None):
        """
        :param config_file: A path to a config file in yaml format.
        See mathemlib_config_example.yaml
        """

        self.user = str()
        self.password = str()

        if config_file:
            with open(config_file) as f:
                self.config = yaml.load(f)
            self.user = self.config['username']
            self.password = self.config['password']


        self.session = None
        self.orders = list()
        self.mathem_url = 'https://mathem.se'

    def login(self):
        """
        A method to login to your account on mathem.se.
        The session will be stored in self.session.
        """
        payload = {
            'username': self.user,
            'Password': self.password,
        }

        self.session = requests.session()
        response = self.session.post('{0}/Account/LogIn'.format(self.mathem_url), data=payload)

        try:
            json_response = response.json()
        except ValueError:
            log.debug('Response text: {0}'.format(response.text))
            log.critical('Login failed')
            raise
        except:
            log.critical('Unhandled exeception')
            raise

        if json_response.get('Success'):
            log.info('Login successful')
            return 'logged in'
        else:
            log.critical('Login failed')
            log.debug('Content of response:{0}'.format(json_response))
            raise Exception('Login failed')

    def get_orders(self, limit=10):
        """
        :param limit: Stop at this many orders
        :return: Returns a list of order IDs
        """
        orders_raw = self.session.get('{0}/min-sida/ordrar'.format(self.mathem_url))
        orders_bs4 = BeautifulSoup(orders_raw.content, 'html.parser')

        order_dict = dict()
        for link in orders_bs4.find_all('a'):
            if link.get('href') and link.get('href').startswith('/min-sida/ordrar/'):
                order_dict[link.get('href').replace('/min-sida/ordrar/', '')] = {}
            if len(order_dict) >= limit:
                break

        return order_dict

    def get_info(self, order_id):
        """
        :param order_id: The ID of the order to get info from
        :return: A dict with various data about the order
        """
        return "Not implemented yet"
        #order_raw = self.session.get(
        #    '{url}/{order_id}'.format(url=self.my_orders_url, order_id=order_id)
        #)
        #order_bs4 = BeautifulSoup(order_raw.content, 'html.parser')
        #order_tables = order_bs4.find_all('table')
        #order_rows = order_tables[0].find_all('tr')
        #order_data = list()
        #for row in order_rows:
        #    cols = row.find_all('td')
        #    cols = [ele.text.strip() for ele in cols]
        #    order_data.append([ele for ele in cols if ele])

        #order_dict = dict()
        #for order_list in order_data:
        #    if 'Status:' in order_list:
        #        # The ugliest line in python history
        #        order_dict['Status'] = order_list[1].split('\n')[0].rstrip('\r')

        #    if 'Orderdatum:' in order_list:
        #        order_dict['Order date'] = order_list[1]

        #    if 'Leveransdatum:' in order_list:
        #        order_dict['Delivery date'] = order_list[1]

        #    if 'Planerad leveranstid:' in order_list:
        #        order_dict['Expected delivery'] = order_list[1]

        #return order_dict
