#monoalphabetic decryption scheme

import sys
import monoalphabetic

if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        
        key = sys.argv[1]
        input_text = sys.stdin.read()   #standard input
        
        #print "key: %s \ninput text: %s" % (key, input_text)
        
    elif len(sys.argv) == 3:
        
        key = sys.argv[1]
        
        with open(sys.argv[2], 'r') as textfile:  #read in text file
            input_text = textfile.read()
            
        #print "key: %s \ninput text: %s" % (key, input_text)
        
    else:
        print "Error: Incorrect arguments given."
        sys.exit(1)
        
        
    plaintext = monoalphabetic.decrypt(key, input_text)
    sys.stdout.write(plaintext)