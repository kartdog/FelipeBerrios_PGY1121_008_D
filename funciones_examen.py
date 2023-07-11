import numpy as np

asientos_concierto = np.zeros((10,10), int)
lista_rut = []
lista_total = []
lista_fila = []
lista_columna = []

lista_plat = []
lista_gold = []
lista_silver = []

total_asientos = 0
cant_platinum = 0
cant_gold = 0
cant_silver = 0
cant_total = 0

def val_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opcion: "))
            if opcion in (1,2,3,4,5):
                return opcion
            else:
                print("ERROR! elija una opcion válida.")
        except:
            print("ERROR! debe ingresar un número entero.")

def val_rut():
    while True:
        rut = input("Ingrese rut (sin guion/sin digito verificador): ")
        if rut.isnumeric and len(rut) == 8:
            return rut
        else:
            print("ERROR!")
            
def val_columna():
        while True:
            try:
                columna = int(input("Ingrese columna: "))
                if columna in (1,2,3,4,5,6,7,8,9,10):
                    lista_columna.append(columna)
                    return columna
                else:
                    print("ERROR! elija una opcion válida.")
            except:
                print("ERROR! debe ingresar un número entero.")
            
def val_fila():
        while True:
            try:
                fila = int(input("Ingrese fila: "))
                if fila in (1,2,3,4,5,6,7,8,9,10):
                    lista_fila.append(fila)
                    return fila
                else:
                    print("ERROR! elija una opcion válida.")
            except:
                print("ERROR! debe ingresar un número entero.")

def val_opcion01():
    
    total_asientos = 0
    cant_platinum = 0
    cant_gold = 0
    cant_silver = 0
    
    while True:
        try:
            cant_asientos = int(input("Cuantos asientos desea comprar: "))
            if cant_asientos in (1,2,3):
                break
            else:
                print("ERROR! elija una cantidad válida.")
        except:
            print("ERROR! ingrese un número entero.")
            
    rut = val_rut()
    for x in range(cant_asientos):
        lista_rut.append(rut)
           
    print("FILA")
    print("|")
    print("V")
    for x in range(10):
        print(x + 1, "", end = "")
        for y in range(10):
            print(asientos_concierto[x][y], end = "")
        print("")
    print("  12345678910 <- COLUMNA")
         
    for x in range(cant_asientos):
        while True:
            print("COMPRA ENTRADAS: ")
            fila = val_fila()
            if fila in (1,2):
                cant_platinum += 1
                lista_plat.append(cant_platinum)
            elif fila in (3,4,5):
                cant_gold += 1
                lista_gold.append(cant_gold)
            elif fila in (6,7,8,9,10):
                cant_silver += 1
                lista_silver.append(cant_silver)
                
            columna = val_columna()
                
            if asientos_concierto[fila-1][columna-1] == 1:
                print("Asiento ocupado")
            elif asientos_concierto[fila-1][columna-1] == 0:
                asientos_concierto[fila-1][columna-1] = 1
                break
    
    print("Entrada comprada exítosamente.")
                
    cant_total = cant_platinum + cant_gold + cant_silver
                    
def val_opcion02():
    print(">> VISTA DE ASIENTOS")
    print(">> '1' SEÑALA ASIENTO OCUPADO")
    
    print("FILA")
    print("|")
    print("V")
    for x in range(10):
        print(x + 1, "", end = "")
        for y in range(10):
            print(asientos_concierto[x][y], end = "")
        print("")
    print("  12345678910 <- COLUMNA")
    
def val_opcion03():
    lista_rut.sort()
    len_rut = len(lista_rut)
    for x in range(len_rut):
        print(lista_rut[x], sep = " ")
    print()
    
def val_opcion04():
    
    cant_silver = 0
    cant_gold = 0
    cant_plat = 0
    
    len_gold = len(lista_gold)
    len_silver = len(lista_silver)
    len_plat = len(lista_plat)
    
    for x in range(len_plat):
        cant_plat += lista_plat[x] 
        
    for x in range(len_gold):
        cant_gold += lista_gold[x] 
        
    for x in range(len_silver):
        cant_silver += lista_silver[x] 
        
    print("--------------------------------------------")
    print("TIPO ENTRADA |CANTIDAD |TOTAL")
    print(f"PLATINUM     |{cant_plat}        |{cant_plat * 120000}")
    print(f"GOLD         |{cant_gold}        |{cant_gold * 80000}")
    print(f"SILVER       |{cant_silver}        |{cant_silver * 50000}")
    print(f"TOTAL        |{cant_silver + cant_gold + cant_plat}        |{cant_plat * 120000 + cant_gold * 80000 + cant_silver * 50000}")
    print("--------------------------------------------")