def input_() -> tuple:
    n = int(input())
    rows = []
    for j in range(n):
        colls = []
        for i in input().split():
            colls.append(int(i))
        rows.append(colls)

    return (n, rows, int(input()))

def get_max_first_coll(n: int, a: list[list]) -> int:
    if n == 1:
        return 0
    i_min = 0
    for index in range(1, n):
        if (a[i_min][0] < a[index][0]):
            i_min = index
    return i_min

def get_summ_row(n: int, a: list[list]) -> list:
    res = []
    for i in range(n):
        sum = 0
        for j in range(0,a[i][0]):
            sum += a[i][j+1]
        res.append(sum)
    return res


def main() -> None:
    n, a, pickles = input_()
    sums = get_summ_row(n, a)
    res_int = [0]*n
    looc_at = list(range(n))
    while pickles != 0:
        for i in looc_at:

            res_int[i] += (int(round(sums[i]/a[i][0])))
            pickles -= int(round(sums[i]/a[i][0]))
            if pickles == 0: break
        if pickles != 0:
            max_val = get_max_first_coll(n,a)
            res_int[max_val] += pickles
            pickles = 0

    res_str = [str(i) for i in res_int]
    
    print(' '.join(res_str))


main()
