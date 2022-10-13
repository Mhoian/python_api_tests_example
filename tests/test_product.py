from unittest import mock

import pytest

from api_requests.api import Product
from mock_server.mocked_response import mocked_requests_get, MyMockedProductClass

from schemas.product_schema import valid_schema

BASE_URL = "http://localhost:3000"


class TestProduct:
    def test_get_product(self):
        response = Product(base_url=BASE_URL).get_product()

        assert response.http_status == 200, f"Actual status code: {response.http_status} != 200"
        assert response.content[1]["title"] == "iPhone X", f"{response.content.title()}"

    @pytest.mark.parametrize(
        "body",
        [
            {
                'title': 'iPhone 13 Pro',
                'description': 'An apple mobile which is nothing like apple',
                'price': 100000,
                'discountPercentage': 8.96,
                'rating': 5.69,
                'stock': 94,
                'brand': 'Apple',
                'category': 'smartphones'
            }
        ]
    )
    def test_add_product(self, body):
        response = Product(base_url=BASE_URL).add_product(body=body, schema=valid_schema)
        content = response.content

        assert response.http_status == 201, f"Actual status code: {response.http_status} != 201"
        assert content["title"] == "iPhone 13 Pro", f"{content['title']}"
        assert content["price"] == 100000, f"{content['price']}"

    @mock.patch('mock_server.mocked_response.requests.get', side_effect=mocked_requests_get)
    def test_add_product_with_mock(self, mock_server):
        mgc = MyMockedProductClass()
        json_body = mgc.get_mocked_response("http://third-party-product-service")

        response = Product(base_url=BASE_URL).add_product(body=json_body, schema=valid_schema)
        content = response.content

        assert response.http_status == 201, f"Actual status code: {response.http_status} != 201"
        assert content["title"] == "iPhone 13 Pro", f"{content['title']}"
        assert content["price"] == 100000000, f"{content['price']}"