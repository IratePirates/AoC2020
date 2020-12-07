import re
import copy


bag_p = re.compile(r"(\d) ([a-z ]*) bag")
def parse_input(in_f):
    f = open(in_f, 'r')
    bags = {}
    for x in f:
        k = x.split(" bags contain")[0]
        v_str = x.split(" bags contain")[1]
        inner_bags = v_str.split(',')
        if inner_bags is "no other bags":
            bags.update({k: None})
        else:
            tmp = []
            for b in inner_bags:
                m = bag_p.search(b)
                if m:
                    tmp.append((int(m[1]), m[2]))
            bags.update({k: tmp})
    return bags


def update_contents(bag_list, orig_bag):
    new_contents = []
    cnt = 0
    for bag in orig_bag:
        cnt += bag[0]
        new_bags = bag_list[bag[1]]
        for n in new_bags:
            new_contents.append((bag[0] * n[0], n[1]))
        else:
            cnt += bag[0]
    return new_contents, cnt


def part1(in_f, target="shiny gold"):
    cnt = 0
    bags = parse_input(in_f)
    remaining_bags = copy.deepcopy(bags)
    
    itr = 0
    while len(remaining_bags) > 0 and itr < 255:
        tmp_bags = {}
        for k, v in remaining_bags.items():
            if not v:
                pass
            else:
                res = [w[1] in target for w in v]
                if any(res):
                    cnt += 1
                else:
                    new_in, _ = update_contents(bags, v)
                    tmp_bags.update({k:new_in})
        remaining_bags = tmp_bags
        itr += 1
    return cnt


def part2(in_f, target="shiny gold"):
    bags = parse_input(in_f)
#    print(bags)

    remaining_bags = bags[target]    
    cnt = sum([b[0] for b in remaining_bags])
    print(remaining_bags)
   
    itr = 0
    while itr < 5 and len(remaining_bags) > 0:
        remaining_bags, i =  update_contents(bags, remaining_bags)
        cnt += i
        print(cnt, i, remaining_bags)
        itr += 1
    return cnt

#print(parse_input("test7.txt"))
assert(part1("test7.txt") == 4)
assert(part1("input7.txt") == 261)
#assert(part2("test7a.txt") == 126)
print(part2("input7.txt"))

