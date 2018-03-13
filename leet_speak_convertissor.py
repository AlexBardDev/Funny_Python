"""
This script is a leet speak convertissor.
It takes a string and it returns the string written in leet speak.
"""

def permutation(letter):
    """Function that transforms letter in leet speak equivalent"""

    if letter == "a":
        new_letter = "4"
    elif letter == "b":
        new_letter = "8"
    elif letter == "e":
        new_letter = "3"
    elif letter == "l":
        new_letter = "1"
    elif letter == "o":
        new_letter = "0"
    elif letter == "g":
        new_letter = "6"
    elif letter == "s":
        new_letter = "5"
    elif letter == "t":
        new_letter = "7"
    else:
        new_letter = "2"

    return new_letter

def convertissor(text):
    """Function that converts a string in leet speak"""

    message_lt = ""
    for letter in text:
        if letter.lower() in ["a", "b", "e", "g", "l", "o", "s", "t", "z"]:
            new_letter = permutation(letter.lower())
            message_lt += new_letter
        else:
            message_lt += letter

    return message_lt

message = input("""Enter text to convert : """)

leet_speak_message = convertissor(message)

print(leet_speak_message)
