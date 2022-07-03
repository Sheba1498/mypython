# 1st recursive no
# lst=[7,10,13,10,14,28,14,35,14,27,14]
# dup_lst=[]
# for i in range(0,len(lst)):
#     for j in range((i+1),len(lst)):
#         if lst[i]==lst[j]:
#             dup_lst.append(lst[i])
# print(dup_lst)
# print(f"1st recursive element {dup_lst[0]} and 2nd recursive element {dup_lst[1]}")=[]



#print pair nos whose sum is 10->linear method
lst=[2,6,4,3,8,1,9,7,5]
sum=10
# for i in range(0,len(lst)):
#     for j in range ((i+1),len(lst)):
#         cur_sum=lst[i]+lst[j]
#         if cur_sum==sum:
#             print(f"pairs{lst[i]},{lst[j]}")
#             break


# algorithm
lst.sort()
low=0
upp=len(lst)-1
while(low<upp):
    cur_sum=lst[low]+lst[upp]
    if cur_sum==sum:
        print(f"pairs{lst[low]},{lst[upp]}")
        break
    elif cur_sum > sum:
        upp -= 1
    elif cur_sum < sum:
        low += 1