people = ['Andres','Maria', 'Juan', 'Samuel', 'Vanesa', 'Gabriel', 'Juan']

count = 0
for person in people:
    if person == 'Juan':
        count+=1

print('Juan se encuentra ', count , " veces")


count = 5
while count <= 10:
    print(count)
    count += 1


def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


for char in reverse('Mazda'):
    print(char)

