import re
import json

ignore_red = False

def main():
    with open('input12.txt') as f:
        string = f.readline()

    string = json.loads(string)

    print("Sum of numbers in JSON:", addNums(string))
    global ignore_red
    ignore_red = True
    print("Sum of numbers in JSON ignoring red:", addNums(string))

def addNums(string):
    if type(string) == list:
        return sum([addNums(x) for x in string])
    if type(string) == dict:
        vals = [x[1] for x in string.items()]
        if 'red' in vals and ignore_red:
            return 0
        return sum([addNums(x) + addNums(y) for x,y in string.items()])
    if type(string) == str:
        return 0
    return string

if __name__ == '__main__':
    main()