import sys
sys.setrecursionlimit(1000)

def main(inp):
    bags = makebags(inp)
    print(bags)
    count = 0
    for bag in bags:
        if containgold(bags, bag):
            count += 1
    return count

def containgold(bags, bag):
    found = 0
    if "shinygold" in bags[bag]:
        found += 1
    else:
        for i in bags[bag]:
            found += containgold(bags, i)
    return found

def makebags(inp):
    smallbags = {}
    for i in inp:
        cont = set()
        leap = i.split(" bags contain")
        name = leap[0].replace(" ", "")
        if leap[1].strip() != "no other bags.":
            for j in leap[1].split(","):
                cont.add("".join(j.split(" ")[2:4]))
        smallbags[name] = cont
    return smallbags

if __name__ == "__main__":
    f = open("inp7_1.txt", "r")
    inp = f.readlines()
    print(main(inp))
