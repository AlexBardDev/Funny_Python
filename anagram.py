"""
This script takes 2 parameters(=words) and tells if they are anagrams or not.
"""

def anagram(chaine1, chaine2):
    """Function that checks if 2 words are anagrams or not"""

    list1 = list(chaine1)
    list2 = list(chaine2)

    i = 0
    is_anagram = False

    while len(list1) == len(list2):

        if list1[i] in list2:
            i += 1
        else:
            break

        if i == len(list1)-1:
            is_anagram = True
            break

    return is_anagram

while True:
    word1 = input("First word : ")
    word2 = input("Second word : ")

    if anagram(word1.lower(), word2.lower()) == True:
        message = """{} and {} are anagrams""".format(word1, word2)
    else:
        message = """{} and {} are not anagrams""".format(word1, word2)

    print(message)

    choice = input("Do you want to quit ? (y/n) ")

    if choice == "y":
        break
