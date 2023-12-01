f = open('input.txt', 'r')
res = []
words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for line in f: 
    l1 = None
    l2 = l1
    word = ""
    for l in range(len(line)):
        if ord(line[l]) > 47 and ord(line[l]) < 58:
            word = ""
            if l1 == None:
                l1 = line[l]
            l2 = line[l]
        else:
            word = word + line[l]
            counter = 0
            for i in words:
                counter += 1
                for j in range(len(word)):
                    if word[j:] == i:
                        word = word[j+1:]
                        if l1 == None:
                            l1 = str(counter)
                        l2 = str(counter)
    x = l1 + l2
    print('from line:', line , x, "\n")
    res.append(int(x))

print(sum(res))