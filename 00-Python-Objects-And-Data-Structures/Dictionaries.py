my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict['key1'])

prices_lookup = {
    'apple': 2.99, 'grapes': 3.2, 'guavava': '2.5'
}

print(prices_lookup['apple'])
d = {'k1': 123, 'k2': [1, 2, 3], 'k3': {
    'insidekey': 100}, 'k4': {'alphabetkey': ['a', 'b', 'c']}}
print(d['k2'])
print(d['k3'])
print(d['k3']['insidekey'])
print(d['k4'])
print(d['k4']['alphabetkey'])
print(d['k4']['alphabetkey'][2])
print(d['k4']['alphabetkey'][2].upper())


d2 = {'k1':
      100, 'k2': 200}
d2['k1'] = 'new value'
print(d2)
print(d2.items())
print(d2.values())
print(d2.keys())
