# Funciones
# Retorna el valor absoluto del parametro que se pase
a= -12
print('El resultado de abs es: ' ,abs(a))

#Obtiene la conversacion a binario
b= 0
print('El resultado de bin es: ',bin (b))

#Retornar el caracter en formato unicode
c=62
print('El resultado de chr es: ',chr(c))

#Retornar el cociente y el resto de una division
d,e = 14,7
cociente,resto= divmod(d,e)
print('El cociente de la division es: ',cociente , ' y el resto, resto')


# Le pide al usuario que ingrese una string ( cadena de texto)
h= input('Ingrese su nombre: ')
print('El resultado de la funcion input es: ' ,h)

#Convierte una cadena de texto a un numero entero
i= '123'
print('El resultado de la funcion int es: ' ,int(i))

# Retorna la longitud del objeto tomado por parametro
j= 12,23,45,13,1231
print ('El resultado de la funcion len es: ' ,len(j))

#Retorna el mayor de loss parametros tomados
k,l= 12,43
print('El resultado de la funcion max es: ',max(k,l))

#Retorna el menor de los parametros tomados
m,n = 12,43
print('El resultado de la funcion min es: ',min(k,l))

#Obtiene la conversacion a octal
o= 124
print('El resultado de la funcion oct es: ',oct(o))


#Retorna el enetero unicode
p='<'
print('El resultado de la funcion ord es: ', ord (p))

#Retorna la potencia entre dos numeros
q,r = 2,3
print('El resultado de la funcion pow es: ',pow(q,r))

#Redondea a la cantidad de decimales que quieran
s=123.5632523
print('El resultado de la funcion round es; ', round(s,2))

#Convierte en cadena dde texto
t=2,4,1
print('El resultado de la funcion str es :', str(t))