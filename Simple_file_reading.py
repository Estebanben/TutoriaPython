import os


def ejercicio_1():
    #Ejercicio numero uno, leer y mostrar un archivo
    with open("ex1.acc", "r") as file: #abre el archivo con el nombre dado, se lee y se guarda en una variable
        for line in file: #itera sobre cada una de las lineas del archivo que fue leido
            print(line) #imprime la linea actual
            
def ejercicio_2():
    #Ejercicio numero dos, leer y mostrar un archivo (preguntando el nombre del archivo)
    file_name = input("Cual es el nombre del archivo que desea abrir: ") #pregunta el nombre del archivo a leer y lo guarda en esta variable llamada file_name
    with open(file_name,"r") as file: #abre el archivo con el nombre guardado en la variable de file_name, lee el archivo y guarda la informacion en la variable file
        for line in file: #itera sobre cada linea del archivo leido
            print(line) #imprime la linea actual

def ejercicio_3():
    #Ejercicio numero dos, leer y mostrar un archivo (preguntando el nombre del archivo)
    num_lines = 0
    file_name = input("Cual es el nombre del archivo que desea abrir: ") #pregunta el nombre del archivo a leer y lo guarda en esta variable llamada file_name
    with open(file_name,"r") as file: #abre el archivo con el nombre guardado en la variable de file_name, lee el archivo y guarda la informacion en la variable file
        for line in file: #itera sobre cada linea del archivo leido
            num_lines += 1 #suma 1 cada itera sobre una linea
        print(str(num_lines)) #imprime el total de lineas en el archivo
                   
def ejercicio_4_Unix():
        
    file_name = input("Cual es el nombre del archivo que desea abrir: ")#Se pregunta el nombre del archivo con el que se quiere trabjar 
    length = 0 #se declara la variable para el la cantidad de elementos de una columna
    mean = 0  #se declara la varibale para el promedio de una columna
    with open(file_name,"r") as file: #se abre el archivo especificado
        for line in file:#se itera sobre cada linea del archivo
            columns = line.split()#se divide la linea, para encontrar el numero de columnas
            
    num_cols = len(columns) #utilizando la funcion len se encuentran el numero de columnas en el archivo
    
    
    for i in range(num_cols): #se itera sobre este ciclo la cantidad de columnas encontradas
        command = "wsl cut -f" + str(i + 1) + " ex1.dat > ex1c" +str(i + 1)+ ".dat" #comando de UNIX que divide el archivo orignial en archivos de una sola columna
        os.system(command) #utilizamos la libreria os para hacer uso de estos comandos de UNIX (se puede hacer manual a traves de la terminal)
    
    for u in range(num_cols): #se itera sobre este ciclo la cantidad de columnas encontradas
        with open("ex1c"+str(u+1)+".dat" , "r") as column: #en cada iteracion se abre uno de los archivos creados anteriormente (archivos de una sola columna)
            for num in column: #se itera sobre cada valor en el archivo
                mean += float(num) #se suma el valor a la variable mean
                length +=1 #se suma uno a la variable de length
        mean = mean/length #al finalizar el ciclo se encuentra el promedio, dividiendo la suma de todos los valores por la cantidad de elementos
        print("El promedio de la columna numero " +str(u+1) + " es " + str(mean)) #se imprime el resultado  
        
        
def ejercicio_4s():
    file_name = input("Cual es el nombre del archivo que desea abrir: ")#Se pregunta el nombre del archivo con el que se quiere trabjar 
    length = 0 #se declara la variable para el la cantidad de elementos de una columna
    mean = 0  #se declara la varibale para el promedio de una columna
    
    with open(file_name , "r") as column: #en cada iteracion se abre uno de los archivos creados anteriormente (archivos de una sola columna)
        for num in column: #se itera sobre cada valor en el archivo
            mean += float(num) #se suma el valor a la variable mean
            length +=1 #se suma uno a la variable de length
    mean = mean/length #al finalizar el ciclo se encuentra el promedio, dividiendo la suma de todos los valores por la cantidad de elementos
    print("El promedio de la columna es " + str(mean)) #se imprime el resultado  
    
    
