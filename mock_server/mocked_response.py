import requests


class MyMockedProductClass:
    def get_mocked_response(self, url):
        response = requests.get(url)
        return response.json()


body = {
    "brand": "Apple Test",
    "category": "smartphones",
    "description": "An apple mobile which is nothing like apple",
    "discountPercentage": 8.96,
    "price": 100000000,
    "rating": 5.69,
    "stock": 94,
    "title": "iPhone 13 Pro",
}


# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == "http://third-party-product-service":
        return MockResponse(body, 200)

    return MockResponse(None, 404)
