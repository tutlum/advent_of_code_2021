import sys
#import numpy as np

''' read file name and outputs an numpy array '''
def readfile(filen):
    f=open(filen,"r")
    content = f.read()
    m = [x for x in content.split("\n") if x!=""]
    f.close()
    return m

def solution(filen):
    m=readfile(filen)
    data = [[int(y) for y in x] for x in m]
    gamma = calc_gamma(data)
    epsilon = epsilon_from_gamma(gamma)
    power=bin_to_dec(gamma)*bin_to_dec(epsilon)
    print("Power: {}, from gamma={} and epsilon={}".format(power,gamma,epsilon))

    oxygen=filter_list(data)
    co2=filter_list(data, False)
    life=bin_to_dec(oxygen)*bin_to_dec(co2)
    print("Life support rating: {}, from oxygen={} and co2={}".format(life,oxygen,co2))


'''
in: array of bits
out: gamma rate (most frequent bit in each column)
'''
def calc_gamma(matrix):
    size = len(matrix[1])
    halfanz = len(matrix)/2
    gamma = []
    for i in range(size):
        gamma.append( get_most_common(matrix, i) )
    return gamma

'''
filters the incoming list bit after bit until only one entry is left
in: list of binary list entries
out: one list entry
'''
def filter_list(data_l, most=True):
    data_size=len(data_l[0])
    new_data=data_l
    #print(new_data)
    while len(new_data)>1:
        for i in range(data_size):
            mc=get_most_common(new_data,i)
            if not most: mc=1-mc
            new_data=filter_list_index(new_data, i, mc)
            #print(mc, new_data)
            if len(new_data)==1: return new_data[0]

'''
filters the list where the bit in the position is the given bit
'''
def filter_list_index(data_l, position, bit):
    return [ dl for dl in data_l if dl[position] == bit ]

'''
calculates the most common bit in the given position of the list of entries
'''
def get_most_common(matrix, position):
    halfanz = len(matrix)/2
    zeros = 0
    for j in range(len(matrix)):
        if matrix[j][position] == 0:
            zeros+=1
            if zeros > halfanz: break;
    if zeros > halfanz: return 0
    else: return 1

'''
inverts a binary
'''
def epsilon_from_gamma(gamma):
    return [1-x for x in gamma]

'''
converts a binary number to a decimal
'''
def bin_to_dec(bin_num):
    return int("".join([str(x) for x in bin_num]),2)

if __name__ == '__main__':
    if len(sys.argv)>1:
        solution(sys.argv[1])
    else: solution("input1.txt")
