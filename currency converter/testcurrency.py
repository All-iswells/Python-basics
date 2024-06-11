"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: Eric Robertson
Date: May 11th, 2024
"""
import introcs
import currency

def test_before_space():
    """Test procedure for before_space"""

    # Test case 1: Single space in the middle
    result = currency.before_space('Hello World')
    introcs.assert_equals('Hello', result)
    
    # Test case 2: Multiple spaces
    result = currency.before_space('The quick brown fox')
    introcs.assert_equals('The', result)
    
    # Test case 3: Space at the beginning
    result = currency.before_space(' Hello')
    introcs.assert_equals('', result)
    
    # Test case 4: Space at the end
    result = currency.before_space('Hello ')
    introcs.assert_equals('Hello', result)
    
    # Test case 5: Multiple spaces, space in the middle
    result = currency.before_space('Hello  World')
    introcs.assert_equals('Hello', result)
    
    # Test case 6: String with special characters
    result = currency.before_space('Hello, World!')
    introcs.assert_equals('Hello,', result)
    
    # Test case 7: String with numerical characters
    result = currency.before_space('123 456')
    introcs.assert_equals('123', result)
    print("Testing before_space")
    

def test_after_space():
    """Test procedure for after_space"""

    # Test case 1: Single space in the middle
    result = currency.after_space('Hello World')
    introcs.assert_equals('World',result)

    # Test case 2: Str with space at the start
    result = currency.after_space(' Hello World')
    introcs.assert_equals('Hello World', result)

    # Test case 3: Multiple spaces
    result = currency.after_space('Hello   World')
    introcs.assert_equals("  World", result)

    # Test case 4: Str with spaces at the start and end
    result = currency.after_space('Hello ')
    introcs.assert_equals('', result)

    print("Testing after_space")


def test_first_inside_quotes():
    """Test procedure for first_inside_quotes"""

    # Test case 1: Basic test
    result = currency.first_inside_quotes('AB "CD" EF')
    introcs.assert_equals('CD', result)

    # Test case 2: Multiple substring with quotes
    result = currency.first_inside_quotes('AB "CD" E "FG"')
    introcs.assert_equals('CD', result)

    # Test case 3: Nothing inside double quotes
    result = currency.first_inside_quotes(' AB "" EF')
    introcs.assert_equals('', result)
    
    # Test case 4: Only double quotes
    result = currency.first_inside_quotes('"ABC"')
    introcs.assert_equals('ABC', result)

    print("Testing first_inside_quotes")


def test_get_src():
    """ Test procedure for get_src"""

    # Test case 1: Basic
    result = currency.get_src('{"success": true, "src": "2 United States Dollars",' +\
    '"dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars', result)
    
    # Test case 2: Empty value
    result = currency.get_src('{"success":false,"src":"","dst":"","error":' + \
    '"Source currency code is invalid."}')
    introcs.assert_equals('', result)

    # Test case 3: Different format
    result = currency.get_src('{"success":true, "src":"2 United States Dollars",' +\
    '"dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals('2 United States Dollars', result)

    # Test case 4: Missing Source field
    result = currency.get_src('{"success":false,"src": "","dst":"","error":'+ \
    '"Source currency code is invalid."}')
    introcs.assert_equals('', result)

    print("Testing get_src")


def test_get_dst():
    """Test procedure for get_dst"""

    # Test case 1: Basic valid input
    result = currency.get_dst('{"success": true, "src": "2 United States Dollars", '+ \
    '"dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros', result)

    # Test case 2: Empty dst
    result = currency.get_dst('{"success":false,"src":"","dst":"","error":'+ \
    '"Source currency code is invalid."}')
    introcs.assert_equals('', result)

    # Test case 3: Additional spaces after colon
    result = currency.get_dst('{"success":true, "src":"2 United States Dollars", '+ \
    '"dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals('1.772814 Euros', result)

    # Test case 4: Empty dst and spaces after colon
    result = currency.get_dst('{"success":false,"src":"","dst": "","error":'+\
    '"Source currency code is invalid."}')
    introcs.assert_equals('', result)

    print("Testing get_dst")


def test_has_error():
    """Test procedure for has_error"""

    #Test case 1: Basic error
    result = currency.has_error('{"success":false,"src":"","dst":"","error":"Source '+\
    'currency code is invalid."}')
    introcs.assert_true(True,result)

    #Test case 2: No error
    result = currency.has_error('{"success": true, "src": "2 United States Dollars", '+\
    '"dst": "1.772814 Euros", "error": ""}')
    introcs.assert_false(False, result)

    #Test case 3: Spaces after colon
    result = currency.has_error('{"success":true, "src":"2 United States Dollars", '+\
    '"dst":"1.772814 Euros", "error":""}')
    introcs.assert_false(False, result)

    #Test case 4: No error and space after.
    result = currency.has_error('{"success":false,"src":"","dst":"","error": "Invalid '+\
    'currency code : USD"}')
    introcs.assert_true(True, result)


    print("Testing has_error")


def test_service_response():
    """Test procedure for service_response"""

    #Test case 1: Valid currency and Non-negative amount
    result = currency.service_response('USD', 'EUR', 2.5)
    introcs.assert_equals('{"success": true, "src": "2.5 United States Dollars", '+\
    '"dst": "2.2160175 Euros", "error": ""}', result)

    #test case 2: Valid currencies, negative amt
    result = currency.service_response('GBP', 'JPY', -5.75)
    introcs.assert_equals('{"success": true, "src": "-5.75 British Pounds Sterling"'+\
    ', "dst": "-780.105164567147 Japanese Yen", "error": ""}', result)

    #Test case 3: Invalid currency
    result = currency.service_response("ABC", "USD", 1)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error": '+\
    '"The rate for currency ABC is not present."}', result)

    #Test case 4: Invalid currency, negative amt
    result = currency.service_response("USD","ABC", -1)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error": "The '+\
    'rate for currency ABC is not present."}', result)

    print("Testing service_response")


def test_iscurrency():
    """Test procedure for iscurrency"""

    #Test case 1: Valid input
    result = currency.iscurrency('USD')
    introcs.assert_equals(True, result)

    #Test case 2: Invalid input
    result = currency.iscurrency('ABC')
    introcs.assert_equals(False, result)

    print("Testing iscurrency")


def test_exchange():
    """Test procedure for exchange"""
    print("Testing exchange")

    #Test case 1: Valid input
    result = currency.exchange('USD','EUR', 100)
    introcs.assert_floats_equal(88.6407, result)

    #Test case 2: Negative
    result = currency.exchange('USD','EUR', -100)
    introcs.assert_floats_equal(-88.6407, result)


# Call test procedures
test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()


print("All tests completed successfully.")