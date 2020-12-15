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
            writer = list(range(1))
            writer[0] = ""
            address, value = lhs.split("[")[1][:-1], rhs.strip()
            bit = format(int(address), "b").zfill(36)
            for i in range(len(bit)):
                if mask[i] != "X":
                    for j in range(len(writer)):
                        writer[j] += str(int(bit[i])|int(mask[i]))
                else:
                    interrimlist = []
                    for j in range(len(writer)):
                        interrimlist.append(writer[j]+"0")
                        interrimlist.append(writer[j] + "1")
                    writer = interrimlist.copy()
            for bit in writer:
                memory[int(bit, 2)] = int(value)

    return sum(memory.values())


if __name__ == "__main__":
    f = open("inp14_1.txt", "r")
    inp = f.readlines()
    print(main(inp))
