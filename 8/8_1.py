
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
                return self.accumulator
            else:
                self.visited.add(self.position)
                instruction, steps = self.inputs[self.position].strip().split(" ")
                eval("self."+instruction+"({})".format(int(steps)))

def main(inp):
    accumulator = Accumulator(inp)
    return accumulator.run()


if __name__ == "__main__":
    f = open("inp8_1.txt", "r")
    inp = f.readlines()
    print(main(inp))