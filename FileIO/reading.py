f=open("abc.txt","w")
# lines=[line.rstrip("\n") for line in f]
# print(lines)


# company_name="tcs"
# f.write(company_name)

lst=["mango","apple","orange"]
for fruit in lst:
    fruit+="\n"
    f.write(fruit)

