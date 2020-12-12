def main(inp):
    inp = list(map(int,inp))
    lst = sorted(inp)
    lst.insert(0, 0)
    lst.insert(len(lst), max(lst)+3)

    return calculateroad(lst)

def calculateroad(lst):
    nodes = {0: 1}
    for i in lst[1:]:
        nodes[i] = nodes.get(i-1, 0) + nodes.get(i-2, 0) + nodes.get(i-3, 0)
    return nodes[max(lst)]


if __name__ == "__main__":
    f = open("inp10_1.txt", "r")
    inp = f.readlines()
    print(main(inp))