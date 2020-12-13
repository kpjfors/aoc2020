import math

def main(inp):
    departtime = int(inp[0])
    buses = inp[1].replace(",x","").strip().split(",")
    buses = list(map(int, buses))
    print(departtime,buses)
    mintimebus = [9999,0]
    for i in buses:
        fractpart, intpart = math.modf(departtime / i)
        print(round((intpart+1-departtime / i)*i), i)
        if round((intpart+1-departtime / i)*i) < mintimebus[0]:
            mintimebus = [round((intpart+1-departtime / i)*i), i]
    return(mintimebus[0]*mintimebus[1])


if __name__ == "__main__":
    f = open("inp13_1.txt", "r")
    inp = f.readlines()
    print(main(inp))
