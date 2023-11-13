from lib.exerciseOne import *

def test_with_twoHundred_words():
    text = " ".join(["word" for i in range(0,200)])
    assert estimated_reading_time(text) == 1
    
def test_with_threeHundred_words():
    text = " ".join(["word" for i in range(0,300)])
    assert estimated_reading_time(text) == 1.5
    
def test_with_fourHundred_words():
    text = " ".join(["word" for i in range(0,400)])
    assert estimated_reading_time(text) == 2
    
def test_with_empty_string():
    assert estimated_reading_time("") == "Can't estimate reading time for empty string."
    
    
