def main(inp):
    tot = 0

    lst = [item for sublist in inp for item in sublist]
    longstr = "".join([elem for elem in lst])
    longlst = longstr.split("\n\n")
    longlstclean = [i.replace("\n", " ").split() for i in longlst]
    print(longlstclean)

    for i in longlstclean:
        resp = set(list())
        for j in i:
            resp = resp.union(set(j))

        tot += len(resp)
    return tot

if __name__ == "__main__":
    f = open("inp6_1.txt", "r")
    inp = f.readlines()
    print(main(inp))
