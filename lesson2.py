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
    if transaction['add'] and "Хлеб" in transaction["products"]:
        total_amount += transaction["amount"]
print(total_amount)

# total_amount = 0 
# for z in transactions.values(): 
#      if z['add']: 
#          if 'Хлеб' in z['products']: 
#              total_amount += z['amount']
# print(total_amount)

# total_amount = 0
# for transaction in transactions.values():
#     if transaction['add']:
#         if "Хлеб" in transaction["products"]:
#            total_amount += transaction["amount"]
# print(total_amount)