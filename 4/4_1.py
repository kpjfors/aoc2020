import re  # regex


def main(inp):
    required = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    passports = []
    tot = 0

    lst = [item for sublist in inp for item in sublist]
    longstr = "".join([elem for elem in lst])
    longlst = longstr.split("\n\n")
    longlstclean = [i.replace("\n", " ").split() for i in longlst]

    for i in longlstclean:
        passport = {}
        for j in i:
            passport[j.split(":")[0]] = j.split(":")[1]
        passports.append(passport)

    counter = 0
    lst = []

    for i in passports:
        tot += 1
        if required.issubset(set(i.keys())):
            counter += 1
    return counter


if __name__ == "__main__":
    f = open("inp4_1.txt", "r")
    inp = f.readlines()
    print(main(inp))
