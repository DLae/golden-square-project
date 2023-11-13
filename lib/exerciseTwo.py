def check_valid_grammar(text):
    if text == "":
        return "Can't grammar check an empty string."
    else:
        if text[0].isupper() == True and text[-1] in ".?!":
            return True
        else:
            return False