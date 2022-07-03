lst=[10,14,2,14,14,20]
st=set(lst)
# print(st)
lst1=list(st)
# print(lst1)

st1={2,4,6,7,3,9}
st2={10,6,4,3,2,8}
union_st=st1.union(st2)
# print(union_st)



intersection_set=st2.intersection(st1)
# print(intersection_set)

diff_set=st1-(st2)
print(diff_set)

diff_st=st2.difference(st1)
# print(diff_st)

student=["kochu","nibin","iswu","cincy","anjali","ashok"]
pass_students=["kochu","iswu","nibin"]
st_student=set(student)
st_pass_students=set(pass_students)
fail_students=st_student.difference(st_pass_students)
# print(fail_students)
