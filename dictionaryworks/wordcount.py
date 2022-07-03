text="kochu vipi kochu kochu vipi vipi vipi feba vinu vinu feba feba kochu kochu"
wrd_cnt={}
wrds=text.split(" ")
for w in wrds:#kochu
    if w in wrd_cnt:
        wrd_cnt[w]+=1
    else:
        wrd_cnt[w]=1
print(wrd_cnt)
