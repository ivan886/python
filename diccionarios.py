person={
    'first_name':'jhnon',
    'last_name':'doe',
   'age':30
}



for key in person:
  print( key, ":", person[key])

for key, value in person.items():
    print(key, value)


person1 = dict(first_name='nestor',
                last_name='camargo',
                age=22)

print(person1)
print(person1['first_name'])


print(person1.keys())
print(person1.values())


#OPERACIONES
person1.update({'first_name':'Natalia', 'last_name':'Alba'})
print(person1)
print(person1.get('last_name'))
print(person1.pop('last_name'))
print(person1)
