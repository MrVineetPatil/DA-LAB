import random,time
def megesort(alist):
    print("splitting",alist)
    if len(alist)>1:
        mid=len(alist)//2
        lefthalf=alist[0:mid]
        righthalf=alist[mid:]

        megesort(lefthalf)
        megesort(righthalf)

        i=0
        j=0
        k=0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
        print("Merging",alist)

alist=[random.randint(0,100) for i in range(10)]
start=time.time()
time.sleep(1)
megesort(alist)
end=time.time()
print(end-start,"seconds")