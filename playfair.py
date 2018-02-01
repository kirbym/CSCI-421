#playfair functions

import string
import helper

def formatKey(key):
    key = helper.removeInvalidChars(key)

    in_table = "j"
    out_table = "i"
    trans_table = string.maketrans(in_table, out_table)
    key = key.translate(trans_table)

    key = helper.removeDuplicates(key)

    key = key.lower()

    return key


def formatInput(text):
    text = helper.removeInvalidChars(text)

    in_table = "j"
    out_table = "i"
    trans_table = string.maketrans(in_table, out_table)
    text = text.translate(trans_table)

    if len(text) % 2 == 1:
        text = text + "x"

    for char in range(0, len(text), 2):
        if text[char] == text[char+1]:
            if text[char] == "x":
                text = text[:char+1] + "z" + text[char+2:]
            else:
                text = text[:char+1] + "x" + text[char+2:]

    text = text.lower()

    return text


def createMatrix(key):
    listofchars = []
    seen = set()

    for char in key:
        listofchars.append(char)
        seen.add(char)

    for char in string.ascii_lowercase:
        if char is not "j":
            if char not in seen:
                listofchars.append(char)
                seen.add(char)

    matrix = {}
    count = 0
    for i in xrange(0,5):
        for j in xrange(0,5):
            matrix[listofchars[count]] = (i, j)
            count += 1

    #print "matrix:", matrix
    #print "length: %d" % len(matrix)
    return matrix


def shiftRight(matrix, letter1, letter2):
    row1 = matrix[letter1][0]
    col1 = matrix[letter1][1]
    row2 = matrix[letter2][0]
    col2 = matrix[letter2][1]

    for letter, position in matrix.iteritems():
        if position == ( row1, (col1 + 1) % 5 ):
            let1 = letter

    for letter, position in matrix.iteritems():
        if position == ( row2, (col2 + 1) % 5 ):
            let2 = letter

    return let1 + let2


def shiftLeft(matrix, letter1, letter2):
    row1 = matrix[letter1][0]
    col1 = matrix[letter1][1]
    row2 = matrix[letter2][0]
    col2 = matrix[letter2][1]

    for letter, position in matrix.iteritems():
        if position == ( row1, (col1 - 1) % 5 ):
            let1 = letter

    for letter, position in matrix.iteritems():
        if position == ( row2, (col2 - 1) % 5 ):
            let2 = letter

    return let1 + let2


def shiftDown(matrix, letter1, letter2):
    row1 = matrix[letter1][0]
    col1 = matrix[letter2][1]
    row2 = matrix[letter2][0]
    col2 = matrix[letter2][1]

    for letter, position in matrix.iteritems():
        if position == ( (row1 + 1) % 5, col1 ):
            let1 = letter

    for letter, position in matrix.iteritems():
        if position == ( (row2 + 1) % 5, col2 ):
            let2 = letter

    return let1 + let2

def shiftUp(matrix, letter1, letter2):
    row1 = matrix[letter1][0]
    col1 = matrix[letter2][1]
    row2 = matrix[letter2][0]
    col2 = matrix[letter2][1]

    for letter, position in matrix.iteritems():
        if position == ( (row1 - 1) % 5, col1 ):
            let1 = letter

    for letter, position in matrix.iteritems():
        if position == ( (row2 - 1) % 5, col2 ):
            let2 = letter

    return let1 + let2


def swap(matrix, letter1, letter2):
    row1 = matrix[letter1][0]
    col1 = matrix[letter1][1]
    row2 = matrix[letter2][0]
    col2 = matrix[letter2][1]

    for letter, position in matrix.iteritems():
        if position == (row1, col2):
            let1 = letter

    for letter, position in matrix.iteritems():
        if position == (row2, col1):
            let2 = letter

    return let1 + let2


def encrypt(key, plaintext):
    key = formatKey(key)
    plaintext = formatInput(plaintext)
    matrix = createMatrix(key)
    ciphertext = ""

    row = 0
    col = 1

    for char in range(0, len(plaintext), 2):
        first = plaintext[char]
        second = plaintext[char+1]

        if matrix[first][row] == matrix[second][row]:  #same row
            tmp = shiftRight(matrix, first, second)

        elif matrix[first][col] == matrix[second][col]:  #same column
            tmp = shiftDown(matrix, first, second)

        else:   #swap letters if they make rectangle, keep letter in respective row and swap columns
            tmp = swap(matrix, first, second)

        ciphertext = ciphertext + tmp

    return ciphertext


def decrypt(key, ciphertext):
    key = formatKey(key)
    ciphertext = formatInput(ciphertext)
    matrix = createMatrix(key)
    plaintext = ""

    row = 0
    col = 1

    for char in range(0, len(ciphertext), 2):
        first = ciphertext[char]
        second = ciphertext[char+1]

        if matrix[first][row] == matrix[second][row]:  #same row
            tmp = shiftLeft(matrix, first, second)

        elif matrix[first][col] == matrix[second][col]:   #same column
            tmp = shiftUp(matrix, first, second)

        else:       #swap letters if they make rectangle, keep letter in respective row and swap columns
            tmp = swap(matrix, first, second)

        plaintext = plaintext + tmp

    return plaintext
