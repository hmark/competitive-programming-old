import math


def construct_the_string(n, a, b):
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    result = ''
    index = 0
    for i in range(0, n):
        result += abc[index]
        index = (index + 1) % b

    print(result)


t = int(input())
for i in range(0, t):
    n, a, b = map(int, (input().split()))
    construct_the_string(n, a, b)
