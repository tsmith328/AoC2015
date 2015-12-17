wires = {}

class Wire(object):
    #Value is a list: [gate, arg1, [arg2]] or [assignment_value]
    def __init__(self, label, value):
        self.label = label
        self.value = None
        if len(value) == 1:
            self.gate = 'assignment'
            self.arg = value[0]
        else:
            self.gate = value[0].lower()
            if self.gate == 'not':
                self.arg = value[1]
            else:
                self.arg1 = value[1]
                self.arg2 = value[2]

    def evaluate(self):
        if self.value:
            return self.value
        if self.gate == 'assignment':
            try:
                self.value = int(self.arg)
            except ValueError:
                self.value = wires[self.arg].evaluate()
        elif self.gate == 'not':
            try:
                self.value = ~int(self.arg)
            except ValueError:
                self.value = ~(wires[self.arg].evaluate())
        else:
            try:
                a = int(self.arg1)
            except ValueError:
                a = wires[self.arg1].evaluate()
            try:
                b = int(self.arg2)
            except ValueError:
                b = wires[self.arg2].evaluate()

            if self.gate == 'and':
                self.value = a & b
            elif self.gate == 'or':
                self.value = a | b
            elif self.gate == 'lshift':
                self.value = a << b
            elif self.gate == 'rshift':
                self.value = a >> b

        return self.value

def main():
    with open('input7.txt') as f:
        for line in f:
            line = line.split() #Split on space
            label = line[-1]
            if len(line) == 5: #2-arg operation
                value = [line[1], line[0], line[2]]
            if len(line) == 4: #1-arg operation (NOT)
                value = [line[0], line[1]]
            if len(line) == 3: #Assignment
                value = [line[0]]
            wire = Wire(label, value)
            wires[label] = wire

    print("Value of wire a:", wires['a'].evaluate())

    wires['b'] = Wire('b', [str(wires['a'].evaluate())])

    for wire in wires:
        wires[wire].value = None

    print("Value of wire a after overriding wire b:", wires['a'].evaluate())

if __name__ == "__main__":
    main()