#HALLAR EN NUMERO DE PI USANDO MEDIANTE SUMAS SUCESIVAS.
#ENTRE MAS GRANDE EL NUMERO DE itera SE HARA MAS ITERACIONES
a = 1
j = 0.0
pi = 0.0
itera = 10000000
for i in range(itera):
    if a==1 or j == 4:
        pi = pi + (4/a)
        j = 2
    else: 
        pi = pi - (4/a)
        j = j + 2
    a+=2
    
print(pi)