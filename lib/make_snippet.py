def make_snippet(sentence):
    words = sentence.split(" ")
    if len(words) > 5:
        first_five = words[:5]
        snippet = " ".join(first_five) + "..."
        return snippet
    else:
        return sentence
    
def count_words(sentence):
    if sentence == "":
        return 0
    words = sentence.split(" ")
    return len(words)