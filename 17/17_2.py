def main(inp):
    ### Initializing
    inp = inp.strip().split("\n")
    active = set()
    for y in range(len(inp)):
        for x in range(len(inp[0])):
            if inp[y][x] == "#":
                active.add((x, y, 0, 0))
    print(active)
    print(len(active))

    for i in range(6):
        active = runonce(active)

    return (len(active))


def runonce(inp):
    neighborsactive = {}
    active = set()
    # Generating neighbors could probably be a lot nicer than nested for loops...
    for i in inp:
        for xo in range(-1, 2):
            for yo in range(-1, 2):
                for zo in range(-1, 2):
                    for wo in range(-1, 2):
                        if (xo, yo, zo, wo) != (0, 0, 0, 0):
                            try:
                                neighborsactive[(i[0] + xo, i[1] + yo, i[2] + zo, i[3] + wo)] += 1
                            except:
                                neighborsactive[(i[0] + xo, i[1] + yo, i[2] + zo, i[3] + wo)] = 1
    print(neighborsactive)
    for k, v in neighborsactive.items():
        if v == 3:
            active.add(k)
        elif v == 2 and k in inp:
            active.add(k)

    return active


if __name__ == "__main__":
    f = open("inp17_1.txt", "r")
    inp = f.read()
    print(main(inp))
