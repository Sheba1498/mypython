import json
with open("countries.json",encoding="utf-8") as f:
    data=json.load(f)




# print total number of country details
# print(len(data))

# print languages of ukrane
# ukr_lan=[country["languages"] for country in data if country["name"]=="Ukraine"]
# for lan in ukr_lan[0]:
    # print(lan["name"])



# print currency of china
# cur_china=[country["currencies"] for country in data if country["name"]=="China"]
# for cur in (cur_china[0]):
    # print(cur["name"])



# print currency of palestine
# cur_plstn=[country["currencies"] for country in data if country["name"].lower().startswith("palestine")]
# for cur in (cur_plstn[0]):
    # print(cur["name"])


# print population of india
# pop_ind=[country["population"] for country in data if country["name"]=="India"]
# print(pop_ind)



# print nigehbouring countries of australia
def get_country(country_name):
    out=[country for country in data if country["name"].lower().startswith(country_name)]
    return out

aus_dtls=get_country("australia")
aus_brdrs=aus_dtls[0].get("borders")
print(aus_brdrs)


ind_dtls=(get_country("india"))
ind_brdrs=ind_dtls[0].get("borders")
print(ind_brdrs)

brdr_cntrs=[country["name"] for country in data if country["alpha3Code"] in ind_brdrs]
print(brdr_cntrs)


#highest populated country
high_pop=max(data,key=lambda d:d["population"])
print(high_pop["name"])

#lowest populated country
low_pop=min(data,key=lambda d:d["population"])
print(low_pop["name"])