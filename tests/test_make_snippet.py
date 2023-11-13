from lib.make_snippet import *
def test_return_empty_string_if_empty():
    assert make_snippet("") == ""
    
def test_given_four_words_returns_same():
    assert make_snippet("one two three four") == "one two three four"
    
def test_given_five_words_returns_same():
    assert make_snippet("one two three four five") == "one two three four five"
    
def test_given_six_words_returns_five_then_ellipsis():
    assert make_snippet("one two three four five six") == "one two three four five..."
    
def test_return_word_count():
    assert count_words("one two three four five six") == 6
    
def test_return_word_count_with_no_string():
    assert count_words("") == 0