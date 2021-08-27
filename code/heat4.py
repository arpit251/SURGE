
n,k=list(map(int, input().split()))
temp=list(map(int, input().split()))
def mean1(list1, start, end):
    add=0
    for i in range(start, end):
        add+=list1[i]
    return(add/(end-start))
list_index=[]
same=0
endgame=0
#finding maximum
for i in range(n-k+1):
  
    u=mean1(temp,i,i+k)
 
    if i == 0:
        high = u
        first_high=u
    else:
        if u > high :
            high=u
            list_index.append(i)
        elif u==high:
            same+=1
            list_index.append(i)
    if i==n-k and first_high==high :
        list_index.insert(0,0)
        
if n==k:
    list_index.append(0)


def changedmean(mainlist, index):
    global k;
    global high;
    global endgame;
    a=index
    if a==0 and k!=n:
        if mainlist[a+k] > high:
            high = (k*high + mainlist[a+k])/(k+1)
            k+=1
            return(a)
        else :
            endgame+= 1
    elif a+k == len(mainlist) and a!=0 :
        if mainlist[a-1] > high:
            high = (k*high + mainlist[a-1])/(k+1)
            k+=1
            return(a-1)
        else :
            endgame+= 1
    elif a==0 and k==n:
        endgame+=1
        
    else :
        if max(mainlist[a+k], mainlist[a-1]) > high:
            high = (k*high + max(mainlist[a+k], mainlist[a-1]))/(k+1)
            k+=1
            if mainlist[a+k] > mainlist[a-1]:
                return(a)
            elif mainlist[a+k] < mainlist[a-1]:
                return(a-1)
            else:
                pass
                
        else:
            endgame+=1

    
        
   
    
for i in range(same+1):
    endgame=0
    d=changedmean(temp,list_index[-1-i])
    while(endgame==0):
        b=d
        d=changedmean(temp, b)

print(high)



    
    
