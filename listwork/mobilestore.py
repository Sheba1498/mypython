mobiles=[
    [1000,"samsungA52","4g","AMOLED",27000,"samsung",12],
    [1001, "samsungA52s", "5g", "AMoLED", 32000, "samsung",20],
    [1002, "redminote10", "4g", "led", 17000, "redmi",50],
    [1003, "redminote11pro", "5g", "superAMOLED", 20000, "redmi",70],
    [1004, "samsungA72", "5g", "AMOLED", 27000, "samsung",1],
    [1005, "samsungA53", "5g", "AMOLED", 27000, "samsung",34],
    [1006, "samsungm52", "5g", "AMOLED", 27000, "samsung",7],
    [1007, "samsungm53", "5g", "AMOLED", 27000, "samsung",89],
    [1008, "samsungA22", "5g", "AMOLED", 27000, "samsung",0],
    [1009, "iphone13", "5g", "AMOLED", 97000, "apple",0],
    [1010, "oneplusnordce2", "5g", "AMOLED", 23000, "oneplus",67]

]

#q0 total no of mobiles
print(len(mobiles))

# q1 total number of out_of_stock mobiles
out_of_stock=[mob for mob in mobiles if mob[-1]==0]
print(out_of_stock)

# q2 total stock
stock_sum=sum([mob[-1] for mob in mobiles])
print(stock_sum)

# q3 print mobiles available in range 20k to 30k
phn_rng=[mob for mob in mobiles if mob[-3] in range(20000,30000)]
print(phn_rng)

# q4 print all 5g phone
phn_band=[mob for mob in mobiles if mob[2]=="5g"]
print(phn_band)

# q5 print samsung mobiles
phn_brand=[mob for mob in mobiles if mob[-2]=="samsung"]
print(phn_brand)

# q6 print costly mobile
costly_phn=max(mobiles,key=lambda mob:mob[4])
print(costly_phn)

mobiles.sort(reverse=True,key=lambda mob:mob[4])
print(mobiles[0])

# q7 print low cost mobiles
low_costphn=min(mobiles,key=lambda mob:mob[4])
print(low_costphn)

mobiles.sort(key=lambda mob:mob[4])
print(mobiles[0])

# q8 print all mobiles having stock >10
mob_stock=[mob for mob in mobiles if mob[-1]>10]
print(mob_stock)

# q9 count of mobiles having dispaly amoled
mob_display=[mob for mob in mobiles if mob[3]=="AMOLED"]
print(mob_display)

# q10 sort mobiles based on price oredr by desc
mobiles.sort(reverse=True,key=lambda mob:mob[4])
print(mobiles)

# q11 sort mobiles based on avl stock oredr by desc
mobiles.sort(reverse=True,key=lambda mob:mob[-1])
print(mobiles)

# q12 is there any mobile available at rs 10000 ?


# q13 list all mobiles having same pri

