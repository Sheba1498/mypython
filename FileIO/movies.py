
movies=open("movies.txt")
movie=[m.rstrip("\n").split(",") for m in movies]
print(movie)

# number of moviews released in 2022
# num=0
# for mov in movie:
#     if mov[1]=="2022":
#         num+=1
# print(num)



# number malayalam movies
# num=0
# for mov in movie:
#     if mov[3]=="malayalam":
#         num+=1
# print(num)

# theater released movies
# thtr_movies=[mov for mov in movie if mov[-1]=="theater"]
# print(thtr_movies)


# list of movies whose rating > 5
high_ratingmvs=[mov for mov in movie if mov[2]>="4"]
print(high_ratingmvs)


# {2022:,4,2021:6,2020:2}
# 2021
