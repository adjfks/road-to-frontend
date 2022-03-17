N = 800005
s = []


def init_set():
    for i in range(N):
        s.append(i)


def find_set(x):
    if(x != s[x]):
        s[x] = find_set(s[x])
    return s[x]


def merge_set(x, y):
    x = find_set(x)
    y = find_set(y)
    if(x != y):
        s[x] = s[y]
