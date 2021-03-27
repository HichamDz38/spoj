"""
inputs:
    t : test case
    n, m  : 1 <= m <= n <= 1000000000 

"""


for t in range(int(input())):
    m , n = list(map(int,input().split()))
    for number in range(m, n+1):
        stat = True
        for i in range(2,int(number**0.5)+1):
            # print('=======>', number, i, number%i)
            if not(number%i):
                stat = False
                break
        if stat and number>1:
            print(number)
    print()
