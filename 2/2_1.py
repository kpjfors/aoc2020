def main(nums):
    aa = list(map(lambda x: x.split(":"), nums))
    counter = 0
    for i in aa:
        ktemp = i[0].split(" ")
        range = list(map(int, ktemp[0].split("-")))
        letter = ktemp[1]
        lettercount = list(i[1]).count(letter)
        if (lettercount >= range[0]) and (lettercount <= range[1]):
            counter += 1

    return (counter)


if __name__ == "__main__":
    f = open("inp2_1.txt", "r")
    inp = f.readlines()
    print(main(inp))
