import re

def parse_input():
     pattern = re.compile(r"(\d+)-(\d+)\s([a-zA-Z]{1}):\s(\w+)")
     f = open("input2.txt", 'r')
     for x in f:
         m = pattern.search(x)
         if m:
             yield int(m[1]), int(m[2]), str(m[3]), m[4]


def part1():
    passes = 0
    for mini, maxi, letter, password in parse_input():        
        count = password.count(letter)
        if count >= mini and count <= maxi:
            passes += 1
    print(passes)


def part2():
    passes = 0
    for mini, maxi, letter, password in parse_input():
        count = password.count(letter)
        if (password[mini - 1] == letter or password[maxi - 1] == letter):
            if password[mini - 1] != password[maxi - 1]:
                passes += 1


part1()
part2()
