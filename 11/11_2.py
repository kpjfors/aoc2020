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

    for x in range(len(curr[0])):
        for y in range(len(curr)):
            neighborsoccupied = 0
            for dy, dx in offsets:
                xtot = x+dx
                ytot = y+dy
                while 0<=ytot<len(curr) and 0<=xtot<len(curr) and curr[ytot][xtot] == ".":
                    xtot += dx
                    ytot += dy
                if 0 <= ytot <len(curr) and 0 <= xtot < len(curr[0]) and curr[ytot][xtot] == '#':
                    neighborsoccupied += 1

            #print(neighborsoccupied)
            if curr[y][x] == "L" and neighborsoccupied == 0:
                next[y].append("#")
                changed = True
            elif curr[y][x] == "#" and neighborsoccupied >= 5:
                next[y].append("L")
                changed = True
            else:
                next[y].append(curr[y][x])
    return next, changed


if __name__ == "__main__":
    f = open("inp11_1.txt", "r")
    inp = f.readlines()
    print(main(inp))