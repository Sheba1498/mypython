master_word = "abbcceddffggt"
#chk_wrd = "egg"

master_word.split(" ")
char_lst=[]
for char in master_word:
    if char=="e":
        char_lst.append(char)
    elif char=="g":
        char_lst.append(char)
c_wrd=(" ".join(char_lst))
print(c_wrd)




# largest no
# num = [9, 39, 8, 78]
#
# print(num.sort())