#binary search
lst=[10,12,20,15,16,14,11,13]
srch=80
flag=0
low=0
upp=len(lst)
lst.sort()#[10,11,12,13,14,15,16,20]
while(low<upp):#0<8
    mid=(low+upp)//2#(0+8)//2=4
    if lst[mid]==srch:#14!=15
        flag=1
        break
    elif(lst[mid]>srch):#14!>15
        upp=mid-1
    elif(lst[mid]<srch):#14<15
        low=mid+1
print("found" if flag >0 else "not found")



# lst=[10,12,14,16,18,20,22,24]
# flag=0
# element=14
# lst.sort()
# low=0
# upp=len(lst)-1
# while(low<=upp):
#     mid=(low+upp)//2
#     if element==lst[mid]:
#         flag=1
#         break
#     elif element>lst[mid]:
#         low= mid+1
#     elif element<lst[mid]:
#         upp=mid-1
# print("found" if flag>0 else "not found")