# Estructura condicional
# Estructura

#if expresion logica:
#...
#else:
#..
'''
#Ejercicio 26
#Entradas
n1=int(input('Ingrese n1:'))
n2=int(input('Ingrese n2:'))
#Procesos
if n1 > n2 : #si n1 es mayor a n2
    #rama verdadera
    print('n1 y n2 son iguales')
elif n1 == n2: #ambos son iguales
    print('ambos son iguales')
else: #sino
    #rama falsa
    mayor= n2
    menor= n1
    print(menor,mayor)
'''
'''
#Ejercicio 27
#Entradas
a=int(input('Ingrese a:'))
b=int(input('Ingrese b:'))
c=int(input('Ingrese c:'))

#Procesos
suma= a+b+c
if suma >10:
   resultado=suma/2
else:
    resultado= suma**3
#Salidas
    print(resultado)
    
'''
'''
#Ejercicio 28
#Entradas
horasT= int(input('Ingrese la cantidad de horas: '))
turno= int(input('Ingrese su turno... 1-Diurno y 2-Nocturno '))
#Procesos
turnoA= 5234
turnoB= 8057.75
if turno == 1:
    cobro = horasT * turnoA
elif turno == 2:
    cobro= horasT * turnoB
else:
    print('Opcion no valida')
#Salidas
print('Su sueldo es: ',cobro)
'''
