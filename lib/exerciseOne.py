def estimated_reading_time(text):
    if text == "":
        return ("Can't estimate reading time for empty string.")
    words = text.split()
    word_count = len(words)
    return word_count / 200