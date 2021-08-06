import unittest
from models import sources
Sources = sources.Sources

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources('bbc news')

        def test_instance(self):
        self.assertTrur(isinstance(new_source,Sources))


    if __name__ == '__main__':
        unittest.main()