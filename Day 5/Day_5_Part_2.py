my_dict = dict(
    s1 = ['H', 'B', 'V', 'W', 'N', 'M', 'L', 'P'],
    s2 = ['M', 'Q', 'H'],
    s3 = ['N', 'D', 'B', 'G', 'F', 'Q', 'M', 'L'],
    s4 = ['Z', 'T', 'F', 'Q', 'M', 'W', 'G'],
    s5 = ['M', 'T', 'H', 'P'],
    s6 = ['C', 'B', 'M', 'J', 'D', 'H', 'G', 'T'],
    s7 = ['M', 'N', 'B', 'F', 'V', 'R'],
    s8 = ['P', 'L', 'H', 'M', 'R', 'G', 'S'],
    s9 = ['P', 'D', 'B', 'C', 'N'])
lst = []
with open('input') as f:
    for line in f:
        print(' ')
        print(line)
        line = line.rstrip().split(' ')
        q = int(line[1])
        fr = line[3]
        to = line[5]
        l_fr = my_dict['s' + fr]
        l_to = my_dict['s' + to]

        print('from:', l_fr, 'to:', l_to)
        for i in range(0, q):
            lst.append(l_fr[len(l_fr) - 1])
            del l_fr[len(l_fr) - 1]
        for i in range(0, q):
            l_to.append(lst[len(lst) - 1])
            del lst[len(lst) - 1]
        my_dict['s' + fr] = l_fr
        my_dict['s' + to] = l_to

        print(l_to)
    print(my_dict)
