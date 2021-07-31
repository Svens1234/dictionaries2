person = {
    'first name': 'Jack',
    'last name': 'Brown',
    'age': 43,
    'hobbies': ['football', 'singing', 'photo'],
    'children': {'son': 'Michael', 'daughter': 'Pamela'}
}

print(person['age'])
print(person['hobbies'])
hobbies = person['hobbies']
print(hobbies[2])
print(person['hobbies'][2])

person['car']='Mazda'
person['hobbies'][0] = 'basketball'
print(person)
print(person.keys())
print(person.values())
print(person.items())
