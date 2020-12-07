import sys
sys.setrecursionlimit(1000)

def main(inp):
    bags = makebags(inp)
    print(bags)
    return inside(bags, "shinygold")

def inside(bags, bag):
    found = 0
    for k in bags[bag]:
        for j in range(bags[bag][k]):
            found += 1 + inside(bags, k)
    return found

def makebags(inp):
    smallbags = {}
    for i in inp:
        cont = {}
        leap = i.split(" bags contain")
        name = leap[0].replace(" ", "")
        if leap[1].strip() != "no other bags.":
            for j in leap[1].split(","):
                cont["".join(j.split(" ")[2:4])] = int(j.split(" ")[1])
        smallbags[name] = cont
    return smallbags

if __name__ == "__main__":
    f = open("inp7_1.txt", "r")
    inp = f.readlines()
    print(main(inp))
