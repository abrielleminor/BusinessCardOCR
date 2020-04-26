#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main driver that will take business card block text as input or input from
file redirect and print the name, phone number, and email address from the input.

@author: Abbie Holloway
"""
import sys
import nltk
nltk.download('names', quiet=True)
from business_card_parser import BusinessCardParser

def main(argv):
    """
    main - This is the main routine.  It looks for input via the command line 
    or standard input and calls the routine to get a person's contact info 
    based on the input. It will print the name, phone number and email to the 
    console.

    Args:
        argv[1] (optional if using file redirect) the string of text to parse

    Returns:
        None

    """
    
    contact_info = None

    try:
        # process via command line argument if provided
        contact_info = BusinessCardParser.getContactInfo(sys.argv[1])
        
    except:
        # if stdin was provided, process that way
        if not sys.stdin.isatty():
            document = ''
            for line in sys.stdin:
                document += line
                
            contact_info = BusinessCardParser.getContactInfo(document)
            
        else:
            print("\nNo file provided via command line or redirect. Cannot process data. Usage examples below:\n" + 
                  " python bcp_driver.py 'string to parse'\n " + "OR\n" +
                  " python bcp_driver.py < input.txt")
            return
        
    print("Name:  %s" %contact_info.getName())
    print("Phone: %s" %contact_info.getPhoneNumber())
    print("Email: %s" %contact_info.getEmailAddress())


if __name__ == "__main__":
    main(sys.argv)