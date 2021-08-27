n,k=list(map(int, input().split()))
temp=list(map(int, input().split()))
slide_sum=0
ans=0
temp_k=k
j=temp_k-1
for i in range(k):
    slide_sum += temp[i]
slide_sumd = slide_sum

if k==n:
    ans=slide_sum/n
elif k==1 :
    ans=max(temp)
else :
    while temp_k < n :
        j=temp_k-1
        while j<n-1:
            if slide_sum/temp_k > ans :
                ans = slide_sum/temp_k
            slide_sum = slide_sum - temp[j-temp_k+1] + temp[j+1]
            j=j+1
        slide_sumd = slide_sumd + temp[temp_k]
        slide_sum = slide_sumd
        temp_k +=1

print(ans)
