from lib.exerciseTwo import *

def test_with_valid_grammar():
    assert check_valid_grammar("Hello, this test should pass.") == True
    
def test_without_capital_letter():
    assert check_valid_grammar("hello, this sentence doesn't have a capital letter.") == False
    
def test_with_question_mark():
    assert check_valid_grammar("Hello, how are you?") == True
    
def test_with_ending_colon():
    assert check_valid_grammar("Hello, this sentence ends with a colon:") == False
    
def test_with_empty_string():
    assert check_valid_grammar("") == "Can't grammar check an empty string."