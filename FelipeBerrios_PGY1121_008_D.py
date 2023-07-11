
import funciones_examen as fn

while True:
    print("MENÚ CREATIVOS")
    print("1. Comprar entradas")
    print("2. Mostrar ubicaciones")
    print("3. Ver listado de asistentes")
    print("4. Mostrar ganancias totales")
    print("5. Salir")
    
    opcion = fn.val_opcion()
    
    if opcion == 1:
        asientos = fn.val_opcion01()
    elif opcion == 2:
        mostrar = fn.val_opcion02()
    elif opcion == 3:
        listado = fn.val_opcion03()
    elif opcion == 4:
        ganancia = fn.val_opcion04()
    else:
        print("Nos vemos!, soy Felipe Berríos y es 11/07/23.")
        break