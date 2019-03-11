import unittest

from main import *

import configparser

API_KEY = "TESTAPIKEY"


class PhotosUrlTest(unittest.TestCase):
    def runTest(self):
        assert make_photos_url(
            "spirit", "TESTAPIKEY", 100) == "https://api.nasa.gov/mars-photos/api/v1/rovers/spirit/photos/?api_key=TESTAPIKEY&sol=100", 'wrong url structure'


class ManifestUrlTest(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
