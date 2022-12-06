def part1(a):
    lst = []
    with open(a) as f:
        for line in f:
            for l in line:
                lst.append(l)
    # reference to other items in list to check:
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
    #create sublist with 14 items:
    for i in range(13, len(lst)):
        for j in range(0, 14):
            lst2.append(lst[i-j])
            # if set of list is shorter than lenght of list break
            if len(lst2) != len(set(lst2)):
                break
        if len(lst2) == len(set(lst2)):
            print(i + 1)
        lst2.clear()


def main():
    input_day_6 = 'input.txt'
    part1(input_day_6)
    part2(input_day_6)


if __name__ == "__main__":
    main()
