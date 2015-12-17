start = "cqjxjnds"

def good(string):
    return straight(string) and exclude(string) and doubles(string)

def straight(string):
    for i in range(len(string)-2):
        start = ord(string[i])
        second = chr(start + 1)
        third = chr(start + 2)
        if string[i+1] == second and string[i+2] == third:
            return True
    return False

def exclude(string):
    if 'i' in string:
        return False
    if 'o' in string:
        return False
    if 'l' in string:
        return False
    return True

def doubles(string):
    used = None
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            used = string[i]
    if not used:
        return False #No pairs
    for i in range(len(string)-1):
        if string[i] == string[i+1] and string[i] != used:
            return True
    return False

def nextString(string):
    string = list(string)
    for i in range(len(string)-1, -1, -1):
        if string[i] != 'z':
            string[i] = chr(ord(string[i]) + 1)
            break
        else:
            string[i] = 'a'
    return ''.join(c for c in string)

password = nextString(start)

while not good(password):
    password = nextString(password)

print("Next good password is:", password)

password = nextString(password)

while not good(password):
    password = nextString(password)

print("And the next:", password)