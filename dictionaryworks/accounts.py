accounts = [
    {
        "acno": 1000, "ac_type": "savings", "balance": 5000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1001, "ac_type": "savings", "balance": 6000, "transactions": [
        {"to": 1000, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1002, "ac_type": "current", "balance": 8000, "transactions": [
        {"to": 1001, "amount": 700, "note": "ebill", "method": "g-pay"},
        {"to": 1000, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 800, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1003, "ac_type": "credit", "balance": 15000, "transactions": [
        {"to": 1001, "amount": 1500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 800, "note": "geto", "method": "neft"},
        {"to": 1000, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1004, "ac_type": "savings", "balance": 50000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },

]




#q1  print details of 1002
for account in accounts:
#     if account["acno"]==1002:
#         print(account)

#or
# ac_1002=[account for account in accounts if account["acno"]==1002]
# print(ac_1002)


#q2 print savings type account details
# for ac in accounts:
#     if ac["ac_type"]=="savings":
#         print(ac)

#or
# sav_ac=[ac for ac in accounts if ac["ac_type"]=="savings"]
# print(sav_ac)

#q3 sort account based on balance on descending order
# accounts.sort(key=lambda ac:ac["balance"],reverse=True)
# print(accounts)

#q4 print all phone pay transactions
# for ac in accounts:
#     for tr in ac["transactions"]:
#         if tr["method"]=="phone-pay":
#             print(tr)

#or
# phn_pay=[tr for ac in accounts for tr in ac["transactions"] if tr["method"]=="phone-pay" ]
# print(phn_pay)

#q5 prit all transactions where transaction amount > 500
# for ac in accounts:
#     for tr in ac["transactions"]:
#         if tr["amount"]>500:
#             print(tr)
#or
# trn=[tr for ac in accounts for tr in ac["transactions"] if tr["amount"]>500]
# print(trn)


#q6 crredit transactions of 1002
# for ac in accounts:
#     for tr in ac["transactions"]:
#         if tr["to"]==1002:
#             print(tr)

#or
# trn=[tr for ac in accounts for tr in ac["transactions"] if tr["to"]==1002]
# print(trn)


#q7 aggregate transactions based on payment mode


















