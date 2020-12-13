def main(inp):
    posx = 0
    posy = 0
    wpx = 10
    wpy = 1
    dirs = {"N":(0,1), "S":(0,-1), "W":(-1,0), "E":(1,0)}
    rotind = 0

    for i in inp:
        instr, dist = i[:1], int(i[1:].strip())
        if instr in dirs:
            wpx += dirs[instr][0] * dist
            wpy += dirs[instr][1] * dist
        elif instr != "F":

            if instr == "R":
                dist = -dist
            wpx, wpy = rotate(wpx, wpy, dist)
            print(wpx, wpy)

        else:
            posx += wpx * dist
            posy += wpy * dist
    print(posx, posy)
    return(abs(posx)+abs(posy))

def rotate(x, y, degrees):
    if degrees == -90 or degrees == 270:
        return y, -x
    if degrees == -180 or degrees == 180:
        return -x, -y
    if degrees == -270 or degrees == 90:
        return -y, x


if __name__ == "__main__":
    f = open("inp12_1.txt", "r")
    inp = f.readlines()
    print(main(inp))
