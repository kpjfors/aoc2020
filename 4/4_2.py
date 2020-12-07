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
            if datavalid(i):
                counter += 1
            else:
                print(i)
    return counter


def datavalid(inp):
    eyecolors = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
    if not 1920 <= int(inp['byr']) <= 2002 or len(inp['byr']) != 4:
        print("byr 1920-2002: " + inp['byr'])
        return False
    if not 2010 <= int(inp['iyr']) <= 2020 or len(inp['iyr']) != 4:
        print("iyr 2010-2020    : " + inp['iyr'])
        return False
    if not 2020 <= int(inp['eyr']) <= 2030 or len(inp['eyr']) != 4:
        print("eyr 2020-2030: " + inp['eyr'])
        return False
    if re.match(r"#[a-fA-F0-9]{1,7}", inp['hcl']) is None or len(inp['hcl']) != 7:
        print("hcl: " + inp['hcl'])
        return False
    if not inp['ecl'] in eyecolors:
        print("ecl: " + inp['ecl'])
        return False
    if re.match(r"[0-9]{1,9}", inp['pid']) is None or len(inp['pid']) != 9:
        print("pid: " + inp['pid'])
        return False
    if inp['hgt'][-2:] == "cm":
        if not 150 <= int(inp['hgt'][:-2]) <= 193 or len(inp['hgt'][:-2]) != 3:
            print("hgt 150-193:" + inp['hgt'][-2:] + inp['hgt'][:-2])
            return False
    elif inp['hgt'][-2:] == "in":
        if not 59 <= int(inp['hgt'][:-2]) <= 76 or len(inp['hgt'][:-2]) != 2:
            print("hgt 59-76:" + inp['hgt'][-2:] + inp['hgt'][:-2])
            return False
    else:
        return False
    return True


if __name__ == "__main__":
    f = open("inp4_1.txt", "r")
    inp = f.readlines()
    print(main(inp))
