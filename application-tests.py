import unittest
import application
from application import app,model
from  mock import *
from datetime import datetime

globalmock = 0

mock_time = Mock()
mock_time_v2 = Mock()
mock_time.return_value = datetime(2012, 1, 1, 10, 10, 10)
mock_time_v2.side_effect = [datetime(2012, 1, 1, 10, 10, 10),datetime(2012, 1, 1, 10, 5, 10),datetime(2011, 1, 1, 10, 10, 10),datetime(2012, 1, 1, 10, 11, 10)]


class BasicTestCase(unittest.TestCase):
    '''
    def test_get(self):
        """inital test. ensure flask was set up correctly"""
        tester = app.test_client(self)
        response = tester.get('/palindromes/api/v1.0/get_palindromes')
        self.assertEqual(response.status_code, 200)
    '''
    #test 1
    def test_checkPalindromeTrue(self):
        self.assertEqual(application.isPalindrome("Dammit I'm Mad"),True)

    # test 2
    def test_checkPalindromeFalse(self):
        self.assertEqual(application.isPalindrome("Dammit I am Mad"), False)

    # test 3
    @patch('model.Palindrome.get_currenttime',mock_time)
    def test_checkAddingNewValue(self):
        expectedoutput = {
            'phrase': 'mam',
            'time': datetime(2012, 1, 1, 10, 10, 10)
        }
        temp = model.Palindrome()
        temp.add('mam')
        self.assertEqual(temp.phrases[0], expectedoutput)

    # test 4
    @patch('model.Palindrome.get_currenttime',mock_time)
    def test_check_existingPhrase_ExistingValue(self):
        temp = model.Palindrome()
        temp.add('mam')
        expectedoutput = {
            'phrase': 'mam',
            'time': datetime(2012, 1, 1, 10, 10, 10)
        }
        self.assertEqual(temp.existingPhrase('mam')[0],expectedoutput )

    # test 5
    @patch('model.Palindrome.get_currenttime',mock_time)
    def test_check_existingPhrase_NewValue(self):
        temp = model.Palindrome()
        temp.add('mam')
        self.assertEqual(temp.existingPhrase('mamam'),[] )

    # test 6
    # check that replace the existing value without adding a new entry
    @patch('model.Palindrome.get_currenttime',mock_time)
    def test_checkAddingMultipleValues(self):
        expectedoutput = [
            {
                'phrase': 'mamam',
                'time': datetime(2012, 1, 1, 10, 10, 10)
            },
        {
            'phrase': 'mam',
            'time': datetime(2012, 1, 1, 10, 10, 10)
        }]
        temp = model.Palindrome()
        temp.add('mam')
        temp.add('mamam')
        temp.add('mam')
        self.assertEqual(temp.phrases, expectedoutput)

    #test 7
    @patch('model.Palindrome.get_currenttime', mock_time_v2)
    def test_checkAddingMultipleValues_time(self):
        global globalmock
        expectedoutput = [
            {
                'phrase': 'mam',
                'time': datetime(2012, 1, 1, 10, 10, 10)
            },
            {
                'phrase': 'mamam',
                'time': datetime(2012, 1, 1, 10, 5, 10)
            }]
        temp = model.Palindrome()
        temp.add('mam')
        temp.add('mamam')
        temp.add('0')
        self.assertEqual(temp.getPhrases(), expectedoutput)



    if __name__ == '__main__':
        unittest.main()
