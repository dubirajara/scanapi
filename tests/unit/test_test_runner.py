import requests
from scanapi.test_runner import run_tests
from tests.unit.factories import APITreeFactory


class TestTestRunner:
    def test_passed(self, requests_mock):
        api = APITreeFactory(without_endpoints_minimal=True)
        request_node = api.request_nodes[0]
        requests_mock.get("http://test.com", text="request content")
        response = requests.get("http://test.com")

        assert run_tests(request_node, response).passed == True
