row = 0
col = 0
first = 20151125
factor = 252533
mod = 33554393


def main():
    global row
    global col
    with open("input25.txt") as f:
        words = f.readline().split(" ")
        words = [word.strip(",.\n") for word in words]
        row = int(words[words.index("row") + 1])
        col = int(words[words.index("column") + 1])

    print("Code: %d" % get_value(row, col))

def get_value(r, c):
    count = get_count(r, c)
    curr = first
    for i in range(count - 1):
        curr = (curr * factor) % mod
    return curr

def get_count(r, c):
    return sum(range(r + c - 1)) + c

if __name__ == '__main__':
    main()