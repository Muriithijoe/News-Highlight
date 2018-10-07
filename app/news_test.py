import unittest
from models import news
News = news.News

class NewsTest(unittest.Testcase):
    def setUp(self):
        self.new_news = New()

        def test_instance(self):
            self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':
    unittest.main()
