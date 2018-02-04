#Vigenere encryption scheme

import sys
import vigenere


if __name__ == "__main__":
    
    if len(sys.argv) == 2:  #standard input
        
        key = sys.argv[1]
        input_text = sys.stdin.read()
        
    elif len(sys.argv) == 3:  #read from text file
        
        key = sys.argv[1]
        
        with open(sys.argv[2], 'r') as textfile:
            input_text = textfile.read()
            
    else:
        print "Error: Incorrect arguments given"
        sys.exit(1)
        
    
    #print "key: %s \ninput text: %s" % (key, input_text)
    ciphertext = vigenere.encrypt(key, input_text)
    sys.stdout.write(ciphertext)
    