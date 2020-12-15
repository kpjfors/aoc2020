def main(inp):
    mask = ""
    address = ""
    value = ""
    memory = {}
    for i in inp:
        lhs, rhs = i.split(" = ")
        if lhs == "mask":
            mask = rhs.strip()
        else:
            address, value = lhs.split("[")[1][:-1], rhs.strip()
            bit = format(int(value), "b").zfill(36)
            out = ""
            for i in range(len(bit)):
                if mask[i] != "X":
                    out += mask[i]
                else:
                    out += bit[i]
            memory[address] = int(out, 2)

    return sum(memory.values())


if __name__ == "__main__":
    f = open("inp14_1.txt", "r")
    inp = f.readlines()
    print(main(inp))
