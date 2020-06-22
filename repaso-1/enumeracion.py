objective = int(input('write a number: \n'))

response = 0

while response**2 < objective:
  print(response)
  response += 1
if response**2 == objective:
  print(f'La raiz cuadrada de {objective} es {response}')
else:
  print(f'{objective} no tiene una raiz cuadrado exacta')