weather=[
    {"district": "tvm", "temp":30},
    {"district": "ktm","temp":28 },
    {"district": "apy","temp":27},
    {"district": "idk","temp":18 },
    {"district": "ekm","temp":31 },
    {"district": "pta","temp":21},
    {"district": "tsr","temp":24},
    {"district": "kzd","temp":29},
    {"district": "pkd","temp":34},
    {"district": "mpm","temp":31},
    {"district": "tvm", "temp": 31},
    {"district": "ktm", "temp": 29},
    {"district": "apy", "temp": 26},
    {"district": "idk", "temp": 20},
    {"district": "ekm", "temp": 30},
    {"district": "pta", "temp": 22},
    {"district": "tsr", "temp": 27},
    {"district": "kzd", "temp": 28},
    {"district": "pkd", "temp": 30},
    {"district": "mpm", "temp": 29},

]
out={}
for data in weather:
    d_name=data["district"]
    c_temp=data["temp"]
    if d_name in out:
        old_temp=out[d_name]
        if old_temp<c_temp:
            out[d_name]=c_temp
    else:
        out[d_name]=c_temp
# print(out)


print(out.items())
print(sorted(out.items(),key=lambda i:i[1],reverse=True))
print(max(out.items(),key=lambda i:i[1]))
print(min(out.items(),key=lambda i:i[1]))















