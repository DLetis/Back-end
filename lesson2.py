# s='a'
# t='b'
# t=s

# s=['a','b','c']
# t=s
# s[0]='x'

#####

# list = [1,3,5,7,9]
# for z in list:
#     if z == 7:
#         print("Yes",z)
#     else:
#         print('no',z)


# list=['Yura','Lyuda','Mike','Rose']
# for a in list:
#     while a == 'Lyuda':
#         print('Yura+Luda')
#     else:
#         print('ups')    

# total = [1,3,5,7,9]
# total_sum = 0
# for z in total:
#     print(total_sum)

# a=0
# while a<10:
#     print(a)
#     a+=1

transactions = {
   '1':{
        "add":True,
        "amount":69,
        "products":{
            "Хлеб",
            "Масло",
            "Сок",
        }
    },
    '2':{
        "add":True,
        "amount":30,
        "products":{
            "Сок",
        }
    },
    '3':{
        "add":True,
        "amount":94,
        "products":{
            "Мука",
            "Хлеб",
            "Масло",
        }
    },
    '4':{
        "add":False,
        "amount":24,
        "products":{
            "Конфеты",
            "Хлеб",
        }
    }, 
}
total_amount = 0
for transaction in transactions.values():
    # if transaction['add']:
    #     if "Хлеб" in transaction["products"]:
    #        total_amount += transaction["amount"]
    if transaction['add'] and "Хлеб" in transaction["products"]:
        total_amount += transaction["amount"]
print(total_amount)