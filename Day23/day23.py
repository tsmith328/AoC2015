instructions = []
registers = {"a": 0, "b": 0}

def read_in():
    global instructions
    with open("input23.txt") as f:
        for line in f:
            line = line.strip()
            instruction = line.split()
            opcode = instruction[0]
            arg1 = instruction[1].strip(", ")
            if opcode in ("jio", "jie"):
                instructions.append((opcode, arg1, instruction[2]))
            else:
                instructions.append((opcode, arg1))

def main():
    #Begin evaluation
    i = 0
    while i < len(instructions):
        instruction = instructions[i]
        #print("Evaluating %s. Registers are: %d, %d" % (str(instruction), registers["a"], registers["b"]))
        if instruction[0] == "hlf":
            registers[instruction[1]] = int(registers[instruction[1]] / 2)
        if instruction[0] == "tpl":
            registers[instruction[1]] *= 3
        if instruction[0] == "inc":
            registers[instruction[1]] += 1
        if instruction[0] == "jmp":
            i += int(instruction[1]) - 1
        if instruction[0] == "jie":
            if registers[instruction[1]] % 2 == 0:
                i += int(instruction[2]) - 1
        if instruction[0] == "jio":
            if registers[instruction[1]] == 1:
                i += int(instruction[2]) - 1
        i += 1 #Go to next instruction if no jump

    print("Register a is: %d" % registers["a"])
    print("Register b is: %d" % registers["b"])

if __name__ == '__main__':
    read_in()
    print("---- Part 1 ----")
    main()
    registers["a"] = 1
    registers["b"] = 0
    print("---- Part 2 ----")
    main()