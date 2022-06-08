dict = {
    'country':{
        'code':'UA',
        'name':'Україна',
        'doc':('Європа','45 млн')
    },
    'person':{
        'first':'Сковорода',
        'last':'Григорій',
        'address':('м. Київ','вул. Перемоги',7),
        'data':{'age':'53 роки','profession':'філософ','rank':'професор'}
    },
    'auto':{'model':'fiat'},
}
print(dict['country']['name'],dict['country']['doc'][0],dict['person']['first'],dict['person']['last'],dict['person']['data']['age'],dict['person']['data']['rank'],dict['auto']['model'])







































dict_ex = {
    "key1":{
        "fff1":"sss",
        "fff2":"sss",
        "fff3":["fff", "ssss"],
    },
    "key2":"value2",
    "key3":"value3",
    "key4":"value4"
}

#print(dict_ex['key1']['fff3'][1])
#print((dict_ex['key1']['fff3'][1]),(dict_ex['key3']))
