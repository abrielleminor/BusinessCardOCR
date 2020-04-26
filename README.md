# BusinessCardOCR
This project parses the text from a business card into `Name`, `Phone Number`, and `Email Address`. If there is no `Name`, `Phone Number`, or `Email Address` provided, None will be returned for that field. For all fields, it is assumed that there will be only one valid instance. Otherwise, the first valid instance is returned. For `Name`, it is assumed that the person's first name is either a common name or a shortened substring of a common name.

## Getting started
These instructions will get a copy of the project up and running.

### Prerequisites
This project was built with Python 3.8.2. It requires one non-standard library, nltk, which can be installed via pip. A `requirements.txt` file is provided for installation purposes. Given a user has Python 3 and pip installed, run

```
pip install -r requirements.txt
```

### Running the code
The main driver can be run two ways: either by specifying the string of text for parsing as a command line argument or by using file redirection. Examples of both are shown below. An example `input.txt` is provided in the code base as well.
```
python bcp_driver.py "ASYMMETRIK LTD
Mike Smith
Senior Software Engineer
(410)555-1234
msmith@asymmetrik.com"
```
Or
```
python bcp_driver.py < input.txt
```

### Running the tests
There is a test file provided to test the parsing functionality. It includes standard functionality test for parsing different phone number, email, and name formats as well as some edge cases including phone numbers with extensions, multi-part names, names with apostrophes, and company names that contain a person's name and could be confused for a name. To run the test cases:
```
python test_business_card_parser.py
```
