
class Accumulator():
    def __init__(self, inputs):
        self.inputs = inputs
        self.position = 0
        self.accumulator = 0
        self.visited = set()


    def nop(self, steps):
        self.position += 1

    def acc(self, steps):
        self.accumulator += steps
        self.position += 1

    def jmp(self, steps):
        self.position += steps

    def run(self):
        while True:
            if self.position in self.visited:
                return False
            elif self.position == len(self.inputs):
                return self.accumulator
            else:
                self.visited.add(self.position)
                instruction, steps = self.inputs[self.position].strip().split(" ")
                eval("self."+instruction+"({})".format(int(steps)))

def changeinput(inp,count):
    changed = False
    i = 0
    while not changed and i<len(inp):
        if inp[i].split(" ")[0] == "acc":
            i += 1
        elif count == 0:
            constr = inp[i].split(" ")
            if constr[0] == "nop":
                inp[i] = "jmp " + constr[1]
            else:
                inp[i] = "nop " + constr[1]
            return inp
        else:
            i += 1
            count -= 1
    return False

def main(inp):
    count = 0
    while True:
        inp_changed = inp.copy()
        changeinput(inp_changed, count)
        accumulator = Accumulator(inp_changed)
        if accumulator.run():
            return accumulator.accumulator
        else:
            count += 1


if __name__ == "__main__":
    f = open("inp8_1.txt", "r")
    inp = f.readlines()
    print(main(inp))