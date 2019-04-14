"""
## Name of Prob
C. Serval and Parenthesis Sequence

## Link
https://codeforces.com/contest/1153/problem/C

## Note

## Input

## Output

## Strategy
Complete string needs half of '(' and ')'
Fill '(' first and ')'
It will fails when left stack empty before last of string

"""
_DEBUG = True
n = int(input())
s = input()


def solve(s):
    ns = list(s)
    l = len(ns)

    lc = rc = 0
    for e in s:
        if e == '(':
            lc += 1
        elif e == ')':
            rc += 1

    l_stack = 0

    for i in range(l):
        e = s[i]
        if e == '(':
            l_stack += 1
        elif e == ')':
            l_stack -= 1
        elif lc < l // 2:
            ns[i] = '('
            l_stack += 1
            lc += 1
        else:
            ns[i] = ')'
            l_stack -= 1
            rc += 1
        if i != l - 1 and l_stack <= 0:
            return None

    return ''.join(ns) if l_stack == 0 else None


res = solve(s)
if res is None:
    print(':(')
else:
    print(res)
