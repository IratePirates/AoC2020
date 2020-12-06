import re


def parse_input(in_f):
    f = open(in_f, 'r')
    tokens = []
    dict_rep = {}
    for x in f:
        if x[0] is not "\n":
            s = str(x)
            tokens += s.split(" ")
        else:
            for t in tokens:
                e = t.strip('\n').split(':')
                dict_rep.update({e[0] : e[1]})
            tokens = []
            yield dict_rep
            dict_rep = {}
    f.close()


def validate_num(num, length, mini=None, maxi=None):
    if len(num) == length:
        if mini and int(num) >= mini:
            if maxi and int(num) <= maxi:
                return True
    return False

pid_p = re.compile(r'[0-9]{9}')
def validate_passport_number(val):
    if len(str(val)) == 9:
        m = pid_p.search(val)
        if m:
            return True
    return False

def validate_height(val):
    units = val[-2:]
    value = val[0:-2]
    if "in" in units:
        if int(value) >= 59 and int(value) <= 76:
            return True
    elif "cm" in units:
        if int(value) >= 150 and int(value) <= 193:
            return True
    return False


hair_p = re.compile(r"(#[0-9a-f]{6})")
def validate_hair(val):
    m = hair_p.search(val)
    if m:
        return True
    return False


def validate_eye(val):
    if val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return True
    return False

val_dispatch = {
        'byr': lambda x : validate_num(x, 4, 1920, 2002),
        'iyr': lambda x : validate_num(x, 4, 2010, 2020),
        'eyr': lambda x : validate_num(x, 4, 2020, 2030),
        'hgt': lambda x : validate_height(x),
        'hcl': lambda x : validate_hair(x),
        'ecl': lambda x : validate_eye(x),
        'pid': lambda x : validate_passport_number(x),
        'cid': lambda x : True,
}


def part1(in_f):
    cnt = 0
    for a in parse_input(in_f):
        if len(a) == 8:
            cnt += 1
        elif len(a) == 7:
            if 'cid' not in a:
                cnt += 1
    print(cnt)

def test_p2():
    assert val_dispatch["byr"]("2002") == True
    assert val_dispatch["byr"]("2003") == False
    assert val_dispatch["hgt"]("60in") == True
    assert val_dispatch["hgt"]("190cm") == True
    assert val_dispatch["hgt"]("190in") == False
    assert val_dispatch["hgt"]("190") == False
    assert val_dispatch["hcl"]("#123abc") == True
    assert val_dispatch["hcl"]("#123abz") == False
    assert val_dispatch["hcl"]("123abc") == False
    assert val_dispatch["ecl"]("brn") == True
    assert val_dispatch["ecl"]("wat") == False
    assert val_dispatch["pid"]("000000001") == True
    assert val_dispatch["pid"]("0123456789") == False

def part2(in_f):
    cnt = 0
    for a in parse_input(in_f):
        tmp = 0
        if len(a) == 8:
            for k, v in a.items():
                if val_dispatch[k](v):
                    tmp += 1
                if tmp == 8:
                    cnt += 1
        elif len(a) == 7:
            if 'cid' not in a:
                for k, v in a.items():
                    if val_dispatch[k](v):
                        tmp += 1
                if tmp == 7:
                    cnt += 1
    print(cnt)


#part1("test4.txt")
#part1("input4.txt")

test_p2()
part2("test4a.txt")
part2("input4.txt")

