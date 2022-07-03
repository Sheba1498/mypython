stdnts=open("students.txt")
all_stdnts=[stdnt.rstrip("\n") for stdnt in stdnts]


f_stdnts=open("failedstdnts.txt")
failed_students=[stdnt.rstrip("\n") for stdnt in f_stdnts]


passed=open("passedstudents.txt","w")


p_students=set(all_stdnts)-set(failed_students)
print(p_students)

for std in p_students:
    std+="\n"
    passed.write(std)
