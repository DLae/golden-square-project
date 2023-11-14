import pytest
from lib.diary_entry_class import *

def test_when_empty_title_and_contents():
    with pytest.raises(Exception) as e:
        DiaryEntry("", "")
    assert str(e.value) == "Entry must contain a title or contents."

def test_formats_with_title_contents():
    diary_entry = DiaryEntry("Title", "Loads of content")
    assert diary_entry.format() == "Title: Loads of content"
    
def test_formats_with_title_contents_returning_word_count():
    diary_entry = DiaryEntry("TItle", "Loads of content")
    assert diary_entry.count_words() == 3
    
def test_reading_time_two_words_two_wpm():
    diary_entry = DiaryEntry("Title", "Two words")
    assert diary_entry.reading_time(2) == 1
    
def test_reading_time_wpm_zero():
    diary_entry = DiaryEntry("Title", "Loads of content")
    with pytest.raises(Exception) as e:
        diary_entry.reading_time(0)
    assert str(e.value) == "Can't calculate with wpm of 0"
    
def test_reading_chunk_with_two_wpm_one_minute():
    diary_entry = DiaryEntry("Title", "one two three four five six")
    assert diary_entry.reading_chunk(2,1) == "one two"