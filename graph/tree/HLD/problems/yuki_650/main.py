#!/usr/bin/env python3
# from typing import *

MOD = 1000000007

# def solve(n: str, a: List[str], b: List[str], q: str, query: List[str]) -> Any:
def solve(n, a, b, q, query):
    pass  # TODO: edit here

# generated by online-judge-template-generator v4.4.0 (https://github.com/kmyk/online-judge-template-generator)
def main():
    n = input()
    a = [None for _ in range(n - 1)]
    b = [None for _ in range(n - 1)]
    for i in range(n - 1):
        a[i], b[i] = input().split()
    q = input()
    query = [None for _ in range(q)]
    for i in range(q):
        query[i] = input()
    ans = solve(n, a, b, q, query)
    print(ans)  # TODO: edit here

if __name__ == '__main__':
    main()
