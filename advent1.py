import os
import sys

in_ra = []
f = open("input1.txt", 'r')
for x in f:
    in_ra.append(int(x))

# print(in_ra)
def part1(in_ra):
    for x in in_ra:
        other = 2020 - x
        if other in in_ra:
            print(x, other, x * other)
            return

def part1a(in_ra):
    a = [x*(2020 - x) for x in in_ra if (2020 - x) in in_ra]
    print(a[0])

def part2(in_ra):
    ra = in_ra
    ra.sort()
    for x in ra:
        for y in ra:
            for z in ra:
                if (x + y + z == 2020):
                    print(z, y, z, x*y*z)
                    return

part1(in_ra)
part1a(in_ra)
part2(in_ra)

