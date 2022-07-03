# for i in range(1,10):
#     print(i)
#
# for i in range(100,90,-1):
#     print(i)

#break
# for i in range(0,10,2):
#     if i==8:
#         break
#     print(i)

#continue
# for i in range(0,20,3):
#     if i==9:
#         continue
#     print(i)

#primeornonprime
# num=14
# flag=0
# for i in range(2,num):#2
#     if num%i==0:#14%2=0
#         flag=1#1
#         break
# if flag==0:
#     print("prime")
# else:
#     print("not prime")

#HCF
# num1=15
# num2=35
# hcf=1
# for i in range(2,16):
#     if(num1%i==0 and num2%i==0):
#         print(i)

# num1=18
# num2=36
# hcf=1
# for i in range(2,(min(num1,num2)+1)):
#     if(num1%i==0 and num2%i==0):
#         hcf=i
# print(hcf)

#
# num1=15
# num2=30
# num3=60
# hcf=1
# if num1<num2 and num1<num3:
#     limit=num1
# elif num2<num1 and num2<num3:
#     limit=num2
# elif num3<num1 and num3<num2:
#     limit=num3
# for i in range(2,(limit+1)):
#     if num1%i==0 and num2%i==0 and num3%i==0:
#         hcf=i
# print(hcf)

#1234
#1234
#1234
#1234
# for row in range(1,5):
#     for col in range(1,5):
#         print(col,end="")
#     print()

#123
#123
#123
#123
# for row in range(1,5):
#     for col in range(1,4):
#         print(col,end="")
#     print()


#456
#456
# for row in range(4,6):
#     for col in range(4,7):
#         print(col,end="")
#     print()

#111
#222
#333
#444
# for row in range(1,5):
#     for col in range(1,4):
#         print(row,end=" ")
#     print()


#1
#1 2
#1 2 3
#1 2 3 4
# for row in range(1,5):
#     for col in range(1,(row+1)):
#         print(col,end=" ")
#     print()

#1234
#123
#12
#1

# for row in range(1,5):#row=1,2,3,4
#     for col in range(1,(6-row)):#col(1,2,3,4) (1,2,3) (1,2) (1)
#         print(col,end=" ")
#     print()

#1
#22
#333
#4444
# for row in range(1,5):
#     for col in range(1,(row+1)):
#         print(row,end=" ")
#     print()


#
# #
# # #
# # # #
# for row in range(1,5):
#     for col in range(1,(row+1)):
#         print("#",end=" ")
#     print()

#   #   #   #
#   #   #
#   #
#
# for row in range(1,5):
#     for col in range(5,row,-1):
#         print("#",end=" ")
#     print()
# full pyramid
# for row in range(1,7):
#     for space in range(1,(7-row)):
#         print(" ",end=" ")
#     for col in range(1,(row+1)):
#         print(" * ",end=" ")
#     print()
#hollow full pyramid
for row in range(1,5):
    for col in range(1,8):
        if (row==4 or row+col==5 or col-row==3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()