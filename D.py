def primfacs(n: int):
    i = 2
    primfac = [1]
    while i * i <= n:
        while n % i == 0:
            primfac.append(int(i))
            n = n / i
        i = i + 1
    if n > 1:
        primfac.append(int(n))
    return primfac


def intersec(a: list, b: list):
    res = []
    a.sort()
    b.sort()
    for a_i in range(len(a)):
        if a[a_i] in b:
            res.append(a[a_i])
            b.remove(a[a_i])
    return res

def difference(a: list, b: list):
    a.sort()
    b.sort()
    res = []
    b_copy = []
    for item in a:
        res.append(item)

    for item in b:
        b_copy.append(item)
    
    for item in b_copy:
        if item in res:
            res.remove(item)

    return res

def fun():

    a, b = input().split()

    a = int(a)
    b = int(b)

    if (a == b) :return a

    prim_a = primfacs(a)
    prim_b = primfacs(b)

    a_min_b = difference(prim_a,prim_b)
    b_min_a = difference(prim_b,prim_a)

    max_a = 1
    max_b = 1
    if len(a_min_b) != 0 :
        max_a = max(list(set(a_min_b)))
    if len(b_min_a) != 0 :
        max_b = max(list(set(b_min_a)))

    if max_a > max_b:
        prim_b.append(max_a)
    else:
        prim_a.append(max_b)

    gcd_list = intersec(prim_a, prim_b)

    res = 1
    for item in gcd_list:
        res *= item

    return res


arr = []
n = int(input())
for _ in range(n):
    arr.append(fun())

for item in arr:
    print(item)
