t=int(raw_input())
c=1
while c<=t:
    m=int(raw_input())
    n=int(raw_input())
    while m<=n:
        if (2**(m-1))%m==1:
            print m
        if m==2 :
            print m
        m+=1
    print '1'
    c+=1