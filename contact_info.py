# -*- coding: utf-8 -*-
"""
ContactInfo

@author: Abbie Holloway
"""

class ContactInfo:
    """
    The ContactInfo object contains the name, phone number and email address
    for a person.
    """
    
    def __init__(self, name, phone_number, email_address):
        self.name = name
        self.phone_number = phone_number
        self.email_address = email_address


    def getName(self):
        """
        getName - return the person's name
        
        Args:
            None
            
        Returns:
            name: The name of the person
        """
        return self.name
    
    
    def getPhoneNumber(self):
        """
        getPhoneNumber - return the person's name
        
        Args:
            None
            
        Returns:
            phone_number: The phone number of the person
        """
        return self.phone_number
    
    
    def getEmailAddress(self):
        """
        getName - return the person's name
        
        getEmailAddress:
            None
            
        Returns:
            email_address: The email address of the person
        """
        return self.email_address