def ejercicio_5():
    file_name = input("Cual es el nombre del archivo que desea abrir: ") #se pide el nombre del archivo que se va a utilizar
    pos = 0 #varibale para la cantidad de numeros positivos
    neg = 0 #variable para la cantidad de numeros negativos
    with open(file_name,"r") as file: #se abre el archivo dado
        for line in file: #se itera sobre cada linea del archivo
            columns = line.split() #se divide la linea para encontrar el numero de columnas
            
    num_cols = len(columns) #utilizando la funcion len se encuentran el numero de columnas en el archivo
    
    
    for i in range(num_cols): #se itera sobre este ciclo la cantidad de columnas encontradas
        command = "wsl cut -f" + str(i + 1) + " ex1.dat > ex1c" +str(i + 1)+ ".dat" #comando de UNIX que divide el archivo orignial en archivos de una sola columna
        os.system(command) #utilizamos la libreria os para hacer uso de estos comandos de UNIX (se puede hacer manual a traves de la terminal)
    
    for u in range(num_cols): #se itera sobre este ciclo la cantidad de columnas encontradas
        with open("ex1c"+str(u+1)+".dat" , "r") as column: #en cada iteracion se abre uno de los archivos creados anteriormente (archivos de una sola columna)
            zero = 0 #variable para la cantidad de ceros en la columna
            for num in column: #se itera sobre cada numero en la columna
                
                if float(num) > 0: #si el numero es mayor a 0, se suma 1 a los positivos
                    pos +=1
                elif float(num) < 0: #si el numero es menor 0, se suma 1 a los negativos
                    neg += 1
                elif float(num) == float(0): #si el numero es igual a 0, se suma 1 a los ceros
                    zero += 1
            print("hay " + str(zero) + " ceros en la columna numero " + str(u+1)) #se imprime la cantidad de ceros encontrada en la columna
    print("hay " + str(pos) + " numeros positivos en el archivo") #se imprime la cantidad de numeros positivos encontrados  
    print("hay " + str(neg) + " numeros negativos en el archivo") #se imprime la cantidad de numeros negativos encontrados    
    
def ejercicio_5s():
    file_name = input("Cual es el nombre del archivo que desea abrir: ") #se pide el nombre del archivo que se va a utilizar
    pos = 0 #varibale para la cantidad de numeros positivos
    neg = 0 #variable para la cantidad de numeros negativos
    
    with open(file_name , "r") as column: #en cada iteracion se abre uno de los archivos creados anteriormente (archivos de una sola columna)
            zero = 0 #variable para la cantidad de ceros en la columna
            for num in column: #se itera sobre cada numero en la columna
                
                if float(num) > 0: #si el numero es mayor a 0, se suma 1 a los positivos
                    pos +=1
                elif float(num) < 0: #si el numero es menor 0, se suma 1 a los negativos
                    neg += 1
                elif float(num) == float(0): #si el numero es igual a 0, se suma 1 a los ceros
                    zero += 1
            print("hay " + str(zero) + " ceros en la columna") #se imprime la cantidad de ceros encontrada en la columna
    print("hay " + str(pos) + " numeros positivos en el archivo") #se imprime la cantidad de numeros positivos encontrados  
    print("hay " + str(neg) + " numeros negativos en el archivo") #se imprime la cantidad de numeros negativos encontrados    
    

def ejercicio_6():
    file_name = input("Cual es el nombre del archivo que desea abrir: ") #se pide el nombre del archivo que se va a utilizar
    with open(file_name,"r") as file: #se abre el archivo dado
        for line in file: #se itera sobre cada linea del archivo
            columns = line.split() #se divide la linea para encontrar el numero de columnas
            
    num_cols = len(columns) #utilizando la funcion len se encuentran el numero de columnas en el archivo
    
    
    for i in range(num_cols): #se itera sobre este ciclo la cantidad de columnas encontradas
        command = "wsl cut -f" + str(i + 1) + " ex1.dat > ex1c" +str(i + 1)+ ".dat" #comando de UNIX que divide el archivo orignial en archivos de una sola columna
        os.system(command) #utilizamos la libreria os para hacer uso de estos comandos de UNIX (se puede hacer manual a traves de la terminal)
    
    for u in range(num_cols): #se itera sobre este ciclo la cantidad de columnas encontradas
        with open("ex1c"+str(u+1)+".dat" , "r") as column: #en cada iteracion se abre uno de los archivos creados anteriormente (archivos de una sola columna)
            max = 0.0 #variable para el valor maximo de la columna
            for num in column: #se itera sobre cada numero en la columna
                
                if float(num) > float(max): #se compara el numero actual con la variable max, si el numero actual es mayor a max este se vuelve el nuevo maximo
                    max = float(num) #en caso de ser mayor, el numero actual es asignado a max
            print("el numero maximo en la columna numero " +str(u+1) + " es: " + str(max)) # se imprime el valor maximo de la columna
            
def ejercicio_6s():
    file_name = input("Cual es el nombre del archivo que desea abrir: ") #se pide el nombre del archivo que se va a utilizar
    
    with open(file_name , "r") as column: #en cada iteracion se abre uno de los archivos creados anteriormente (archivos de una sola columna)
            max = 0.0 #variable para el valor maximo de la columna
            for num in column: #se itera sobre cada numero en la columna
                
                if float(num) > float(max): #se compara el numero actual con la variable max, si el numero actual es mayor a max este se vuelve el nuevo maximo
                    max = float(num) #en caso de ser mayor, el numero actual es asignado a max
            print("el numero maximo en la columna es: " + str(max)) # se imprime el valor maximo de la columna
                    
    
