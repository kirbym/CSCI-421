# "library" file for encryption and decryption project

def removeDuplicates(string):
    seen = set()
    unique = []
    for char in string:
        if char not in seen:
            seen.add(char)
            unique.append(char)

    return "".join(unique)

def removeInvalidChars(string):
    invalid_chars = ' \n,./<>?;:\'"[]{}\|-=_+!@#$%^&*()1234567890'
    return string.translate(None, invalid_chars)
