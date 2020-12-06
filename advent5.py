def parse_input(in_f):
    f = open(in_f, 'r')
    for x in f:
        yield x.strip()
    f.close()

def interpret_code(code, maximum, higher, lower):
    s = 0
    r = maximum
    for c in code:
        r = (r + 1) // 2
        if c is higher:
            s += r
    return s


def parse_column(code):
    return interpret_code(code, 8, 'R', 'L')


def parse_row(code):
    return interpret_code(code, 127, 'B', 'F')
    

def parse_ticket(ticket):
    row = parse_row(ticket[0:-3])
    column = parse_column(ticket[-3:])
    seat_id = row * 8 + column
    return row, column, seat_id

def part1(in_f):
    max_id = 0
    for ticket in parse_input(in_f):
        row, column, seat_id = parse_ticket(ticket)
        if seat_id > max_id:
            max_id = seat_id
    return max_id


def part2(in_f):
    max_seat = part1(in_f)
    empty_seats = []
    empty_seats.extend(range(1, max_seat + 1))
    for ticket in parse_input(in_f):
        _, _, seat_id = parse_ticket(ticket)
        print(seat_id)
        empty_seats.remove(seat_id)
    return empty_seats

#part1("test5.txt")
print(part1("input5.txt"))
print(part2("input5.txt"))

