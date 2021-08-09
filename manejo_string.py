

s ='Jennifer Margarita Guerrero'



print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.swapcase())

print(len(s))
print(s.replace('world','everyone'))
print(s.startswith('hello'))
print(s.find('r'))
print(s.isalpha())

print("substring")
#acceder a una posicion
print(s[0])
#segmentos de cadena
print(s[0:3])
print(s[3:10])
print(s[3:-1])

print(3 * " Juanito  ")

#recorrido
for x in "hola mundo ":
    print(x)


#las cadenas son inmutables
#pais = "colombia"
#pais[0] = "C"
#print(pais)

nombre =  "Marcos"
s = "hola me llamo "+ nombre + ', soy pianista'
print(s)

txt = "Hi, my name is Mary. I like zebras and xylophones."


def processString5(txt):
    transTable = txt.maketrans("aeiou", "AEIOU", "xyz")
    txt = txt.translate(transTable)
    print(txt)


processString5(txt)


# split

text = 'Python is a fun programming language'

# split the text from space
print(text.split(' '))