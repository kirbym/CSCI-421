#alternate method for caesar cipher

import sys
import string

def encrypt(key, plaintext):
    plaintext = plaintext.lower()

    invalid_chars = ' \n,./<>?;:\'"[]{}\|-=_+!@#$%^&*()1234567890'
    in_tab = string.ascii_lowercase
    out_tab = string.ascii_lowercase[key:] + string.ascii_lowercase[:key]
    trans_tab = string.maketrans(in_tab, out_tab)
    plaintext = plaintext.translate(trans_tab, invalid_chars)

    return plaintext

if __name__ == "__main__":

    if len(sys.argv) == 2:

        key = int(sys.argv[1]) % 26

        input_text = sys.stdin.read()

    elif len(sys.argv) == 3:

        key = int(sys.argv[1]) % 26

        with open(sys.argv[2], 'r') as textfile:
            input_text = textfile.read()

    else:
        print "Error: Incorrect arguments given"
        sys.exit(1)

    ciphertext = encrypt(key, input_text)
    sys.stdout.write(ciphertext)
