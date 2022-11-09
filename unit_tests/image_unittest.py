import unittest
import requests


class WebsiteTest(unittest.TestCase):
    """unit test to weather website"""
    def setUp(self):
        """creating website request"""
        self.website_url = "http://localhost:80"
        self.request = requests.get(self.website_url)
        self.http_code = self.request.status_code

    def testReachable(self):
        """test http code return from website"""
        self.assertTrue(200 <= self.http_code <= 299)


if __name__ == '__main__':
    unittest.main()
