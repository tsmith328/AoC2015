start = "1113122113"

def see_n_say(string):
    curr = string[0]
    count = 1
    output = ""
    for i in range(1, len(string)):
        if string[i] == curr:
            count += 1
        else:
            #Finished with this one
            output += str(count) + str(curr)
            curr = string[i]
            count = 1
    output += str(count) + str(curr)
    return output

answer = start
for i in range(40):
    answer = see_n_say(answer)

print("After 40 iterations, the string is length:", len(answer))

answer = start
for i in range(50):
    answer = see_n_say(answer)

print("After 50 iterations, the string is length:", len(answer))