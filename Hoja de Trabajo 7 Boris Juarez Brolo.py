

while(1):

    
    

    eleccion1=input("Seleccione su inciso a visualizar 1 / 2 / 3 / 4 / 5 : '   ")
    
    if eleccion1 == '1':
        
        while (1):
            rectangulo = {
                "coordenada inicial": "0,0",
                "base": "0,0",
                "altura": "0,0",
                "color": "green",

            }

            for x, y in rectangulo.items():
                print(2*x, y)

        
    elif eleccion1 == '2':
        

        while (1):
            l1 = [1, 2, 3]
            l2 = [4, 5, 6]


            for q, a in zip(l1, l2):
                print('El par ordenado es {0},{1}.'.format(q, a))
                print('La multiplicación de ambos es :'+{0}*{1})
    

    elif eleccion1 == '3':
        
        while (1):
            entrada=input(str("Ingrese su string separado por comas:",))

            diccionario = {}

            for x in entrada:
                diccionario[x] = entrada[x].count
    

    elif eleccion1 == '4':
    
        while (1):
            palabras_prohibidas = {
                "1":"comer",
                "2":"perder",
                "3":"fallar",
            }

            texto=input(str("Ingrese su frase menor a 150 caracteres:"))

            for palabras_prohibidas in texto: 
                print("Las palabras prohibidas aparecen de la siguiente manera",palabras_prohibidas.count)
    

    elif eleccion1 == '5':
        
        import operator

        alumnos={'Pedro':{'Matematica':'99','Progra1':'70','Fisica':'70','Circuitos':'70'},
        'Martin':{'Matematica':'99','Progra1':'70','Fisica':'70','Circuitos':'70'},
        'Juan':{'Matematica':'99','Progra1':'70','Fisica':'70','Circuitos':'70'},
        'Carlos':{'Matematica':'99','Progra1':'70','Fisica':'70','Circuitos':'70'},
        'Arturo':{'Matematica':'99','Progra1':'70','Fisica':'70','Circuitos':'70'},
        'Jose':{'Matematica':'99','Progra1':'70','Fisica':'70','Circuitos':'70'},
        'Andres':{'Matematica':'99','Progra1':'70','Fisica':'70','Circuitos':'70'},
        'Sara':{'Matematica':'99','Progra1':'70','Fisica':'70','Circuitos':'70'},
        'Camilo':{'Matematica':'99','Progra1':'70','Fisica':'70','Circuitos':'70'},
        'Lucas':{'Matematica':'99','Progra1':'70','Fisica':'70','Circuitos':'70'},
        }

        alumnoporvisualizar=input(str('Ingrese el nombre del alumno que desea observar: '))

        print(alumnos[alumnoporvisualizar])
        temp={}
        for key, value in alumnos.items():
            temp[key]=sum(value)/float(len(value))
            print('La nota mas alta para',key,'es', max(alumnos[alumnoporvisualizar].iteritems(),key=operator.itemgetter(1))[0])

    else:
        print("Input Invalido")





        






