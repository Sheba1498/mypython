student={"name":"sheba","rollno":1112119,"cls":"MSc","main":"Physics","passout":2021}
# print(student.get("name"))
# print(student.get("rollno"))
# print(student.get("cls"))

if "faculty" in student:
    student["faculty"]="John jacob"
else:
    student["faculty"]="Twinkle"
# print(student)

if "mark" in student:
    student["mark"]=90
else:
    student["mark"]=76
print(student)

student["mark"]=student["mark"]+15 if student["mark"]>85 else student["mark"]-5
print(student)


if student["mark"]>85:
    student["mark"]+=15
else:
    student["mark"]-=5
# print(student)


###wordcount
text="hai hello hai hello bye bye"
wrds=text.split(" ")
wordcount={}
for w in wrds:
    if w in wordcount:
        wordcount[w]+=1
    else:
        wordcount[w]=1
# print(wordcount)


###pattern
#first recursive char
pattern="ABABACC"
char_count={}
for char in pattern:
    if char in char_count:
        # print("first recursive element", char)
        break
    else:
        char_count[char]=1


#second recursive char

pattern="ABABACC"
char_count={}
rec_char=[]
for char in pattern:
    if char in char_count:
        rec_char.append(char)
    else:
        char_count[char]=1
print(rec_char[1])


