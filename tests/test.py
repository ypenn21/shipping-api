import unittest

from data_model import Package
from connect_connector import SessionMaker

from main import app

class TestPackage(unittest.TestCase):

    def setUp(self):
        self.session_maker = SessionMaker()

    def tearDown(self):
        self.session_maker.close()

    def test_get_package(self):
        """Test the `get_package()` function."""

if __name__ == "__main__":
    unittest.main()
