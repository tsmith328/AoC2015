print("Difference in memory vs literal:", sum(len(s[:-1]) - len(eval(s)) for s in open('input8.txt')))
print("Adding escapes:", sum(2 + s.count('"') + s.count('\\') for s in open('input8.txt')))