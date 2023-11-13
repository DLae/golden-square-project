Describe the Problem 
    As a user
    So that i can improve my grammar
    I want to verify that a text starts with a capital and ends with a suitable punctuation mark

---------
Design the Function Signature:
    def check_sentence_grammar(text):
    parameters: text (string)
    returns True or False

---------
Create Examples of Tests:
    check_sentence_grammar("Hello, this test shoud pass.")
    => True

    check_sentence_grammar("Hello, this sentence doesn't have a full-stop")
    => False

    check_sentence_grammar("hello, this sentence doesn't have a capital letter.")
    => False

    check_sentence_grammar("Hello, how are you?")
    => True

    check_sentence_grammar("Hello, this sentence ends with a colon")
    => False

    check_sentence_grammar("")
    => "Can't grammar check an empty string."
    