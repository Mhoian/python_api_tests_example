import logging

from jsonschema import validate
from common.models import ResponseModel
from common.custom_requests import Client

logger = logging.getLogger("api")


class Product:
    def __init__(self, base_url):
        self.base_url = base_url
        self.client = Client()

    GET_PRODUCTS = '/products'
    ADD_PRODUCT = '/products'

    def get_product(self):
        """
              https://localhost:3000/products
        """
        response = self.client.custom_request("GET", f"{self.base_url}{self.GET_PRODUCTS}")
        logger.info(response.text)
        return ResponseModel(http_status=response.status_code, content=response.json(), text=response.text)

    def add_product(self, body: dict, schema: dict):
        """
              https://localhost:3000/products
        """
        response = self.client.custom_request("POST", f"{self.base_url}{self.ADD_PRODUCT}", json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(http_status=response.status_code, content=response.json(), text=response.text)
