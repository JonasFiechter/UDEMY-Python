d1 = {'key1':'valor da chave'}

print(d1['key1'])

###############################

d1 = dict(key1='valor da chave', key2='valor da segunda chave')
d1['key2'] = 'new_key_value'

print(d1['key2'], d1['key1'], sep=' - ')

###############################

d1 = {
    'key1': 'value',
    'key2': 'other',
    'key4': 'alter'
}

print(d1.get('key2'))

###############################

d1 = {
    'key1': 'value',
    'key2': 'other',
    'key4': 'alter'
}

d1.update({'newkey': 'new_value'})

d1['new_key'] = 'any_new_value'

print(d1.get('key2'), d1.get(('newkey')))

del d1['key2']

print(d1)
print(d1.values())
print(d1.keys())
print('')

##################################

clients = {
    'client1': {
        'name': 'John',
        'last_name': 'Jackson',
        'age': 23,
    },
    'client2': {
        'name': 'Jack',
        'last_name': 'Boris',
        'age': 25,
    }
}

for k, v in clients.items():
    print(f'showing: {k}')
    for data_k, data_v in v.items():
        print(f'\t{data_k} = {data_v}')