#json -> javascript object notation
import json
with open("blogs.json")as f:
    data=json.load(f)
    print(data)
print(len(data))

#no of post by userid1
post_u1=[post for post in data if post["userId"]==1]
print(len(post_u1))



#total no of likes for postid6
like_pid6=[post["liked_by"]for post in data if post["postId"]==6]
print(len(like_pid6[0]))


#no of posts liked by userid2
liked_by2=[post for post in data if 2 in post["liked_by"]]
print(len(liked_by2))

