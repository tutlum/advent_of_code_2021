import sys

def readfile(filen):
    f=open(filen,"r")
    content = f.read()
    m = [int(x) for x in content.split("\n") if x!=""]
    f.close()
    return m

def solution(filen):
    m=readfile(filen)
    print("Increases: {}".format(countMeasure(m)))

    l=[]
    for i in range(len(m)):
        l.append(m[i]+m[i-1]+m[i-2])
    print("Smoothe increases: {}".format(countMeasure(l)))

def countMeasure(m):
    count = 0
    for i in range(1,len(m)):
        if m[i]>m[i-1]: count+=1
    return count

if __name__ == '__main__':
    if len(sys.argv)>1:
        solution(sys.argv[1])
    else: solution("input1.txt")
