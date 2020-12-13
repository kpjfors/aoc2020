def main(inp):
    posx = 0
    posy = 0
    dirs = {"N":(0,1), "S":(0,-1), "W":(-1,0), "E":(1,0)}
    rotlist = ((1, 0), (0, 1), (-1, 0), (0, -1))
    rotind = 0
    dir = rotlist[rotind]
    for i in inp:
        instr, dist = i[:1], int(i[1:].strip())
        if instr in dirs:
            posx += dirs[instr][0]*dist
            posy += dirs[instr][1] * dist
        elif instr != "F":

            steps = int(dist/90)

            if instr == "L":
                rotind = rotind+steps
                dir = rotlist[rotind%4]
            else:
                rotind = rotind-steps
                dir = rotlist[rotind%4]
            print(rotind)

        else:
            posx += dir[0] * dist
            posy += dir[1] * dist
    print(posx, posy)
    return(abs(posx)+abs(posy))

if __name__ == "__main__":
    f = open("inp12_1.txt", "r")
    inp = f.readlines()
    print(main(inp))
