# Implementation of the Playfair encryption scheme

import sys  #for command line arguments and std input
import playfair   #playfair methods


if __name__ == "__main__":

    if len(sys.argv) == 2:   #std input, only given key
        key = sys.argv[1]
        input_text = sys.stdin.read()   #enter End-Of-File character to stop reading (Ctrl-D on *nix, Ctrl-Z on Windows)
        #print "key: %s \ninput text: %s" % (key, input_text)

    elif len(sys.argv) == 3:  #given a key and text file to read
        key = sys.argv[1]
        #textfile = open(sys.argv[2], 'r')
        #input_text = textfile.read()
        #textfile.close()
        with open(sys.argv[2], 'r') as textfile:   #open and read contents of file, file closes automatically at the end
            input_text = textfile.read()

        #print "key: %s \ninput text: %s" % (key, input_text)

    else:   #too few or too many arguments given
        print "Error. Incorrect arguments given."
        sys.exit(1)

    ciphertext = playfair.encrypt(key, input_text)  #result of encryption method
    sys.stdout.write(ciphertext)
