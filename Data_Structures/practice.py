import sys


def calc(v, index, r):
    temp = 10000
    for j in range(len(v)):
        if j >= index:
            if int(n[j]) < temp and not int(n[j]) in r:
                if int(n[j]) > r[len(r) - 1]:
                    temp = int(n[j])
    return temp


r = []
n = int(input())
for i in range(n):
    result = []
    name = sys.stdin.readline().rstrip('\n')
    n = name.split()
    mn = min
    result.append(int(mn))
    index = n.index(mn)
    for l in range(len(n)):
        if l > index:
            num = calc(n, l, result)
            index = n.index(str(num))
            result.append(num)
    r.append(result)
s = ''
for i, items in enumerate(r):
    for j, l in enumerate(items):
        if j == 0:
            s = f'Case#{i + 1}: {len(r[i])} {l}'
        else:
            s += f' {l}'
    print(s)