lst=[
    [10,11],
    [12,28],
    [14,40],
    [15,30]
]
# for sub_list in lst:
#     for num in sub_list:
#         if num>16:
#             print(num)

# print(lst)

# flatten_list=[]
# for sub_list in lst:
#     for num in sub_list:
#         flatten_list.append(num)
# print(flatten_list)
# print(max(flatten_list))
# print(min(flatten_list))
# print(sum(flatten_list))
# print(sorted(flatten_list))
# flatten_list.sort()
# print(flatten_list)

#list comprehension
# flatten_list=[num for sub_list in lst for num in sub_list]
# print(flatten_list)
# print(max(flatten_list))
# print(min(flatten_list))
# print(sum(flatten_list))
# print(sorted(flatten_list))


#list comprehension
# odd_num=[num for sub_list in lst for num in sub_list if num%2!=0]
# print(odd_num)


# evn_num=[num for sub_list in lst for num in sub_list if num%2==0]
# print(evn_num)


# mapped_list=[num+1 if num>15 else num-1 for sub_list in lst for num in sub_list]
# print(mapped_list)

