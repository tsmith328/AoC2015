nice = 0
nice2 = 0

def vowels(string):
    count = 0
    for c in string:
        if c in ['a','e','i','o','u']:
            count += 1
    return True if count >= 3 else False

def doubles(string):
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False

def exclusions(string):
    bad = ['ab','cd','pq','xy']
    for i in range(len(string)-1):
        if string[i:i+2] in bad:
            return False
    return True

def pairs(string):
    for i in range(len(string)-2):
        seg = string[i:i+2]
        for j in range(i+2, len(string)):
            if seg == string[j:j+2]:
                return True
    return False

def skip(string):
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            return True
    return False

with open("input5.txt") as f:
    for string in f:
        isNice = vowels(string) and doubles(string) and exclusions(string)
        nice += 1 if isNice else 0
        isNice2 = pairs(string) and skip(string)
        nice2 += 1 if isNice2 else 0

print("Number of nice strings:", nice)
print("Number of new nice strings:", nice2)