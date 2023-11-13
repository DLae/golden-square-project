Describe the Problem 
    As a user
    So that i can manage my time
    I want to see an estimate reading time assuming that i can read 200 wpm

---------
Design the Function Signature:
    def estimated_reading_time(text)
    parameters: text (string)
    returns reading time (float)

---------
Create Examples of Tests:
    estimated_reading_time(200 words)
    => 1

    estimated_reading_time(300 words)
    => 1.5

    estimated_reading_time(400 words)
    => 2

    estimated_reading_time(empty)
    => "Can't estimate reading time for empty text"