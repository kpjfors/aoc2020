def main(inp):
    inp = list(map(int,inp))
    lst = sorted(inp)
    lst.insert(0,0)
    lst.insert(len(lst), max(lst)+3)

    for i in range(len(lst)):
        if i+1 == len(lst):
            return (skiplist.count(1), skiplist.count(3) + 1, skiplist.count(1)*(skiplist.count(3)))
        else:
            skiplist.append(lst[i+1]-lst[i])

if __name__ == "__main__":
    f = open("inp10_1.txt", "r")
    inp = f.readlines()
    print(main(inp))