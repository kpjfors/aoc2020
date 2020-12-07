def main(inp):
    maxid = 0
    for i in inp:
        a = calculateseat(i)[2]
        if a > maxid:
            maxid = a
    return maxid

def calculateseat(inp):
    row = 0
    col = 0
    rowbits = list("0000000")
    colbits = list("000")

    lst = list(inp.strip())
    ####ROW
    for i in range(len(rowbits)):
        if inp[i] == "B":
            rowbits[i] = "1"
            row = int("".join(rowbits),2)
    ####COL
    for i in range(len(colbits)):
        if inp[i+7] == "R":
            colbits[i] = "1"
            col = int("".join(colbits),2)
    print(row, col, row*8+col)
    return(row, col, row*8+col)




if __name__ == "__main__":
    f = open("inp5_1.txt", "r")
    inp = f.readlines()
    print(main(inp))