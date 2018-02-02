# library file for encryption and decryption project
import string


def removeDuplicates(text):   #remove duplicate characters in a string
    seen = set()
    unique = []
    for char in text:
        if char not in seen:
            seen.add(char)
            unique.append(char)

    return "".join(unique)     #string of unique characters


def removeInvalidChars(text):    #remove specific characters chosen with translate method
    invalid_chars = ' \n,./<>?;:\'"[]{}\|-=_+!@#$%^&*()1234567890'
    return text.translate(None, invalid_chars)  #first arg is a translation table for switching characters, "None" in this case
                                                  #second arg is a string type of chars translate will eliminate


def chunkText(text):   #chunk string of text into blocks of 2 with a space in between each chunk
    chunked = ""
    for c in range(0, len(text), 2):
        chunked = chunked + text[c:c+2] + " "

    return chunked


def replaceCharacters(text, in_table, out_table):    #replace chars from 'in_table' with chars from 'out_table'
    table = string.maketrans(in_table, out_table)
    return text.translate(table)


def findLetter(dictionary, row, column):     #find a key in a dictionary where the associated value is a tuple of numbers
    for k, v in dictionary.iteritems():    #iterate over key-value pairs to find key with specific value we searched for
        if v == (row, column):              #'k' stands for key of dictionary, 'v' is a value associated with a key in a dictionary
            return k
