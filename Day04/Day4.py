import hashlib

key = "bgvyzdsv"

for want in ["00000", "000000"]:
    i = 0
    found = False
    while not found:
        val = key + str(i)
        hashed = hashlib.md5(val.encode('ascii')).hexdigest()
        if hashed.startswith(want):
            found = True
            continue
        i += 1

    print("Answer for {} zeros is:".format(len(want)), i)