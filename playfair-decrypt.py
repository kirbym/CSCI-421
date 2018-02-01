# Implementation of the Playfair decryption scheme
# Author: Michael Kirby

import sys
import playfair


if __name__ == "__main__":

    if len(sys.argv) == 2:
        key = sys.argv[1]
        input_text = sys.stdin.read()
        #print "key: %s \ninput text: %s" % (key, input_text)

    elif len(sys.argv) == 3:
        key = sys.argv[1]
        #textfile = open(sys.argv[2], 'r')
        #input_text = textfile.read()
        #textfile.close()
        with open(sys.argv[2], 'r') as textfile:
            input_text = textfile.read()

        #print "key: %s \ninput text: %s" % (key, input_text)

    else:
        print "Error. Incorrect arguments given."
        sys.exit(1)

    plaintext = playfair.decrypt(key, input_text)
    print plaintext
