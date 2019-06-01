import random, time
count=0
def merge_sort(li):
    if len(li)<2:
        return li
    mid=(len(li))//2
    return merge(merge_sort(li[:mid]),merge_sort(li[mid:]))

def merge(l,r):
    global count
    i=0
    j=0
    result=[]
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            result.append(l[i])
            i+=1
        else:
            result.append(r[j])
            count=count+(len(l)-i)
            j+=1
    result.extend(l[i:])
    result.extend(l[j:])
    return result

a=[random.randint(0,100)for i in range(10)]
print("Unsorted list :",a)
start=time.time()
time.sleep(1)
merge_sort(a)
end=time.time()
print(a)
print("Counting Inversions:",count)
print(end-start,"seconds")