Describe the Problem:
    As a user
    So that i can keep track of my tasks
    I want to check if a text includes the string #TODO

---------
Design the Function Signature:
    def checks_for_TODO(text)
    parameters: text (string)
    returns True or False depending on if string contains #TODO

    if no text is given, return "No text was provided"

---------
Create Examples of Tests:
    test_checks_for_TODO_in_text_with_TODO()
    => True

    test_checks_for_TODO_in_text_without_TODO()
    => False

    test_checks_for_TODO_in_text_without_hastag()
    => False

    test_checks_for_TODO_in_text_lowercase_TODO()
    => False

    test_checks_for_TODO_in_empty_string()
    => False