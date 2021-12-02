import sys

''' read file name and outputs a list '''
def readfile(filen):
    f=open(filen,"r")
    content = f.read()
    m = [x for x in content.split("\n") if x!=""]
    f.close()
    return m

def solution(filen):
    m=readfile(filen)
    (direction, depth) = sum_instructions( get_instructions(m) )
    print("Direction, depth: {}, {} -> {}"
          .format(direction, depth, direction*depth))
    (direction, depth) = sum_instr_aim( get_instructions(m) )
    print("With aim: Direction, depth: {}, {} -> {}"
          .format(direction, depth, direction*depth))

'''
in:  m input list
out: list of list of instructions
'''
def get_instructions(m):
    return [x.split(" ") for x in m]

'''
in:  l list of list of instructions
out: tupel of (direction, depth)
     suming up the vectors
'''
def sum_instructions(l):
    direction = 0
    depth = 0
    for v in l:
        if v[0]=="forward": direction+=int(v[1])
        elif v[0]=="down": depth+=int(v[1])
        else: depth-=int(v[1])
    return (direction, depth)

'''
in: l list of  list of instructions
out: tupel of (direction, depth)
     using aim as inbetween step
'''
def sum_instr_aim(l):
    direction = 0
    depth = 0
    aim = 0
    f_t = 0
    for v in l:
        if v[0]=="forward":
            f_t = int(v[1])
            direction += f_t
            depth += f_t * aim
        elif v[0]=="down": aim+=int(v[1])
        else: aim-=int(v[1])
    return (direction, depth)

if __name__ == '__main__':
    if len(sys.argv)>1:
        solution(sys.argv[1])
    else: solution("input1.txt")
