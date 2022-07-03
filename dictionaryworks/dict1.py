student={"name":"sheba","rollno":1112119,"cls":"MSc","main":"Physics","passout":2021}
print(student["name"])
print(student["cls"])
print(student["rollno"])
print(student["main"])

print("faculty" in student)
student["faculty"]="John"
print(student)

print("clg" in student)
student["clg"]="Mar Ivanios"
print(student)

student["rollno"]=1119112
print(student)