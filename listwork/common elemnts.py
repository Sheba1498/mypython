arr1=[20,12,17,16,11,15]
arr2=[8,19,14,16,18,20]
p1=0
p2=0
arr1.sort()
arr2.sort()
while (p1<len(arr1) and p2<len(arr2)):
    if arr1[p1]==arr2[p2]:
        print(f"common {arr1[p1]}")
        p1+=1
        p2+=1
    elif arr1[p1]>arr2[p2]:
        p2+=1
    elif arr1[p1]<arr2[p2]:
        p1+=1#


