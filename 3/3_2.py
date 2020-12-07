def trees(slope, right, down):
    i = 0
    j = 0
    count = 0
    while i < len(slope):
        if slope[i][j] == "#":
            count += 1
        j = (j + right) % len(slope[0])
        i += down
    return count

def main(inp):
    slope = list(map(lambda x: list(x.strip()), inp))
    product = 1
    toboggans = [(1,1),(3,1),(5,1),(2,1),(1,2)]
    for i in toboggans:
        product *= trees(slope, i[0], i[1])
    return product

if __name__ == "__main__":
    f = open("inp3_1.txt", "r")
    inp = f.readlines()
    print(main(inp))