import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    def setUp(self):
        self.new_news = News({"bbc-new":"BBC News"},"BBC News", "Pakistan train accident", "description", "http://www.bbc.co.uk/news/world-asia-57380615", "https://ichef.bbci.co.uk/news/1024/branded_news/35AE/production/_118824731_pakistanmapghotki.png", "2021-06-07T04:52:23.0389688Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':
    unittest.main()