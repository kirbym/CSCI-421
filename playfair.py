#playfair functions
import library


def formatKey(key):  #format key to remove bad chars, replacing "j" with "i", removing duplicates, and changing to lowercase
    key = library.removeInvalidChars(key)
    key = library.replaceCharacters(key, "j", "i")
    key = library.removeDuplicates(key)
    key = key.lower()

    return key


def formatInput(text):   #format input to remove bad chars, replacing "j" with "i", and changing to lowercase
    text = library.removeInvalidChars(text)
    text = library.replaceCharacters(text, "j", "i")

    if len(text) % 2 == 1:        #add an "x" if the string has odd number of chars
        text = text + "x"

    #if there are double letters, replace second with an "x" (XX gets replaced with XZ)
    for char in range(0, len(text), 2):
        if text[char] == text[char+1]:
            if text[char] == "x":
                text = text[:char+1] + "z" + text[char+2:]
            else:
                text = text[:char+1] + "x" + text[char+2:]

    text = text.lower()

    return text


def createMatrix(key):   #create the 5x5 matrix of letters needed for playfair scheme
    listofchars = []
    seen = set()

    for char in key:    #create list of chars beginning with key and doesn't include repeated characters
        listofchars.append(char)
        seen.add(char)

    for char in library.string.ascii_lowercase:   #fill out rest of list with all other chars except "j"
        if char is not "j":
            if char not in seen:
                listofchars.append(char)
                seen.add(char)

    #create symbolic matrix of letters using a dictionary (key-value pairs)
    #key is the letter, value is a tuple indicating the position of the letter in the matrix
    matrix = {}    #empty dictionary
    count = 0
    for i in xrange(0,5):
        for j in xrange(0,5):
            matrix[listofchars[count]] = (i, j)   #filling out dictionary
            count += 1

    #print "matrix:", matrix
    #print "length: %d" % len(matrix)
    return matrix


def shiftRight(matrix, letter1, letter2):   #shift letters right when in the same row
    row1 = matrix[letter1][0]
    col1 = matrix[letter1][1]
    row2 = matrix[letter2][0]
    col2 = matrix[letter2][1]
    let1 = library.findLetter( matrix, row1, (col1 + 1) % 5 )
    let2 = library.findLetter( matrix, row2, (col2 + 1) % 5 )

    return let1 + let2


def shiftLeft(matrix, letter1, letter2):   #shift letters left when in the same row
    row1 = matrix[letter1][0]
    col1 = matrix[letter1][1]
    row2 = matrix[letter2][0]
    col2 = matrix[letter2][1]
    let1 = library.findLetter( matrix, row1, (col1 - 1) % 5 )
    let2 = library.findLetter( matrix, row2, (col2 - 1) % 5 )

    return let1 + let2


def shiftDown(matrix, letter1, letter2):   #shift letters down when in the same column
    row1 = matrix[letter1][0]
    col1 = matrix[letter2][1]
    row2 = matrix[letter2][0]
    col2 = matrix[letter2][1]
    let1 = library.findLetter( matrix, (row1 + 1) % 5, col1 )
    let2 = library.findLetter( matrix, (row2 + 1) % 5, col2 )

    return let1 + let2

def shiftUp(matrix, letter1, letter2):   #shift letters up when in the same column
    row1 = matrix[letter1][0]
    col1 = matrix[letter2][1]
    row2 = matrix[letter2][0]
    col2 = matrix[letter2][1]
    let1 = library.findLetter( matrix, (row1 - 1) % 5, col1 )
    let2 = library.findLetter( matrix, (row2 - 1) % 5, col2 )

    return let1 + let2


#when letters form a rectangle in matrix, replace each letter with
#the new letter in the same row with the opposite letter's column positon
def swap(matrix, letter1, letter2):
    row1 = matrix[letter1][0]
    col1 = matrix[letter1][1]
    row2 = matrix[letter2][0]
    col2 = matrix[letter2][1]
    let1 = library.findLetter(matrix, row1, col2)
    let2 = library.findLetter(matrix, row2, col1)

    return let1 + let2


def encrypt(key, plaintext):   #perform the encryption technique of playfair scheme
    key = formatKey(key)
    plaintext = formatInput(plaintext)
    matrix = createMatrix(key)
    ciphertext = ""

    row = 0
    col = 1

    for char in range(0, len(plaintext), 2):
        first = plaintext[char]
        second = plaintext[char+1]

        if matrix[first][row] == matrix[second][row]:  #letters in same row, shift right
            tmp = shiftRight(matrix, first, second)

        elif matrix[first][col] == matrix[second][col]:  #letters in same column, shift down
            tmp = shiftDown(matrix, first, second)

        else:   #swap letters if they make rectangle, keep letter in respective row and swap columns
            tmp = swap(matrix, first, second)

        ciphertext = ciphertext + tmp

    ciphertext = library.chunkText(ciphertext)   #chunk text into 2's

    return ciphertext


def decrypt(key, ciphertext):   #perform the decryption technique of the playfair scheme
    key = formatKey(key)
    ciphertext = formatInput(ciphertext)
    matrix = createMatrix(key)
    plaintext = ""

    row = 0
    col = 1

    for char in range(0, len(ciphertext), 2):
        first = ciphertext[char]
        second = ciphertext[char+1]

        if matrix[first][row] == matrix[second][row]:  #letters in same row, shift left
            tmp = shiftLeft(matrix, first, second)

        elif matrix[first][col] == matrix[second][col]:   #letters in same column, shift up
            tmp = shiftUp(matrix, first, second)

        else:       #swap letters if they make rectangle, keep letter in respective row and swap columns
            tmp = swap(matrix, first, second)

        plaintext = plaintext + tmp

    plaintext = library.chunkText(plaintext)   #chunk text into 2's

    return plaintext
