#Vigenere cipher methods

def formatKey(text):
    text = filter(lambda c: c.isalpha(), text)
    text = text.lower()
    return text

def encrypt(key, plaintext):
    
    key = formatKey(key)
    
    ciphertext = ""   #empty string to hold ciphertext
    key_count = 0    #counter to keep track of which letter of key we are encrypting with
    for i in range(len(plaintext)):
        
        if not plaintext[i].isalpha():   #don't encrypt space and punctuation characters, keep them in same place
            ciphertext = ciphertext + plaintext[i]
            
        
        elif plaintext[i].isupper():     #keeping encrypted letter same case
            letter = ord(plaintext[i]) - ord('A')   #convert letter to mod 26 equivalent
            offset = ord(key[key_count % len(key)]) - ord('a')   #convert key letter to mod 26 equivalent
                                                #(key is all lower case, hence different value subtracted)
                                                #repeat the key when necessary via 'count % len(key)'
                                                
            new_letter = ((letter + offset) % 26) + ord('A')  #new letter in mod 26, then convert back to ASCII value
            ciphertext = ciphertext + chr(new_letter)   #get the character representing the ASCII value
            key_count += 1
            
        elif plaintext[i].islower():    #keeping encrypted letter same case
            letter = ord(plaintext[i]) - ord('a')  #convert letter to mod 26 equivalent
            offset = ord(key[key_count % len(key)]) - ord('a')   #convert key letter to mod 26 equivalent
                                                            #repeat key when necessary via 'count % len(key)'
                                                            
            new_letter = ((letter + offset) % 26) + ord('a')  #new letter in mod 26, then convert back to ASCII value
            ciphertext = ciphertext + chr(new_letter)   #get the character representing the ASCII value
            key_count += 1
            
    
    return ciphertext
    
    
def decrypt(key, ciphertext):
    
    key = formatKey(key)
    
    plaintext = ""   #empty string to hold plaintext
    key_count = 0    #counter to keep track of which letter of key we are decrypting with
    for i in range(len(ciphertext)):
        
        if not ciphertext[i].isalpha():   #don't encrypt space and punctuation characters, keep them in same place
            plaintext = plaintext + ciphertext[i]
            
        
        elif ciphertext[i].isupper():     #keeping encrypted letter same case
            letter = ord(ciphertext[i]) - ord('A')   #convert letter to mod 26 equivalent
            offset = ord(key[key_count % len(key)]) - ord('a')   #convert key letter to mod 26 equivalent
                                                #(key is all lower case, hence different value subtracted)
                                                #repeat key when necessary with 'count % len(key)'
                                                
            new_letter = ((letter - offset) % 26) + ord('A')  #new letter in mod 26, then convert back to ASCII value
            plaintext = plaintext + chr(new_letter)   #get the character representing the ASCII value
            key_count += 1
            
        elif ciphertext[i].islower():    #keeping encrypted letter same case
            letter = ord(ciphertext[i]) - ord('a')  #convert letter to mod 26 equivalent
            offset = ord(key[key_count % len(key)]) - ord('a')   #convert key letter to mod 26 equivalent
                                                        #repeat key when necessary with 'count % len(key)'
                                                        
            new_letter = ((letter - offset) % 26) + ord('a')  #new letter in mod 26, then convert back to ASCII value
            plaintext = plaintext + chr(new_letter)   #get the character representing the ASCII value
            key_count += 1
            
    
    return plaintext