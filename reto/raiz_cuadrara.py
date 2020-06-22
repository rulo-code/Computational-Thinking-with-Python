
objetivo = int(input('Escribe un numero: \n'))
print(f'Escoge el algoritmo para hallar la raiz cuadrara de {objetivo} \n')
print('1 - Enumeración exhaustiva \n ')
print('2 - Aproximación decimal \n')
print('3 - Busqueda binaria \n')
algoritmo = int(input('Escribe el número correspondiente\n'))

def Enumeracion(objetivo):
  iteraciones = 0
  respuesta = 0
  while respuesta**2 < objetivo:
    respuesta += 1
    iteraciones += 1
  if respuesta **2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}\n encontrado en {iteraciones} iteraciones')
  else:
    print(f'{objetivo} no tiene una raiz cuadrada exacta')

def Aproximacion(objetivo):
  epsilon = 0.1
  paso = epsilon**2
  respuesta = 0.0
  iteraciones= 0

  while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(f'{abs(respuesta**2 - objetivo)}')
    respuesta += paso
    iteraciones += 1
  if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontró la raiz cuadrada de {objectivo}')
  else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}\n Encontrado en {iteraciones} iteraciones ')

def BusquedaBinaria(objetivo):
  epsilon = 0.1
  bajo = 0.0
  alto = max(1.0, objetivo)
  respuesta = (alto + bajo) / 2
  iteraciones = 0

  while abs(respuesta**2 - objetivo) >= epsilon:
    iteraciones +=1 
    print(respuesta)
    if respuesta**2 < objetivo:
      bajo = respuesta
    else:
      alto = respuesta
    respuesta = (alto + bajo )/2
  print(f'La raiz cuadrada de {objetivo} es {respuesta} \n Encontrado en {iteraciones} iteraciones')


if algoritmo == 1:
  Enumeracion(objetivo)
if algoritmo == 2:
  Aproximacion(objetivo)
if algoritmo == 3:
  BusquedaBinaria(objetivo)