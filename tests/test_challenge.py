from lib.challenge import *

def test_checks_for_TODO_in_text_with_TODO():
    assert checks_for_TODO("Wash car #TODO") == True
    
def test_checks_for_TODO_in_text_without_TODO():
    assert checks_for_TODO("Wash car") == False
    
def test_checks_for_TODO_in_text_without_hashtag():
    assert checks_for_TODO("Wash car TODO") == False
    
def test_checks_for_TODO_in_text_lowercase_TODO():
    assert checks_for_TODO("Wash car #todo") == False
    
def test_checks_for_TODO_in_empty_string():
    assert checks_for_TODO("") == False