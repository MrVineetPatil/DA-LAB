import random,time
def partition(l,r):
    global a
    pivot=a[l]
    i=l+1
    j=r
    while True:
        while (i<=j and a[i]<=pivot):
            i=i+1
        while (i<=j and a[j]>=pivot):
            j=j-1
        if i>j:
            break
        else:
            a[i],a[j]=a[j],a[i]
    a[l],a[j]=a[j],a[l]
    return j

def quicksort(l,r):
    global a
    if l<r:
        mid=partition(l,r)
        quicksort(l,mid-1)
        quicksort(mid+1,r)


a=[random.randint(0,100) for i in range(10)]
print(a)
start=time.time()
time.sleep(1)
quicksort(0,len(a)-1)
end=time.time()
print(a)
print(end-start,"seconds")

