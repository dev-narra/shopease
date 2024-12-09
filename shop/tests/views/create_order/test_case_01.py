"""
# TODO: Update test case description
"""
import pytest
from dsu.test_cases.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX, URL_BASE_PATH


class TestCase01CreateOrderAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    URL_BASE_PATH = URL_BASE_PATH
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {}

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {
            'id':
            'string',
            'products': [{
                'name': 'string',
                'description': 'string',
                'price': 1.1,
                'mfg_date': 'string',
                'exp_date': 'string',
                'stock_quantity': 1.1,
                'id': 1
            }],
            'customer': {
                'id': 'string',
                'name': 'string',
                'email': 'string',
                'phone': 'string',
                'address': 'string'
            },
            'payment': {
                'id': 'string',
                'order_id': 'string',
                'amount': 1.1,
                'method': 'Card',
                'status': 'Success',
                'transaction_date': '2099-12-31 00:00:00'
            },
            'status':
            'Pending',
            'expected_delivery_date':
            '2099-12-31',
            'order_datetime':
            '2099-12-31 00:00:00'
        }
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
