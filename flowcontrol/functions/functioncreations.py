#add_numbers
def add_numbers(n1,n2):
    return n1+n2
# print(add_numbers(13,27))
#sub_numbers
def sub_numbers(n1,n2):
    return n1-n2
# print(sub_numbers(99,108))
#smart_sub
def smart_sub(n1,n2):
    return n1-n2 if n1>n2 else n2-n1
# print(smart_sub(99,108))
#max_two
def max_two(n1,n2):
    return n1 if n1>n2 else n2
# print(max_two(100,200))
#num_chk
def num_chk(num):
    return "even" if num%2==0 else "odd"
# print(num_chk(13))
#cube

#startswith!!
# def startswith(name):
#     return name.startswith("s")
# name="harry"
# print(startswith("harry"))

# def validate_gmail(mail):
#     return mail.endswith("gmail.com")
# print(validate_gmail("sk14@gmail.com"))
# print(validate_gmail("sk14@yahoo.com"))
#HW
def prime_chk(num):
    for i in range(2,(num)):
       return False if(num%i==0) else True
print(prime_chk(12))
print(prime_chk(13))
#HW
#
def prime_range(low,upp):
    for num in range(low,(upp+1)):
        if prime_chk(num):
            print(num)
print(prime_range(2,40))            