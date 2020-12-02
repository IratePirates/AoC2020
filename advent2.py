import re

def part1():
    passes = 0
    pattern = re.compile(r"(\d+)-(\d+)\s([a-zA-Z]{1}):\s(\w+)")
    f = open("input2.txt", 'r')
    for x in f:
        m = pattern.search(x)
        if m:
            min_r = int(m[1])
            max_r = int(m[2])
            letter = str(m[3])
            password = m[4]

            count = password.count(letter)
            if count >= min_r and count <= max_r:
                passes += 1
    print(passes)

def part2():
    passes = 0
    pattern = re.compile(r"(\d+)-(\d+)\s([a-zA-Z]{1}):\s(\w+)")
    f = open("input2.txt", 'r')
    for x in f:
        m = pattern.search(x)
        if m:
            min_r = int(m[1]) - 1
            max_r = int(m[2]) - 1
            letter = str(m[3])
            password = m[4]

            count = password.count(letter)
            if (password[min_r] == letter or password[max_r] == letter):
                if password[min_r] != password[max_r]:
                    passes += 1
    print(passes)


part1()
part2()
