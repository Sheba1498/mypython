pattern="ABASDFGASDFASDASAS"
char_cnt={}
for char in pattern:
    if char in char_cnt:
        char_cnt[char]+=1
    else:
        char_cnt[char]=1
print(char_cnt)


print(char_cnt.items())
sr=sorted(char_cnt.items(),key=lambda i:i[1],reverse=True)
print(sr)
mx=max(sr,key=lambda i:i[1])
print(mx)
mn=min(sr,key=lambda i:i[1])
print(mn)



#1ST RECURSIVE
# pattern="ABSDFGSDFASDASAS"
# char_cnt={}
# for char in pattern:
#     if char in char_cnt:
#         print(char,"1st recursive element")
#         break
#     else:
#         char_cnt[char]=1



# 2nd RECURSIVE
# pattern="ABABBBSDFGSDFASDASAS"
# char_cnt={}
# rec_cnt=[]
# for char in pattern:
#     if char in char_cnt:
#         rec_cnt.append(char)
#     else:
#         char_cnt[char]=1
# print(rec_cnt[1])