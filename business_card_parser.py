# -*- coding: utf-8 -*-
"""
BusinessCardParser

@author: Abbie Holloway
"""
from contact_info import ContactInfo
import re
from nltk.corpus import names as nltk_names


class BusinessCardParser:
    """
    The Business Card Parser parses the relevant information from a 
    business card. 
    """
    
    ignore_phone_types = ['fax', '(f)']
    # common first names
    first_names = set(nltk_names.words('male.txt') + nltk_names.words('female.txt'))
    # a short list of common words in company names
    business_names = ['Analytics', 'Corporation', 'Engineering', 'Incorporated', 'Innovations', 
                      'LLC', 'LTD', 'Software', 'Solutions', 'Systems', 'Technologies', 'Technology']
    
    
    @staticmethod
    def parse_name(document):
        """
        parse_name - parse a person's name from a string of text from a 
            business card. Assumes the person's first name is either a common
            name or a shortened substring of a common name
                    
        Args:
            document (str): The text of a business card.
            
        Returns:
            name: The name from the card or None if no name found
        """
        document = document.split('\n')
        # keep only two word names and remove any lines containg numbers
        potential_names = [line for line in document if
                           re.findall('^[a-z]+[a-z ]*.?[a-z ,\'-]+', line, re.IGNORECASE) and not re.search('\d', line)]
        name = []

        for pn in potential_names:
            # skip any lines containing business words
            if any(business_name in pn for business_name in BusinessCardParser.business_names):
                continue
            
            first_name = pn.split()[0].lower()
            if any(first_name in fn.lower() for fn in BusinessCardParser.first_names):
                name.append(pn)
        
        
        if len(name) == 0:
            return None
        
        return name[0]
        
        
    @staticmethod
    def parse_phone_number(document):
        """
        parse_phone_number - parse a person's phone number from a string of 
            text from a business card. Assumes there is only one valid phone
            number, otherwise returns the first listed. Will keep phone 
            extensions as show them as x### at the end of the phone number
        
        Args:
            document (str): The text of a business card.
            
        Returns:
            phone_number: The phone number from the card or None if no number 
                          found.
        """
        phone_num_regex = '[^\n]*\+?\d?[^\S\n\t]?\(?\d{3}\)?[ -]?\d{3}[ -]?\d{4}[ ext\.\d]*'
        phone_numbers = re.findall(phone_num_regex, document)
        
        # for all phone numbers found, remove ignored types
        for p_num in phone_numbers:
            if any(phone_type in p_num.lower() for phone_type in BusinessCardParser.ignore_phone_types):
                phone_numbers.remove(p_num)
        
        # if there are no phone numbers found or valid, return None
        if len(phone_numbers) == 0:
            return None
        
        # remove all non-digit characters except for x in case of extensions
        phone_number = re.sub('[^\dx]*', '', phone_numbers[0])
        
        return phone_number
    
    
    @staticmethod
    def parse_email_address(document):
        """
        parse_email_address - parse a person's email address from a string of 
            text from a business card. Assumes there is only one valid email, 
            otherwise returns the first listed.
        
        Args:
            document (str): The text of a business card.
            
        Returns:
            email: The email address from the card or None if no number 
                          found.
        """
        email_regex = '[\w\.-]+@[\w\.-]+\.\w{2,4}'
        email = re.findall(email_regex, document)
        
        if len(email) == 0:
            return None
        
        return email[0]
    
    
    @staticmethod
    def getContactInfo(document):
        """
        getContactInfo - Create and return a ContactInfo instance with the
            name, phone number and email address from the business card text.
        
        Args:
            document (str): The text of a business card.
            
        Returns:
            ContactInfo - An instance of the ContactInfo class with the
            name, phone number and email address from the business card text.   
        """
        name = BusinessCardParser.parse_name(document)
        phone_number = BusinessCardParser.parse_phone_number(document)
        email_address = BusinessCardParser.parse_email_address(document)

        return ContactInfo(name, phone_number, email_address)

