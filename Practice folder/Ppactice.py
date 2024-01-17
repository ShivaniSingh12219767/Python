n=int(input())
for i in range(1,n+1):
    sum=i
    for j in range(0,i):
        print(sum,end=" ")  
        sum+=n-j-1 
    print()    