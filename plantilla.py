#Plantilla 
import math 

dat = []
max_lotes = 5  

procesos =  int(input('Indica el numero de procesos(N): '))

lot = procesos/max_lotes #Calcula la cantidad de lotes
lotes = math.ceil(lot)   #Redondea el numero de lotes

lot_pend = lotes-1       #Lotes pendientes 
cont = 0                 #Contador de procesos
registro = 0             #Contador de registros

while procesos > 0:      #Mientras haya procesos 
    nom = input('-Nombre de Programador: ')
    cont += 1 
    registro +=1
    if(cont == procesos):
        dat.append((nom))              #Ultimo registro incompleto -> Ej: 5 procesos completan 1.25 registros
        break                          #[(nom,id,op,TME),(nom)]
    id = int(input('ID: '))
    cont += 1
    registro +=1
    if (cont== procesos):
        dat.append((nom,id))           #Ultimo registro incompleto -> Ej: 6 procesos completan 1.5 registros
        break                          #[(nom,id,op,TME),(nom,id)]
    op = input('-Operacion a realizar: ')
    cont += 1
    registro +=1
    if (cont== procesos):
        dat.append((nom,id,op))        #Ultimo registro incompleto -> Ej: 7 procesos completan 1.75 registros
        break                          #[(nom,id,op,TME),(nom,id,op)]
    TME = int(input('Tiempo Maximo Estimado: '))
    cont += 1
    registro +=1
    if (cont== procesos):
        dat.append((nom,id,op,TME))    #Ultimo registro completo -> Ej: 8 procesos completan 2 registros 
        break                          #[(nom,id,op,TME),(nom,id,op,TME)]
    if registro == 4:
        dat.append((nom,id,op,TME))
        registro = 0                   #Se tiene un registro completo y comienza otro registro 


print(f'Mi lista es: {dat}')