def ejercicio_7():
    file_name = input("Cual es el nombre del archivo que desea abrir: ") #se pide el nombre del archivo que se va a utilizar
    with open(file_name,"r") as file: #se abre el archivo dado
        for line in file: #se itera sobre cada linea del archivo
            columns = line.split() #se divide la linea para encontrar el numero de columnas
            
    num_cols = len(columns) #utilizando la funcion len se encuentran el numero de columnas en el archivo
    
    
    for i in range(num_cols): #se itera sobre este ciclo la cantidad de columnas encontradas
        command = "wsl cut -f" + str(i + 1) + " ex1.dat > ex1c" +str(i + 1)+ ".dat" #comando de UNIX que divide el archivo orignial en archivos de una sola columna
        os.system(command) #utilizamos la libreria os para hacer uso de estos comandos de UNIX (se puede hacer manual a traves de la terminal)
    
    for u in range(num_cols): #se itera sobre este ciclo la cantidad de columnas encontradas
        with open("ex1c"+str(u+1)+".dat" , "r") as column: #en cada iteracion se abre uno de los archivos creados anteriormente (archivos de una sola columna)
            min = 0.0 #variable para el valor minimo de la columna
            for num in column: #se itera sobre cada numero en la columna
                
                if float(num) < float(min): #se compara el numero actual con la variable min, si el numero actual es menor a min este se vuelve el nuevo minimo
                    min = float(num) #en caso de ser menor, el numero actual es asignado a min
            print("el numero minimo en la columna numero " +str(u+1) + " es: " + str(min)) # se imprime el valor minimo de la columna

def ejercicio_7s():
    file_name = input("Cual es el nombre del archivo que desea abrir: ") #se pide el nombre del archivo que se va a utilizar

    with open(file_name , "r") as column: #en cada iteracion se abre uno de los archivos creados anteriormente (archivos de una sola columna)
            min = 1.0 #variable para el valor minimo de la columna
            for num in column: #se itera sobre cada numero en la columna
                
                if float(num) < float(min): #se compara el numero actual con la variable min, si el numero actual es menor a min este se vuelve el nuevo minimo
                    min = float(num) #en caso de ser menor, el numero actual es asignado a min
            print("el numero minimo en la columna es: " + str(min)) # se imprime el valor minimo de la columna

def ejercicio_8():
    mean = 0
    length = 0
    pos = 0
    neg = 0 
    sum = 0
    lines = 0 
    file_name = input("Cual es el nombre del archivo que desea abrir: ") #se pide el nombre del archivo que se va a utilizar
    with open(file_name,"r") as file: #se abre el archivo dado
        for line in file: #se itera sobre cada linea del archivo
            lines += 1
            columns = line.split() #se divide la linea para encontrar el numero de columnas
            
    num_cols = len(columns) #utilizando la funcion len se encuentran el numero de columnas en el archivo
    
    
    for i in range(num_cols): #se itera sobre este ciclo la cantidad de columnas encontradas
        command = "wsl cut -f" + str(i + 1) + " ex1.dat > ex1c" +str(i + 1)+ ".dat" #comando de UNIX que divide el archivo orignial en archivos de una sola columna
        os.system(command) #utilizamos la libreria os para hacer uso de estos comandos de UNIX (se puede hacer manual a traves de la terminal)
        
    for u in range(num_cols):
        with open("ex1c"+str(u+1)+".dat" , "r") as column: #en cada iteracion se abre uno de los archivos creados anteriormente (archivos de una sola columna)
            zero = 0 
            min = 0.0
            max = 0.0
            for num in column:
                if float(num) > float(max): #se compara el numero actual con la variable max, si el numero actual es mayor a max este se vuelve el nuevo maximo
                    max = float(num) #en caso de ser mayor, el numero actual es asignado a max
                
                if float(num) < float(min): #se compara el numero actual con la variable min, si el numero actual es menor a min este se vuelve el nuevo minimo
                    min = float(num) #en caso de ser menor, el numero actual es asignado a min
                    
                sum += float(num)
                mean += float(num) #se suma el valor a la variable mean
                length +=1 #se suma uno a la variable de length
                if float(num) > 0: #si el numero es mayor a 0, se suma 1 a los positivos
                    pos +=1
                elif float(num) < 0: #si el numero es menor 0, se suma 1 a los negativos
                    neg += 1
                elif float(num) == float(0): #si el numero es igual a 0, se suma 1 a los ceros
                    zero += 1
            
            print("el numero maximo en la columna numero " +str(u+1) + " es: " + str(max)) # se imprime el valor maximo de la columna
            print("el numero minimo en la columna numero " +str(u+1) + " es: " + str(min)) # se imprime el valor minimo de la columna
            print("hay " + str(zero) + " ceros en la columna numero " + str(u+1)) #se imprime la cantidad de ceros encontrada en la columna    
        mean = mean/length #al finalizar el ciclo se encuentra el promedio, dividiendo la suma de todos los valores por la cantidad de elementos
        print("El promedio de la columna numero " +str(u+1) + " es " + str(mean)) #se imprime el resultado  
    print("hay " + str(pos) + " numeros positivos en el archivo") #se imprime la cantidad de numeros positivos encontrados  
    print("hay " + str(neg) + " numeros negativos en el archivo") #se imprime la cantidad de numeros negativos encontrados    
    print("la suma de todos los numeros en el archivo es: " , str(sum)) #se imprime la suma total de todos los numeros en el archivo

