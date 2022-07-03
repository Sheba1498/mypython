#print(dir(dict))




#age
person=[
    ["kochu",24],
    ["kunju",54],
    ["maya",50],
    ["feba",30]

]
print(sorted(person,key=lambda per:per[1]))
print(max(person,key=lambda per:per[1]))
print(min(person,key=lambda per:per[1]))


