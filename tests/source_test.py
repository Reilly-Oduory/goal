import unittest
from app.models import source

Source = source.Source

class SourceTest(unittest.TestCase):
    def setUp(self):
        self.new_source = Source("bbc-news", "BBC NEWS")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))
   