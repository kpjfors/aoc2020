offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def main(inp):
    occupied = 0
    seats = [list(x)[:-1] for x in inp]
    converged = False
    while not converged:
        seats, changed = iterateseats(seats)
        converged = not changed
        #for i in seats:
        #    print(i)
        #print("\n")

    for i in seats:
        occupied += i.count("#")
        print(i)
    return occupied

def iterateseats(inp):
    changed = False
    curr = inp
    next = [[] for x in inp]
    block = 0
    for x in range(len(curr[0])):
        for y in range(len(curr)):
            block +=1
            neighborsoccupied = 0

            for dx, dy in offsets:
                if 0 <= y + dy < len(inp) and 0 <= x + dx < len(inp[0]):
                    neighborsoccupied += curr[y + dy][x + dx] == '#'

            if curr[y][x] == "L" and neighborsoccupied == 0:
                next[y].append("#")
                changed = True
            elif curr[y][x] == "#" and neighborsoccupied >= 4:
                next[y].append("L")
                changed = True
            else:
                next[y].append(curr[y][x])
    #print(next)
    return next, changed


if __name__ == "__main__":
    f = open("inp11_1.txt", "r")
    inp = f.readlines()
    print(main(inp))