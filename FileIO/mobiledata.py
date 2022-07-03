mobiles=open("mobiles.txt")
all_mobiles=[]
for mob in mobiles:
    mobile=mob.rstrip("\n").split(",")
    all_mobiles.append(mobile)
costly_mob=max(all_mobiles,key=lambda mob:int(mob[2]))
print(costly_mob)