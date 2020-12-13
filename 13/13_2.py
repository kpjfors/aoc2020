def main(inp):
    buses = inp[1].strip().split(",")
    busesaug = []

    idx = 0
    for i in buses:
        if i!="x":
            busesaug.append((idx, int(i)))
        idx += 1

    period = busesaug[0][1]
    timestamp = busesaug[0][0]
    for bus in busesaug[1:]:
        while ((timestamp + bus[0]) % bus[1]) != 0:
            timestamp = timestamp + period
        period = period * bus[1]
    return timestamp

if __name__ == "__main__":
    f = open("inp13_1.txt", "r")
    inp = f.readlines()
    print(main(inp))
