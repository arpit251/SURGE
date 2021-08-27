
n,k=list(map(int, input().split()))
temp=list(map(int, input().split()))
high=0
for i in range(1,n-k+2):
    for j in range(1,n-k+3-i):
        sum=0
        for p in range(j-1, j+k+i-2):
            sum=sum +temp[p]
            a=(sum/(k+i-1))
        if a> high:
            high=a
          
print(high)
