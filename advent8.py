import copy

def parse_input(in_f):
    instr = []
    f = open(in_f, 'r')
    for idx, x in enumerate(f):
        s = x.split(" ")
        if len(s) == 2:
            instr.append((idx, s[0].strip(), int(s[1].strip())))
    return instr


class intcode_again:
    acc = 0
    pc = 0
    history = []
    instr = []
    _dispatch = {}

    def __init__(self, prog):
        self.instr = copy.deepcopy(prog)

        self._dispatch = { 'jmp' : lambda x : self.jump(x),
                           'acc' : lambda x : self.accumulate(x),
                           'nop' : lambda x : self.noop(x),
                         }

    def noop(self, val):
        self.pc += 1

    def jump(self, val):
        self.pc += val

    def accumulate(self, val):
        self.pc += 1
        self.acc += val 

    def run_instruction(self, instr):
        if instr[0] not in self.history:
            print(instr)
            self._dispatch[instr[1]](instr[2])
            self.history.append(instr[0])
            return None
        else:
            return self.acc

    def print_state(self):
        print(f"PC: {self.pc} ACC: {self.acc}, {self.history}")

    def run(self):
        print("Starting the new intcode")
        res = self.run_instruction(self.instr[0])
        cnt = 0
        while res is None:
            print(cnt)
            res = self.run_instruction(self.instr[self.pc])
            self.print_state()
            cnt += 1
        return(res)
 

def part1(in_f):
    instr = parse_input(in_f)
    interp = intcode_again(instr)
    return interp.run()


#print(parse_input("input8.txt"))
#assert(part1("test8.txt" == 5))
print(part1("input8.txt"))


