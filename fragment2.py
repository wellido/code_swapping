import bisect


def take_second(elem):
    return elem[1]


def define_p(data):
    start = [item[0] for item in data]
    end = [item[1] for item in data]
    p = [0, ]
    for j in range(len(data)):
        index = bisect.bisect_right(end, start[j])
        p.append(index)
    return p

i = 0
td = [[0, 4, 2], [1, 6, 4], [5, 7, 4], [2, 9, 7], [8, 10, 2], [8, 11, 1]]
pi = define_p(td)
ss = [0] * (len(td) + 1)
f = []
l = len(td)
td.sort(key=take_second)

print("i = ", i)
print("l = ", l)
# print("cd", cd)
print("td = ", td)
print("ss = ", ss)
print("f = ", f)
print("pi = ", pi)

###################################### fragment 2 #########################################
while i < l:
    cd = td[i][2] + ss[pi[i + 1]]
    if cd < ss[i]:
        ss[i + 1] = ss[i]
        f = f + [[0, i]]
    else:
        ss[i + 1] = cd
        f = f + [[1, pi[i + 1]]]
    i += 1
###################################### fragment 2 #########################################
print("cd", cd)
