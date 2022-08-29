"""
    Activity:

6) Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

Todos los números del 0 al 10 [0, 1, 2, ..., 10]
Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

"""
# Solution 1
print("""
List 1
All numbers from 0 to 10 [0, 1, 2, ..., 10]""")
list_1 = []
for n in range(11):
    list_1.append(n)
print(list_1)

print("""
List 2
All numbers from -10 to 0 [-10, -9, -8, ..., 0]""")
list_2 = []
for n in range(11):
    list_2.append(n-10)
print(list_2)

print("""
List 3
All even numbers from 0 to 20 [0, 2, 4, ..., 20]""")
list_3 = []
for n in range(0, 21, 2):
    list_3.append(n)
print(list_3)

print("""
List 4
All odd numbers from -20 to 0 [-19, -17, -15, ..., -1]""")
list_4 = []
for n in range(-19, 0, 2):
    list_4.append(n)
print(list_4)

print("""
List 5
All multiples of 5 from 0 to 50 [0, 5, 10, ..., 50]""")
list_5 = []
for n in range(0, 51, 5):
    list_5.append(n)
print(list_5)

# Solution 2

print("""
List 1
All numbers from 0 to 10 [0, 1, 2, ..., 10]""")
list_1 = list(range(0, 11))
print(list_1)

print("""
List 2
All numbers from -10 to 0 [-10, -9, -8, ..., 0]""")
list_2 = list(range(-10, 0))
print(list_2)

print("""
List 3
All even numbers from 0 to 20 [0, 2, 4, ..., 20]""")
list_3 = list(range(0, 21, 2))
print(list_3)

print("""
List 4
All odd numbers from -20 to 0 [-19, -17, -15, ..., -1]""")
list_4 = list(range(-19, 0, 2))
print(list_4)

print("""
List 5
All multiples of 5 from 0 to 50 [0, 5, 10, ..., 50]""")
list_5 = list(range(0, 51, 5))
print(list_5)