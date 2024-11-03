def input_() -> tuple:
    n = int(input())
    a = []
    for i in input().split():
        a.append(int(i))
    return (n, a)


def func(a: list) -> int:
    if (sorted(a) != a):
        return -1
    return max(a) - min(a)


def main() -> None:
    n, a = input_()
    print(func(a))


main()
