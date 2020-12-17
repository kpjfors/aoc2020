def main(inp):
    rules, myticket, neartickets = inp.split("\n\n")
    rulesdict, goodnums = makerules(rules)
    goodtickets = filtertickets(neartickets, goodnums)
    possibilities = {}
    goodtickets.append(myticket.split("\n")[1])
    for i in range(len(rulesdict)):
        possibilities[i] = set(range(len(rulesdict)))
    for ticket in goodtickets:
        values = list(map(int, ticket.split(",")))
        for idx in range(len(values)):
            for possidx in range(len(possibilities)):
                if not values[idx] in rulesdict[possidx]:
                    possibilities[possidx].remove(idx)
    order = sorted([(i, len(possibilities[i]) - 1) for i in possibilities], key=lambda x: x[1])
    truth = []
    for i in order:
        index, value = (i[0], possibilities[i[0]].pop())
        truth.append((index, value))
        for j in possibilities:
            possibilities[j].discard(value)
    key = sorted(truth)
    retval = 1
    myticket = list(map(int, myticket.split("\n")[1].split(",")))
    for i in range(6):  # first 6 values start w departure.
        retval *= myticket[key[i][1]]

    return retval


def filtertickets(neartickets, goodnums):
    neartickets = neartickets.split("\n")
    neartickets = neartickets[1:len(neartickets) - 1]
    goodtickets = []
    for i in neartickets:
        fail = False
        for j in i.split(","):
            if int(j) not in goodnums:
                fail = True
        if not fail:
            goodtickets.append(i)
    return goodtickets


def makerules(rules):
    retdict = {}
    allgoodnums = set()
    idx = 0
    for row in rules.split("\n"):
        goodnums = set()
        name, nums = row.split(": ")
        range1, range2 = nums.split(" or ")
        range1 = list(map(int, range1.split("-")))
        range2 = list(map(int, range2.split("-")))
        for i in range(range1[0], range1[1] + 1):
            goodnums.add(i)
            allgoodnums.add(i)
        for i in range(range2[0], range2[1] + 1):
            goodnums.add(i)
            allgoodnums.add(i)
        retdict[idx] = goodnums
        idx += 1
    return retdict, allgoodnums


if __name__ == "__main__":
    f = open("inp16_1.txt", "r")
    inp = f.read()
    print(main(inp))
