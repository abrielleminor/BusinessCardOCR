# -*- coding: utf-8 -*-
"""
Test file for BusinessCardParser

@author: Abbie Holloway
"""
import nltk
nltk.download('names', quiet=True)
import unittest
from business_card_parser import BusinessCardParser

test_string_1 = '''ASYMMETRIK LTD
Mike Smith
Senior Software Engineer
(410)555-1234
msmith@asymmetrik.com'''

test_string_2 ='''Foobar Technologies
Analytic Developer
Lisa Haung
1234 Sentry Road
Columbia, MD 12345
Phone: 410-555-1234
Fax: 410-555-4321
lisa.haung@foobartech.com'''

test_string_3='''Arthur Wilson
Software Engineer
Decision & Security Technologies
ABC Technologies
123 North 11th Street
Suite 229
Arlington, VA 22209
Tel: +1 (703) 555-1259
Fax: +1 (703) 555-1200
awilson@abctech.com'''

test_string_4='''John William Smith, Jr.
Software Engineer
Tech Solutions
123 North 11th Street
Suite 229
Arlington, VA 22209
(410)555-1234 x123
jwsmithjr@techsolutions.com'''

test_string_5 ='''Creative Solutions
Software Developer
Bill O'Reilly
1234 Sentry Road
Columbia, MD 12345
Phone: 410-555-1234 ext. 555
Fax: 410-555-4321
bill.oreilly@creativesolns.com'''

test_string_6 ='''William Analytics
Data Scientist
Bill Smith
1234 Bill Road
Columbia, MD 12345
Phone: 410-555-1234
Fax: 410-555-4321
bill.smith@williamanalytics.net'''

        
class TestBusinessCardParserMethods(unittest.TestCase):
    
    def test_email_parser_case_1(self):
        email = BusinessCardParser.parse_email_address(test_string_1)
        self.assertEqual('msmith@asymmetrik.com', email)
        
    def test_email_parser_case_2(self):
        email = BusinessCardParser.parse_email_address(test_string_2)
        self.assertEqual('lisa.haung@foobartech.com', email)
        
    def test_name_parser_case_1(self):
        name = BusinessCardParser.parse_name(test_string_1)
        self.assertEqual('Mike Smith', name)

    def test_name_parser_case_2(self):
        name = BusinessCardParser.parse_name(test_string_4)
        self.assertEqual('John William Smith, Jr.', name)
        
    def test_name_parser_case_3(self):
        name = BusinessCardParser.parse_name(test_string_5)
        self.assertEqual('Bill O\'Reilly', name)
        
    def test_phone_parser_extension_case_1(self):
        phone = BusinessCardParser.parse_phone_number(test_string_4)
        self.assertEqual('4105551234x123', phone)
        
    def test_phone_parser_extension_case_2(self):
        phone = BusinessCardParser.parse_phone_number(test_string_5)
        self.assertEqual('4105551234x555', phone)
        
    def test_phone_parser_parens(self):
        phone = BusinessCardParser.parse_phone_number(test_string_1)
        self.assertEqual('4105551234', phone)  
        
    def test_phone_parser_prefix_one(self):
        phone = BusinessCardParser.parse_phone_number(test_string_3)
        self.assertEqual('17035551259', phone)
        
    def test_phone_parser_prefix_word(self):
        phone = BusinessCardParser.parse_phone_number(test_string_2)
        self.assertEqual('4105551234', phone)
        
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBusinessCardParserMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)

