def part1(a):
    lst = []
    with open(a) as f:
        for line in f:
            for l in line:
                lst.append(l)

    for i in range(3, len(lst)):
        if ord(lst[i]) != ord(lst[i - 1]) and ord(lst[i]) != ord(lst[i - 2]) and ord(lst[i]) != ord(lst[i - 3]):
            if ord(lst[i - 1]) != ord(lst[i - 2]) and ord(lst[i - 1]) != ord(lst[i - 3]):
                if ord(lst[i - 2]) != ord(lst[i - 3]):
                    print(i + 1)
                    break


def part2(a):
    lst = []
    lst2 = []
    count = 0
    with open(a) as f:
        for line in f:
            for l in line:
                lst.append(l)

    for i in range(13, len(lst)):
        for j in range(0, 14):
            lst2.append(lst[i-j])
        if len(lst2) <= len(set(lst2)):
            print(i + 1)
        lst2.clear()


def main():
    
    input_day6 = 'input.txt'
    part1(input_day6)
    part2(input_day6)


if __name__ == "__main__":
    main()
