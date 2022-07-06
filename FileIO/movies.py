m=open("movies.txt")
movies=[movi.rstrip("\n").split(",") for movi in m ]
print(movies)


# number of movies released in 2022
mov_22=len([movie for movie in movies if movie[1]=="2022" ])
print(mov_22)


# number malayalam movies
mala_mov=[movie for movie in movies if movie[-2]=="malayalam"]
print(len(mala_mov))


# theater released movies
thtr_mov=[movie for movie in movies if movie[-1]=="theater"]
print(thtr_mov)


# list of movies whose rating > 4
rtd_movie=[movie for movie in movies if movie[2]>="4"]
print(rtd_movie)



# {2022:,4,2021:6,2020:2}
movie_yr={}
for movie in movies:
    year=movie[1]
    if year in movie_yr:
        movie_yr[year]+=1
    else:
        movie_yr[year]=1
print(movie_yr)


#year in which largset no of movies released
yr_highmv=max(movie_yr.items(),key=lambda i:i[1])
print(yr_highmv)