import unittest
from models import articles
Articles = articles.Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('cnn','Mitchell Clark', 'Whatsapp and its advantages','Microsoft update','"https://www.theverge.com/2021/8/6/22613617/microsoft-xbox-night-mode-feature-dim-screen-controller-led','https://cdn','2021-08-05')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))


if __name__ == '__main__':
    unittest.main()