def ejercicio_8s():
    mean = 0 #variable para el promedio de la columna
    length = 0 #variable para la cantidad de elementos de la columna
    pos = 0 #variable para la cantidad de numeros positivos en el archivo
    neg = 0 #variables para la cantidad de numeros negativos en el archivo
    sum = 0 #variable para la suma de todos los numeros en el archivo
    lines = 0 #variable para la cantidad de lineas en el archivo
    file_name = input("Cual es el nombre del archivo que desea abrir: ") #se pide el nombre del archivo que se va a utilizar
    
    with open(file_name , "r") as column: #en cada iteracion se abre uno de los archivos creados anteriormente (archivos de una sola columna)
            zero = 0 #variable para los ceros en la columna
            min = 1.0 #variable para el valor minimo de la columna
            max = 0.0 #variable para el valor maximo de la columna
            for num in column: #se itera sobre cada elemento en el archivo
                
                lines += 1 #se suma uno a la cantidad de lineas que tiene el archivo
                
                if float(num) > float(max): #se compara el numero actual con la variable max, si el numero actual es mayor a max este se vuelve el nuevo maximo
                    max = float(num) #en caso de ser mayor, el numero actual es asignado a max
                
                if float(num) < float(min): #se compara el numero actual con la variable min, si el numero actual es menor a min este se vuelve el nuevo minimo
                    min = float(num) #en caso de ser menor, el numero actual es asignado a min
                    
                sum += float(num)
                mean += float(num) #se suma el valor a la variable mean
                length +=1 #se suma uno a la variable de length
                if float(num) > 0: #si el numero es mayor a 0, se suma 1 a los positivos
                    pos +=1
                elif float(num) < 0: #si el numero es menor 0, se suma 1 a los negativos
                    neg += 1
                elif float(num) == float(0): #si el numero es igual a 0, se suma 1 a los ceros
                    zero += 1
            
    print("el numero maximo en la columna es: " + str(max)) # se imprime el valor maximo de la columna
    print("el numero minimo en la columna es: " + str(min)) # se imprime el valor minimo de la columna
    print("hay " + str(zero) + " ceros en la columna") #se imprime la cantidad de ceros encontrada en la columna    
    mean = mean/length #al finalizar el ciclo se encuentra el promedio, dividiendo la suma de todos los valores por la cantidad de elementos
    print("El promedio de la columna es: " + str(mean)) #se imprime el resultado  
    print("hay " + str(pos) + " numeros positivos en el archivo") #se imprime la cantidad de numeros positivos encontrados  
    print("hay " + str(neg) + " numeros negativos en el archivo") #se imprime la cantidad de numeros negativos encontrados    
    print("la suma de todos los numeros en el archivo es: " , str(sum)) #se imprime la suma total de todos los numeros en el archivo
 

def ejercicio_9():
    print("Piensa en un numero del 1 al 10.")
    low = 1 #limite inferior
    high = 10 #limite superior
    while True: #permite que el programa siga corriendo
        guess = (low + high) // 2 #el programa adivina el resultado de la division entera de la suma entre el limite superior y el inferior
        print("Tu numero es " , guess , "?")
        response = input("Estoy en lo correcto? Escribe 'yes', 'higher', o 'lower': ") #se le pide al usuario responder si el numero es correcto, mayor o menor
        if response == 'yes': #si el numero es adivinado se termina el programa
            print("Adiviné tu numero!")
            break
        elif response == 'higher': #si el numero es mayor se suma 1 al limite inferior
            low = guess + 1
        elif response == 'lower': #si el numero es menor se resta 1 al limite superior
            high = guess - 1
        else:
            print("respuesta invalida. Porfavor ingresa 'yes', 'higher', or 'lower'.") #si se da una respuesta invalida se le pide al usuario responder nuevamente


ejercicio_9()