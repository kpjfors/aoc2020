def main(inp):
    rules, myticket, neartickets = inp.split("\n\n")
    goodnums = set()
    errorrate = 0
    for row in rules.split("\n"):
        name, nums = row.split(": ")
        range1, range2 = nums.split(" or ")
        range1 = list(map(int, range1.split("-")))
        range2 = list(map(int, range2.split("-")))
        for i in range(range1[0], range1[1] + 1):
            goodnums.add(i)
        for i in range(range2[0], range2[1] + 1):
            goodnums.add(i)
    neartickets = neartickets.split("\n")
    neartickets = neartickets[1:len(neartickets) - 1]
    for i in neartickets:
        for j in i.split(","):
            if int(j) not in goodnums:
                errorrate += int(j)

    return errorrate


if __name__ == "__main__":
    f = open("inp16_1.txt", "r")
    inp = f.read()
    print(main(inp))
