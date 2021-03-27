"""
inputs:
    t : test case
    n, m  : 1 <= m <= n <= 1000000000 

"""


for t in range(int(input())):
    m , n = list(map(int,input().split()))
    primes = set()
    for number in range(m, n+1):
        stat = True
        for i in primes:
            if not(number%i):
                stat = False
                break
        if stat and number>1:
            primes.add(number)
            print(number)
    print()
