
# STRING: us_admin, contrasenia_admin, texto_nove1, texto_nove2, texto_nove3, fecha_ini_nove1, fecha_ini_nove2, fecha_ini_nove3, fecha_fin_nove1, fecha_fin_nove2, fecha_fin_nove3, fecha, fecha_aux, codigo_pais, descripcion_aereo, nombre_aereo, codigo_mayor, codigo_menor, usuario, contrasenia
# INT: intentos, codigo_nove1, codigo_nove2, codigo_nove3, opc, nuevo_codigo, opc_novedad, opc_aspecto, mayor, menor, contador_arg, contador_bra, contador_chi, opc_input, codigo_IATA
# BOOL: fecha_valida
from colorama import Fore, Style, Back, init
import random
import pwinput
import os
from datetime import datetime
import getpass 
import os.path
import pickle


#------------------------------------------------PROCEDIMIENTOS Y FUNCIONES GENERALES------------------------------------------------------------------
init(autoreset=True) 

def calcular_tamanio_registro(tamanio_arfi,arlo):
    if tamanio_arfi != 0:
        arlo.seek(0,0)
        registro = pickle.load(arlo) 
        len_registro = arlo.tell()
        return len_registro
    else:
        return -1

def buscar_ultimo_registro(arfi, arlo):
    len_archivo  = os.path.getsize(arfi)
    len_registro  = calcular_tamanio_registro(len_archivo,arlo)
    if len_registro != -1:
        cant_registros = len_archivo // len_registro #al ser registros de tamanio fijo, no es necesario verificar que no sea cero para no dividir por 0. Si fuese 0 entonces todo el documento tendria registros vacios
        return cant_registros-1
        
    else:
        return -1

def busqueda_secuencial_registro(arfi, arlo, valor, campo):
    arlo.seek(0,0)
    cant_registros = buscar_ultimo_registro(arfi, arlo)
    if cant_registros != -1:
        arlo.seek(0,0)
        i = 1
        registro = pickle.load(arlo)
        valor_campo = getattr(registro, campo)
        while valor_campo!= valor and i < cant_registros:
            i = i+1
            registro = pickle.load(arlo)
            valor_campo = getattr(registro, campo)
        if valor_campo == valor:
            return i-1
        else:
            return -1
    else:
        return -1
        
        
    

def validar_entero():
    opc_input = input("\nSeleccione una opción valida: ")
    if opc_input.isdigit():
        return(int(opc_input))
    else:
        return -1    

def cambiar_color(): 
    print(Fore.BLUE )

def en_construccion():
     input(Back.GREEN + Fore.BLUE + " En construccion. Presione enter para continuar:" + Style.RESET_ALL)#back asigna color fondo, fore color letra, style reset resea el estilo despues de ejecutar
     os.system('cls')

def volver():
    input("Regresando al menu anterior. Presione enter para continuar")
    os.system('cls')
    
""" def add_item(arreglo, valores_fila, posicion): #funcion general para agregar los valores de una fila a toda una fila de cualquier arreglo
    for i in range(len(valores_fila)): #[0-1-2]
        arreglo[posicion][i] = valores_fila[i] """ 
        
def pedir_fecha_valida():
    fecha_aux = input("Ingrese la fecha en formato dd/mm/aaaa: ")
    while not validar_fecha(fecha_aux):
        print("Fecha invalida. Intentelo nuevamente")
        fecha_aux = input("Ingrese la fecha en formato dd/mm/aaaa: ")
    return fecha_aux

def validar_fecha(fecha):
    try:
        datetime.strptime(fecha,"%d/%m/%Y")#transforma string a formato fecha, este dentro de try porque si falla corta ejecucion codigo
        fecha_valida = True
    except:
        fecha_valida = False
    return fecha_valida

def validar_entero():
    opc_input = input("\nSeleccione una opción valida: ")
    if opc_input.isdigit():
        return(int(opc_input))
    else:
        return -1

def ver_arreglo_limitado_pr(arreglo, texto_principal, titulos, condicion_hasta, pos_evaluar, mostrar_pos_y_modo, longitud_columnas):
    print(f"\n📑 {texto_principal} 📑\n")
    longitud= int(longitud_columnas)
    columnas = len(titulos)
    filas = len(arreglo)
    pos= int(pos_evaluar)
    print("-" * int(longitud*(columnas-1)))
    print()

    if mostrar_pos_y_modo[0]: #si mostramos la posicion
        print(f"{'N°':<4}", end=" ")
    for i in range(columnas):
        print(f"{titulos[i]:<{longitud}}", end=" ")
    print()
    i = 0
    #en la parte de modo, false signifca mostrar base 0, true significa mostrar base 1 (user friendly)
    if mostrar_pos_y_modo[0] and not mostrar_pos_y_modo[1]: #ej: [True, false] 1=true 0=false
        #si paso 1 en modo (segunda posicion) entonces estoy mostrando con base 1. Si paso 0 estoy mostrando con base 0
        #mostrar_pos_y_modo es un arreglo de booleanos. La primera posicion indica si queremos o no mostrar la posicion (nro de fila)
        #si mostramos posicion y el modo es false, entonces lo niego y entra aca. 
        while i < len(arreglo) and arreglo[i][pos] != condicion_hasta: #evalua que la posicion que indicamos a evaluar sea distinta a la condicion hasta
            print(f"{i :<4}", end=" ")
            for j in range(columnas):
                print(f"{arreglo[i][j]:<{longitud}}", end=" ")
            print()
            i += 1
    elif mostrar_pos_y_modo[0] and mostrar_pos_y_modo[1]:
        #si mostramos posicion y el modo es true, mostramos la posicion en base 1, por eso i+1
        while i < len(arreglo) and arreglo[i][pos] != condicion_hasta:
            print(f"{i+1 :<4}", end=" ")
            for j in range(columnas):
                print(f"{arreglo[i][j]:<{longitud}}", end=" ")
            print()
            i += 1
    else:
        #mostrar pos va a ser falso entonces no muestro i
        while i < filas and arreglo[i][pos] != condicion_hasta:
            for j in range(columnas):
                print(f"{arreglo[i][j]:<{longitud}}", end=" ")
            print()
            i += 1
    print()


def ver_arreglo_limitado_func(arreglo, texto_principal, titulos, condicion_hasta, pos_evaluar, mostrar_pos_y_modo, longitud_columnas):
    #hace lo mismo que el procedmiento con el mismo nombre pero ademas devuelve la ultima posicion del arreglo
    print(f"\n📑 {texto_principal} 📑\n")
    longitud= int(longitud_columnas)
    columnas = len(titulos)
    filas = len(arreglo)
    pos= int(pos_evaluar)
    print("-" * int(longitud*(columnas-1)))
    print()

    if mostrar_pos_y_modo[0]:
        print(f"{'N°':<4}", end=" ")
    for i in range(columnas):
        print(f"{titulos[i]:<{longitud}}", end=" ")
    print()
    i = 0
    if mostrar_pos_y_modo[0] and not mostrar_pos_y_modo[1]:
        while i < len(arreglo) and arreglo[i][pos] != condicion_hasta:
            print(f"{i :<4}", end=" ")
            for j in range(columnas):
                print(f"{arreglo[i][j]:<{longitud}}", end=" ")
            print()
            i += 1
    elif mostrar_pos_y_modo[0] and mostrar_pos_y_modo[1]:
        while i < len(arreglo) and arreglo[i][pos] != condicion_hasta:
            print(f"{i+1 :<4}", end=" ")
            for j in range(columnas):
                print(f"{arreglo[i][j]:<{longitud}}", end=" ")
            print()
            i += 1
    else:
        while i < filas and arreglo[i][pos] != condicion_hasta:
            for j in range(columnas):
                print(f"{arreglo[i][j]:<{longitud}}", end=" ")
            print()
            i += 1
    
    print()
    return i

def ver_arreglo_limitado_unidimensional(arreglo, texto_principal, titulos, condicion_hasta, mostrar_pos_y_modo, longitud_columnas):
    print(f"\n📑 {texto_principal} 📑\n")
    longitud= int(longitud_columnas)
    columnas = len(titulos)
    filas = len(arreglo)
    
    print("-" * int(longitud*(columnas)))
    print()

    if mostrar_pos_y_modo[0]:
        print(f"{'N°':<4}", end=" ")
    for i in range(columnas):
        print(f"{titulos[i]:<{longitud}}", end=" ")
    print()
    i = 0
    if mostrar_pos_y_modo[0] and not mostrar_pos_y_modo[1]:
        while i < len(arreglo) and arreglo[i]!= condicion_hasta:
            print(f"{i :<4}", end=" ")
            print(f"{arreglo[i]:<{longitud}}", end=" ")
            print()
            i += 1
    elif mostrar_pos_y_modo[0] and mostrar_pos_y_modo[1]:
        while i < len(arreglo) and arreglo[i]!= condicion_hasta:
            print(f"{i+1 :<4}", end=" ")
            print(f"{arreglo[i]:<{longitud}}", end=" ")
            print()
            i += 1
    else:
        while i < filas and arreglo[i]!= condicion_hasta:
            print(f"{arreglo[i]:<{longitud}}", end=" ")
            print()
            i += 1
    
    print()

def ordenar_burbuja_desc(arreglo, columna_orden, cant_columnas):
    filas = len(arreglo)

    fila_temp = [""] * cant_columnas
    i = 0
    while i < filas - 1:
        j = i + 1
        while j < filas:
            if arreglo[j][columna_orden] > arreglo[i][columna_orden]:
                #es descendente porque cambia si en la posicion j (que esta despues) es mayor a lo que esta en la posicion i. la mayor arriba
                k = 0
                while k < cant_columnas:
                    fila_temp[k] = arreglo[i][k]
                    k += 1
                k = 0
                while k < cant_columnas:
                    arreglo[i][k] = arreglo[j][k]
                    k += 1
                k = 0
                while k < cant_columnas:
                    arreglo[j][k] = fila_temp[k]
                    k += 1
            j += 1
        i += 1

def busqueda_secuencial (arreglo, elemento_buscado, columna):
    cant_filas = len(arreglo)
    i=0
    while i<cant_filas-1 and arreglo[i][columna]!=elemento_buscado:
        i=i+1
    if arreglo[i][columna]==elemento_buscado:
        return i
    else:
        return-1
    
def obtener_pos_menor(arreglo): #evalua en que posicion esta el menor
    pos_menor = 0
    for i in range(1, len(arreglo)):
        if arreglo[i] < arreglo[pos_menor]:
            pos_menor = i
    return pos_menor

def obtener_pos_mayor(arreglo): #evalua en que posicion esta el mayor
    pos_mayor = 0
    for i in range(1, len(arreglo)):
        if arreglo[i] > arreglo[pos_mayor]:
            pos_mayor = i
    return pos_mayor


#----------------------------------------------------------------------MENU ADMIN---------------------------------------------

def mostrar_menu_report():
    print("╔═════════════════════════════════════╗")
    print("║       📊 MENÚ DE REPORTES 📊        ║")
    print("╚═════════════════════════════════════╝\n")
    print("1) Reporte de Ventas (Confirmadas) 💰")
    print("2) Reporte de Vuelos ✈️")
    print("3) Reporte de Usuarios 👥")
    print("4) Volver 🔙")

def menu_report ():
    opc = -1
    while opc != 4:
        mostrar_menu_report()
        opc = validar_entero()
        os.system('cls')
        while opc <1 or opc>4:
            print("⚠️   Opción no válida. Inténtelo nuevamente.\n")
            mostrar_menu_report()
            opc = validar_entero()
            os.system('cls')
        match opc:
            case 1:
                en_construccion()
            case 2:
                en_construccion()
            case 3:
                en_construccion()
            case 4:
                volver()

""" def ver_novedades(novedades):
    print("╔═══════════════════════════════════════╗")
    print("║    📑  NOVEDADES DISPONIBLES  📑      ║")
    print("╚═══════════════════════════════════════╝\n")
    
    print()
    print(f"{'N°':<4} {'Descripcion':<100} {'Desde':<12} {'Hasta':<12}")
    print("-" * 130)

    i = 0
    while i < len(novedades) and novedades[i][0] != "":
        descripcion = novedades[i][0]
        desde = novedades[i][1]
        hasta = novedades[i][2]

        print(f"{i+1:<4} {descripcion:<100} {desde:<12} {hasta:<12}")
        i += 1
    print("-" * 130)
    print()
    return i """


""" def validar_codigo(): #DE LA NOVEDAD
    nuevo_codigo = -1
    while nuevo_codigo <0:
        nuevo_codigo = input("Ingrese el nuevo codigo (DEBE SER ENTERO POSITIVO, 0 PARA SALIR)\n")
        if nuevo_codigo.isdigit():
            nuevo_codigo = int(nuevo_codigo)
        else:
            nuevo_codigo = -1
            print("El codigo debe ser un numero entero positivo")
    os.system('cls')
    return nuevo_codigo """

def mostrar_menu_editar_nov():
    print("╔══════════════════════════════════════╗")
    print("║   ✏️ EDITAR ASPECTOS DE LA NOVEDAD ✏️  ║")
    print("╚══════════════════════════════════════╝\n")
    print("1) Descripción 📝")
    print("2) Fecha de Inicio 📅")
    print("3) Fecha de Finalización 📅")
    print("4) Volver 🔙")

def editar_nov():
    global novedades
    ultima_novedad = ver_arreglo_limitado_func(novedades, "NOVEDADES DISPONIBLES", ["descripcion", "fecha inicio", "fecha fin"], " ", 0, [True,True], 50)
    print("Ingrese la novedad que desea editar (0 para salir)")
    opc_novedad = validar_entero()-1
    while opc_novedad !=-1:
        while opc_novedad != -1 and opc_novedad >ultima_novedad: 
            print("⚠️   Opción no válida. Inténtelo nuevamente (0 para salir)")
            opc_novedad = validar_entero()-1
            
        os.system('cls')
        mostrar_menu_editar_nov()
        opc_aspecto = validar_entero()
        os.system('cls')

        while opc_aspecto < 1 or opc_aspecto > 4:
            print("⚠️   Opción no válida. Inténtelo nuevamente.")
            mostrar_menu_editar_nov()
            opc_aspecto = validar_entero()
            os.system('cls')

        while opc_aspecto != 4:

            match opc_aspecto:
                case 1:
                    print("Texto actual:", novedades[opc_novedad][0])
                    novedades[opc_novedad][0] = input("Ingrese el nuevo texto: ")
                case 2:
                    print("Fecha de inicio actual:", novedades[opc_novedad][1])
                    fecha_aux = pedir_fecha_valida()
                    if datetime.strptime(fecha_aux, "%d/%m/%Y") <= datetime.strptime(novedades[opc_novedad][2], "%d/%m/%Y"):
                        novedades[opc_novedad][1] = fecha_aux
                    else:
                        input("⚠️  La fecha de inicio no puede ser posterior a la de finalización. Se mantuvo la fecha original. Presione Enter para continuar.")
                case 3:
                    print("Fecha de finalización actual:", novedades[opc_novedad][2])
                    fecha_aux = pedir_fecha_valida()
                    if datetime.strptime(fecha_aux, "%d/%m/%Y") >= datetime.strptime(novedades[opc_novedad][1], "%d/%m/%Y"):
                        novedades[opc_novedad][2] = fecha_aux
                    else:
                        input("⚠️  La fecha de finalización no puede ser anterior a la de inicio. Se mantuvo la fecha original. Presione Enter para continuar.")
            os.system('cls')
            input("✅ Modificación realizada. Presione Enter para continuar...")
            mostrar_menu_editar_nov()
            opc_aspecto = validar_entero()
            os.system('cls')    
            while opc_aspecto < 1 or opc_aspecto > 4:
                print("⚠️   Opción no válida. Inténtelo nuevamente.")
                mostrar_menu_editar_nov()
                opc_aspecto = validar_entero()
                os.system('cls')
        volver()
        ver_arreglo_limitado_pr(novedades, "NOVEDADES DISPONIBLES", ["descripcion", "fecha inicio", "fecha fin"], " ", 0, [1,1], 100)
        print("Ingrese el codigo de la novedad (0 para salir)")
        opc_novedad = validar_entero()-1
    os.system('cls')
    volver()


def mostrar_menu_novedades():
    print("╔═════════════════════════════════════╗")
    print("║        📆 MENÚ DE NOVEDADES 📆      ║")
    print("╚═════════════════════════════════════╝\n")
    print("1) Crear Novedades ➕")
    print("2) Modificar Novedades ✏️")
    print("3) Eliminar Novedades 🗑️")
    print("4) Ver Novedades 📑")
    print("5) Volver al Menú Principal 🔙")

def menu_novedades():
    global novedades
    opc = -1
    while opc != 5:
        mostrar_menu_novedades()
        opc = validar_entero()
        os.system('cls')
        while opc <1 or opc>5:
            print("⚠️   Opción no válida. Inténtelo nuevamente.\n")
            mostrar_menu_novedades()
            opc = validar_entero()
            os.system('cls')
        match opc:
            case 1:
                en_construccion()
            case 2:
                editar_nov()
            case 3:
                en_construccion()
            case 4:
                ver_arreglo_limitado_pr(novedades, "NOVEDADES DISPONIBLES", ["descripcion", "fecha inicio", "fecha fin"], " ", 0, [1,1], 50)
                input("Presione Enter para continuar...")
                os.system('cls')
            case 5:
                volver()
    os.system('cls')


#-------------------------------------------------------------------------------------------------------------


def modificar_aereo(): 
    global aerolineas
    os.system('cls')
    
    codigo = input("Ingrese el código de la aerolínea que desea modificar (Presione enter para salir): ")

    while codigo != "":
        pos = busqueda_secuencial(aerolineas, codigo, 0)

        if pos == -1:
            print("⚠️ No se encontró ninguna aerolínea con ese código.")
        else:
            os.system('cls')
            print(f"Aerolínea actual:\nCódigo: {aerolineas[pos][0]}\nNombre: {aerolineas[pos][1]}\nCódigo IATA: {aerolineas[pos][2]}\nDescripción: {aerolineas[pos][3]}\nPaís: {aerolineas[pos][4]}")
            print()
            print("Seleccione qué desea modificar:")
            print("1. Nombre ✏️")
            print("2. Código IATA 🛫")
            print("3. Descripción 📝")
            print("4. País 🌍")
            print("5. Volver 🔙")
            opcion = validar_entero()

            while opcion < 1 or opcion > 5:
                print("⚠️  Opción no válida. Inténtelo nuevamente.")
                opcion = validar_entero()

            if opcion == 1:
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                aerolineas[pos][1] = nuevo_nombre
            elif opcion == 2:
                nuevo_iata = pedir_codigo_IATA()
                aerolineas[pos][2] = nuevo_iata
            elif opcion == 3:
                nueva_descripcion = input("Ingrese la nueva descripción: ")
                aerolineas[pos][3] = nueva_descripcion
            elif opcion == 4:
                nuevo_pais = pedir_codigo_pais()
                aerolineas[pos][4] = nuevo_pais
            else:
                volver()

            input("✅ Modificación realizada (o cancelada). Presione Enter para continuar...")

        os.system('cls')
        codigo = input("Ingrese otro código de aerolínea a modificar (Presione enter para salir): ")

    os.system('cls')
    volver()

def pedir_codigo_pais():
    print("\nCodigo de pais:")
    print('- "ARG"')
    print('- "CHI"')
    print('- "BRA"')
    codigo_pais = input("Ingrese la opcion que desea (SIN ESPACIOS O CARACTERES ESPECIALES Y TODO EN MAYUSCULAS)\n")
    print("")
    while codigo_pais != "ARG" and codigo_pais != "CHI" and codigo_pais != "BRA":
        print("⚠️   Opción no válida. Inténtelo nuevamente.")
        print("\nCodigo de pais:")
        print('- "ARG"')
        print('- "CHI"')
        print('- "BRA"')
        codigo_pais = input("Ingrese la opcion que desea (SIN ESPACIOS O CARACTERES ESPECIALES Y TODO EN MAYUSCULAS)\n")
        print("")
    return codigo_pais

def pedir_codigo_IATA():
    codigo = input("Ingrese código IATA: ")
    while not (1 <= len(codigo) <= 3):   
        print("El código debe tener como máximo 3 caracteres")
        codigo = input("Ingrese código IATA: ")
    return codigo

def pedir_codigo_aerolinea():
    codigo = input("Ingrese código de la aerolinea: ")
    while not (1 <= len(codigo) <= 5):   
        print("El código debe tener como minimo 1 caracter y como máximo 5 caracteres")
        codigo = input("Ingrese código de la aerolinea: ")
    return codigo

def crear_aereo():
    global aerolineas
    nombre_aereo = input('Ingrese el nombre de la aerolínea. Presione enter para salir\n')
    cantidad_aereo =  busqueda_secuencial(aerolineas,"",0)
    contadores = [0]*3
    paises = ["ARG", "BRA", "CHI"]
    if cantidad_aereo == -1:
        input("\nYa no se pueden cargar mas aerolíneas. Presione enter para continuar")
        nombre_aereo = ""
    else:
        while nombre_aereo != "" and cantidad_aereo < 5:
            codigo_nuevo = pedir_codigo_aerolinea()
            nro = busqueda_secuencial(aerolineas, codigo_nuevo, 0)
            while nro != -1:
                print("Ese código de aerolínea ya existe. Intente con otro.")
                codigo_nuevo = pedir_codigo_aerolinea()
                nro = busqueda_secuencial(aerolineas, codigo_nuevo, 0)
            aerolineas[cantidad_aereo][0]=codigo_nuevo
            aerolineas[cantidad_aereo][1]=nombre_aereo
            aerolineas[cantidad_aereo][2] = pedir_codigo_IATA()
            aerolineas[cantidad_aereo][3]= input("Ingrese la descripcion del vuelo: ")
            codigo_pais = pedir_codigo_pais()
            aerolineas[cantidad_aereo][4]=codigo_pais

            os.system('cls')
            cantidad_aereo = cantidad_aereo+1
            nombre_aereo =input('Ingrese el nombre de la aerolínea. Presione enter para salir\n')
    
    for i in range(0,5):#es necesario recorrer ya que el admin puede registrar una aerolinea, irse y despues registrar otra.
        match aerolineas[i][4]:
            case "ARG":
                contadores[0]=contadores[0]+1
            case "BRA":
                contadores[1]=contadores[1]+1
            case "CHI":
                contadores[2]=contadores[2]+1
    
    
    if contadores[0] == contadores[1] == contadores[2]:
        print("Los tres codigos (ARG, CHI y BRA) tienen la misma cantidad de aerolineas cargadas:", contadores[0])
        print("")
    else:
        menor=obtener_pos_menor(contadores)
        mayor=obtener_pos_mayor(contadores)
        print("")
        print("Mayor:", paises[mayor],"con una cantidad de aerolineas cargadas de", contadores[mayor])
        print("Menor:", paises[menor],"con una cantidad de aerolineas cargada de", contadores[menor])
        print("")
    volver()


def mostrar_menu_gestion_aereo():
    print("╔════════════════════════════════════════╗")
    print("║  🛩️  MENÚ DE GESTIÓN DE AEROLÍNEAS 🛩️    ║")
    print("╚════════════════════════════════════════╝\n")
    print("1) Crear Aerolínea ✈️")
    print("2) Modificar Aerolínea ✏️")
    print("3) Eliminar Aerolínea 🗑️")
    print("4) Volver al Menú Principal 🔙")

def menu_gestion_aereo(): #menu 1
    opc = -1
    while opc != 4:
        mostrar_menu_gestion_aereo()
        opc = validar_entero()
        os.system('cls')
        while opc <1 or opc >4:
            print("⚠️   Opción no válida. Inténtelo nuevamente.\n")
            mostrar_menu_gestion_aereo()
            opc = validar_entero()
            os.system('cls')
        match opc:
            case 1:
                crear_aereo()
            case 2:
                modificar_aereo()
            case 3:
                en_construccion()
            case 4:
                volver()

def mostrar_menu_principal_admin():
    print("╔════════════════════════════════════╗")
    print("║ 🏠    MENÚ PRINCIPAL ADMIN  🏠        ║")
    print("╚════════════════════════════════════╝\n")
    print("1) Gestión de Aerolíneas 🛩️")
    print("2) Aprobar / Denegar Promociones💲")
    print("3) Gestión de Novedades 📆")
    print("4) Mostrar Reportes 📊")
    print("5) Salir del Programa ❌")

def menu_administrador():
    opc = -1
    while opc != 5:
        mostrar_menu_principal_admin()
        opc = validar_entero()
        os.system('cls')
        while opc < 1 or opc > 5:
            print("⚠️   Opción no válida. Inténtelo nuevamente.\n")
            mostrar_menu_principal_admin()
            opc = validar_entero()
            os.system('cls')
        match opc:
            case 1:
                menu_gestion_aereo()
            case 2:
                en_construccion()
            case 3:
                menu_novedades()
            case 4:
                menu_report()
            case 5:
                os.system('cls')
                volver()

#-------------------------------------------------------------------------------------------------------------








#-----------------------------------------------------------------------MENU CEO-------------------------------------------------------------



def  mostrar_menu_reportes():
    print("╔════════════════════════════════════════╗")
    print("║        📊  MENÚ DE REPORTES 📊         ║")
    print("╚════════════════════════════════════════╝\n")
    print("1) Reporte de ventas de mi Aerolínea 💲") 
    print("2) Reporte de ocupación de Vuelos de mi Aerolínea 📆")
    print("3) Volver al Menú Principal 🔙")
        
def  menu_reportes_ceo():
    opc= -1 
    while opc != 3:
        mostrar_menu_reportes()
        opc = validar_entero()
        os.system('cls')
        while opc < 1 or opc > 3:
            print("⚠️   Opción no válida. Inténtelo nuevamente.\n")
            mostrar_menu_reportes()
            opc = validar_entero()
            os.system('cls')
        match opc:
            case 1:
                en_construccion()
            case 2:
                en_construccion()
            case 3:
                volver()

def  mostrar_menu_gestion_promociones():
    print("╔════════════════════════════════════════╗")
    print("║ 💲 MENÚ DE GESTIÓN DE PROMOCIONES 💲   ║")
    print("╚════════════════════════════════════════╝\n")
    print("1) Crear  Promoción💲 ") 
    print("2) Modificar  Promoción ✏️")
    print("3) Eliminar  Promoción 🗑️")
    print("4) Volver al Menú Principal 🔙") 

    
def  menu_gestion_promociones():
    opc= -1 
    while opc != 4:
        mostrar_menu_gestion_promociones()
        opc = validar_entero()
        os.system('cls')
        while opc < 1 or opc > 4:
            print("⚠️   Opción no válida. Inténtelo nuevamente.\n")
            mostrar_menu_gestion_promociones()
            opc = validar_entero()
            os.system('cls')
        match opc:
            case 1:
                en_construccion()
            case 2:
                en_construccion()
            case 3:
                en_construccion()
            case 4:
                volver() 

def validar_hora(): 
    h = [0,0]
    m = [0,0]
    hora_valida = False
    while not hora_valida:
        hora = input("Ingrese la hora (HH:MM): ")
        if len(hora) == 5 and hora[2] == ":":
            for i in range(2):
                j = i+3
                h[i]=hora[i]
                m[i]=hora[i + 3]
                
            try:
                hh = int(h[0]) * 10 + int(h[1])
                mm = int(m[0]) * 10 + int(m[1])
                
                if 0 <= hh <= 23 and 0 <= mm <= 59:
                    hora_valida = True
                    
                else:
                    print("hora fuera de rango.")
                    
            except ValueError:
                print("formato invalido solo numeros.") 
                
        else:
            print("formato incorrecto use HH:MM.")
                        
    return hora

def validar_precio():
    valido = False
    while not valido:
        entrada = input("Precio del vuelo: ")
        try:
            precio = float(entrada)
            if precio >= 0:
                valido = True
            else:
                print("⚠️ El precio no puede ser negativo.")
        except:
            print("⚠️ Precio inválido. Ingrese solo números.")
    return precio
            
def eliminar_vuelo():
    global vuelos, CANTIDAD_VUELOS
    codigo = 0
    
    while codigo != CANTIDAD_VUELOS:
        print(f"ingrese el codigo del vuelo que quiere eliminar, {CANTIDAD_VUELOS} para salir. ")
        codigo = validar_entero()
        os.system('cls')
        while codigo == -1 or codigo > CANTIDAD_VUELOS:
            print(f" ⚠️  codigo de vuelo invalido, {CANTIDAD_VUELOS} para salir. ")
            codigo = validar_entero()
            
        if codigo == CANTIDAD_VUELOS:
            volver()
        else:
            if vuelos[codigo][5] != 'A' and vuelos[codigo][5] != 'B' :
                print("no se ha creado un vuelo con ese codigo aun. ")
                volver()
            else:
                if vuelos[codigo][5] == 'A':
                    opc = input("seguro que quiere eliminar el vuelo, S(si) N(no): ")
                    while opc != 'S' and opc != 'N':
                        opc = input("opcion invalida, poravor seleccione S o N: ")
                        
                    if opc == 'S':
                        vuelos[codigo][5] = 'B'
                        print("se ha eliminado el vuelo nro:", codigo)
                        volver()
                    else:
                        input("no se ha eliminado el vuelo, presione enter para volver.")
                else:
                    input("ese vuelo ya fue eliminado, presione enter para volver.")   

def mostrar_opciones_modificacion():
    print("\nSeleccione qué desea modificar:")
    print("1. Codigo aerolinea 🛫")
    print("2. Origen 🛫")
    print("3. Destino 🛫")
    print("4. Fecha salida 📅")
    print("5. Hora salida 🕒")
    print("6. Precio 💰")
    print("7. Volver 🔙")

def modificar_vuelo():
    global vuelos, precios_vuelos, aerolineas, CANTIDAD_VUELOS, CANTIDAD_AEROLINEAS

    codigo = 0 

    while codigo != CANTIDAD_VUELOS:

        print(f"Ingrese el código del vuelo que quiere modificar ({CANTIDAD_VUELOS} para salir): ")
        codigo = validar_entero()

        if codigo == -1:
            print("⚠️  Entrada inválida. Intente nuevamente.")
        elif codigo == CANTIDAD_VUELOS:
            volver()
        elif codigo<0 or codigo>19:
            print("⚠️  Código de vuelo inválido. Inténtelo nuevamente.")
        else:
            estado = vuelos[codigo][5]
            puede_modificar = False

            if estado == 'A':
                puede_modificar = True

            elif estado == 'B':
                print("✈️  VUELO EN ESTADO INACTIVO.")
                opc = input("¿Desea cambiar el estado de su vuelo? S(si) / N(no): ").upper()
                while opc != 'S' and opc != 'N':
                    opc = input("Opcion invalida. Seleccione S o N: ").upper()
                if opc == 'S':
                    vuelos[codigo][5] = 'A'
                    puede_modificar = True
                else:
                    print("No se puede modificar un vuelo en estado INACTIVO.")

            else:
                print("No existe ningún vuelo activo o dado de baja con ese código.")

            if puede_modificar:
                opcion = 0  
                while opcion != 7:
                    print("\n✈️  VUELO EN ESTADO ACTIVO:")
                    print("Codigo aerolinea:", vuelos[codigo][0])
                    print("Origen:", vuelos[codigo][1])
                    print("Destino:", vuelos[codigo][2])
                    print("Fecha salida:", vuelos[codigo][3])
                    print("Hora salida:", vuelos[codigo][4])
                    print("Precio: $", precios_vuelos[codigo])

                    mostrar_opciones_modificacion()
                    opcion = validar_entero()

                    while opcion < 1 or opcion > 7:
                        print("⚠️  Opción no válida. Inténtelo nuevamente.")
                        opcion = validar_entero()

                    match opcion:
                        case 1:
                            existe = -1
                            while existe == -1:
                                nuevo_cod_aerolinea = ""
                                while nuevo_cod_aerolinea =="":
                                    nuevo_cod_aerolinea = input("Ingrese el nuevo codigo de aerolinea: ")
                                existe = busqueda_secuencial(aerolineas,nuevo_cod_aerolinea,0)
                            vuelos[codigo][0]=nuevo_cod_aerolinea
                        case 2:
                            vuelos[codigo][1] = input("Nuevo origen: ").upper()
                        case 3:
                            vuelos[codigo][2] = input("Nuevo destino: ").upper()
                        case 4:
                            vuelos[codigo][3] = pedir_fecha_valida()
                        case 5:
                            vuelos[codigo][5] = validar_hora()
                        case 6:
                            precios_vuelos[codigo] = validar_precio()
                        case 7:
                            volver()
                    if opcion != 7:
                        print("✅ Modificación realizada.")

def listar_vuelos_aerolineas():
    global vuelos, aerolineas, CANTIDAD_VUELOS, CANTIDAD_AEROLINEAS
    fecha_actual = datetime.today()
    vuelos_por_aerolinea = [[i, 0] for i in range(CANTIDAD_AEROLINEAS)]

    i = 0
    while i < CANTIDAD_VUELOS and vuelos[i][0] != "":
        if vuelos[i][5]=="A":
            fecha_vuelo = datetime.strptime(vuelos[i][3], "%d/%m/%Y")
            if fecha_vuelo > fecha_actual:
                cod_aerolinea = vuelos[i][0]
                pos = busqueda_secuencial(aerolineas, cod_aerolinea, 0)
                if pos != -1:
                    vuelos_por_aerolinea[pos][1] += 1
        i += 1

    ordenar_burbuja_desc(vuelos_por_aerolinea, 1, 2)

    print("\n" + "="*60)
    print("REPORTE DE VUELOS --VIGENTES-- POR AEROLINEA")
    print("="*60)
    print(f"{'POSICION':<10}{'AEROLINEA':<30}{'CANTIDAD DE VUELOS'}")
    print("-" * 60)

    total = 0
    i = 0
    while i < CANTIDAD_AEROLINEAS and aerolineas[i][0] != "":
        pos_aero = vuelos_por_aerolinea[i][0]
        nombre = aerolineas[pos_aero][1]
        cantidad = vuelos_por_aerolinea[i][1]
        print(f"{i:<10}{nombre:<30}{cantidad}")
        total += cantidad
        i += 1

    print("-" * 60)
    print(f"TOTAL DE VUELOS VIGENTES: {total}")
    
    if i > 0:
        print(f"Aerolínea con MAYOR cantidad de vuelos: {aerolineas[vuelos_por_aerolinea[0][0]][1]} ({vuelos_por_aerolinea[0][1]})") #la aerolinea que se encuentra en la primer posicion del arreglo ordenado de forma descendente y su cantidad
        print(f"Aerolínea con MENOR cantidad de vuelos: {aerolineas[vuelos_por_aerolinea[i - 1][0]][1]} ({vuelos_por_aerolinea[i - 1][1]})") #la aerolinea que se encuentra en la ultima posicion no "vacia" del arreglo ordenado de forma descendente y su cantidad
    
    
def crear_vuelo():
    global aerolineas, vuelos, precios_vuelos, asientos, ASIENTOS_POR_AVION, CANTIDAD_VUELOS
    ultimo= busqueda_secuencial(vuelos, "", 0)
     #VER
    
    while ultimo!=-1 and ultimo<=(int(CANTIDAD_VUELOS-1)):

        print("\nIngrese datos del vuelo (deje el codigo vacio para salir):")
        codigo = input("Codigo de aerolinea: ")
        if codigo == "":
            ultimo = 100
        else:
            ultimo_vuelo_aerolinea = busqueda_secuencial(aerolineas, codigo, 0)
            if ultimo_vuelo_aerolinea == -1:
                print("Aerolínea no encontrada. Intente nuevamente.")
            else:
                vuelos[ultimo][0] = codigo
                vuelos[ultimo][1] = input("Origen: ").upper()
                vuelos[ultimo][2] = input("Destino: ").upper()
                vuelos[ultimo][3] = pedir_fecha_valida()
                vuelos[ultimo][4] = validar_hora()
                vuelos[ultimo][5] = "A"
                precios_vuelos[ultimo] = validar_precio()
                
                
                j = int((ultimo * ASIENTOS_POR_AVION)/6)
                for i in range(int(ASIENTOS_POR_AVION/6)):
                    for k in range(3): #carga hasta pasillo
                        asientos[j][k] = random.choice(["L", "O", "R"])
                    for k in range(4,7): #carga dsp pasillo
                        asientos[j][k] = random.choice(["L", "O", "R"])
                    j += 1
                print("✔ Vuelo cargado correctamente.")
        ultimo = ultimo+1           
    if ultimo == -1 or ultimo==CANTIDAD_VUELOS:
        print("Ya no hay espacio disponible para mas vuelos.")
    listar_vuelos_aerolineas()
    volver()

def mostrar_menu_gestion_vuelos():
    print("╔════════════════════════════════════════╗")
    print("║    🛩️  MENÚ DE GESTIÓN DE VUELOS 🛩️      ║")
    print("╚════════════════════════════════════════╝\n")
    print("1) Crear Vuelo ✈️")
    print("2) Modificar Vuelo ✏️")
    print("3) Eliminar Vuelo 🗑️")
    print("4) Volver al Menú Principal 🔙") 

def menu_gestion_vuelos():
    global vuelos, asientos, precios_vuelos
    opc = -1
    while opc !=4:
        mostrar_menu_gestion_vuelos()
        opc=validar_entero()
        while opc<1 or opc>4:
            print("⚠️  Opción no válida. Inténtelo nuevamente.\n")
            mostrar_menu_gestion_vuelos()
            opc=validar_entero()
        mostrar = -1
        while opc!=4 and (mostrar<1 or mostrar>2):
            print("Desea ver los vuelos cargados hasta el momento? 1-Si 2-No")
            mostrar = validar_entero()
        if mostrar == 1:
            ver_arreglo_limitado_pr(vuelos, "TODOS los vuelos Ingresados (incluyendo eliminados/no vigentes)", ["Cod Ar", "Origen", "Destino", "Salida", "Hora","Estado"], "", 0, [1,0], 15)
            ver_arreglo_limitado_unidimensional(precios_vuelos, "Precios vuelos", ["Precio"], 0,[1,0],15)

        match opc:
            case 1:
                crear_vuelo()
            case 2:
                modificar_vuelo()
            case 3:
                eliminar_vuelo()
            case 4:
                volver()

def mostrar_menu_principal_ceo():
    print("╔════════════════════════════════════╗")
    print("║   🏠   MENÚ PRINCIPAL CEO   🏠     ║")
    print("╚════════════════════════════════════╝\n")
    print("1) Gestión de Vuelos 🛩️")
    print("2) Gestión de  Promociones💲")
    print("3) Reportes 📊")
    print("4) Salir del Programa ❌")

def menu_ceo():
    opc = -1
    while opc != 4:
        mostrar_menu_principal_ceo()
        opc = validar_entero()
        os.system('cls' if os.name == 'nt' else 'clear')

        while opc < 1 or opc > 4:
            print("⚠️  Opción no válida. Inténtelo nuevamente.\n")
            mostrar_menu_principal_ceo()
            opc = validar_entero()
            os.system('cls' if os.name == 'nt' else 'clear')

        match opc:
            case 1:
                menu_gestion_vuelos()
            case 2:
                menu_gestion_promociones()
            case 3:
                menu_reportes_ceo()
            case 4:
                print("Cerrando sesión...\n")
                os.system('cls' if os.name == 'nt' else 'clear')









#--------------------------MENU USUARIO---------------------------------------------

def ver_vuelos(vuelos, aerolineas, precio, cant_vuelos):
    print("\n") 
    print("="*100)
    print("LISTADO DE VUELOS DISPONIBLES EN EL SISTEMA".center(100))
    print("="*100)
    print("\n")
    print("CÓDIGO   AEROLÍNEA          ORIGEN           DESTINO        FECHA        HORA     PRECIO")
    print("-"*100)
    fecha_actual = datetime.today()
    i = 0
    cont = 0
    
    while i < cant_vuelos and vuelos[i][0] != "":
        if vuelos[i][5] == "A":
            fecha_vuelo = datetime.strptime(vuelos[i][3], "%d/%m/%Y")
            if fecha_vuelo > fecha_actual:
                cont = cont + 1   
                pos_aerolinea = busqueda_secuencial(aerolineas, vuelos[i][0], 0)
                print(f"{i:<8}{aerolineas[pos_aerolinea][1]:<20}{vuelos[i][1]:<16}{vuelos[i][2]:<16}{vuelos[i][3]:<12}{vuelos[i][4]:<8}${precio[i]:<5}") 
               
        i += 1
    print("-"*100)
    print(f"Total de vuelos: {cont}")
    volver()
    
def  buscar_vuelos():
    global vuelos, aerolineas, CANTIDAD_VUELOS, precios_vuelos
    fecha = input("Ingrese la fecha en formato dd/mm/aaaa, Enter para salir: ")
    valida = validar_fecha(fecha)
   
    while fecha != '' and valida != True :
        fecha = input("Porfavor, Ingrese la fecha en formato dd/mm/aaaa, Enter para salir: ")
        valida = validar_fecha(fecha)
    if valida == True :
        os.system('cls')
        ver_vuelos(vuelos, aerolineas, precios_vuelos, CANTIDAD_VUELOS)


def mostrar_asientos(asientos, vuelo):
    inicio = int(vuelo * ASIENTOS_POR_AVION/6)#si es el 0, va a empezar en el 0, si es 1, va empezar en el 40 que es 1 mas del final del primer vuelo
    fin = int(inicio + ASIENTOS_POR_AVION/6)#se desplaza la cantidad de filaas que es la cantidad de asientos por avion sobre la cantidad de asientos por fila
    print("   A     B     C         D     E     F")
    print("+-----+-----+-----+   +-----+-----+-----+")
    for i in range(inicio, fin):
        for j in range(7):
            print("|",asientos[i][j],"|", end=" ")
        print()

def validar_vigencia(arreglo, vuelo):
    vigente = False
    if arreglo[vuelo][5]=="A":
        fecha_actual = datetime.today()
        fecha_vuelo = datetime.strptime(vuelos[vuelo][3], "%d/%m/%Y")
        if fecha_vuelo > fecha_actual:
            vigente = True
    return vigente

def  buscar_asientos():
    global CANTIDAD_VUELOS, vuelos, asientos
    vuelo = -1
    while vuelo != CANTIDAD_VUELOS:
        print(f"Ingrese el codigo del vuelo del cual quiere ver los asientos, {CANTIDAD_VUELOS} para salir. ")
        vuelo = validar_entero()
        os.system('cls')
        while vuelo == -1 or vuelo > CANTIDAD_VUELOS:
            print(f" ⚠️  Codigo de vuelo invalido, {CANTIDAD_VUELOS} para salir. ")
            vuelo = validar_entero()
        if vuelo == CANTIDAD_VUELOS:
            volver()
        else:
            if validar_vigencia(vuelos, vuelo):
                mostrar_asientos(asientos, vuelo)
            else:
                print("El vuelo no esta vigente.")


def  mostrar_menu_principal_usuario():
    print("╔════════════════════════════════════╗")
    print("║   👤 MENÚ PRINCIPAL USUARIO  👤    ║")
    print("╚════════════════════════════════════╝\n")
    print("1) Buscar Vuelos 🛩️")
    print("2) Buscar Asientos💺")
    print("3) Reservar Vuelos 🛩️")
    print("4) Gestionar Reservas 📆")
    print("5) Ver Historial de Compras 💲")
    print("6) Ver Novedades 📑")
    print("7) Cerrar Sesión ❌")
    
def menu_usuario():
     opc = -1
     global novedades
     while opc != 7:
        mostrar_menu_principal_usuario()
        opc = validar_entero()
        os.system('cls' if os.name == 'nt' else 'clear')

        while opc < 1 or opc > 7:
            print("⚠️  Opción no válida. Inténtelo nuevamente.\n")
            mostrar_menu_principal_usuario()
            opc = validar_entero()
            os.system('cls' if os.name == 'nt' else 'clear')

        match opc:
            case 1:
                buscar_vuelos()
            case 2:
                buscar_asientos()
            case 3:
                en_construccion()
            case 4:
                en_construccion()
            case 5:
                en_construccion()
            case 6:
                ver_arreglo_limitado_pr(novedades, "NOVEDADES DISPONIBLES", ["descripcion", "fecha inicio", "fecha fin"], " ", 0, [1,1], 100)
            case 7:
                input("Cerrando sesión...\nPresione enter para continuar")
                os.system('cls' if os.name == 'nt' else 'clear')
       
#----------------------------------------------------------------------------------------------------------------------------------





#----------------------------------------MAIN---------------------------------------------------------------------------------------------

def registrarse(arfi_usuarios, arlo_usuarios):
    registrado = False
    mail = input("\nIngrese el mail con el que quiere registrarse o * para volver: ")
    while mail == "":
            print("\nDebe ingresar un mail")
            mail = input("\nIngrese el mail con el que quiere registrarse o * para volver: ")
    while mail != "*" and not registrado:
        mail = mail.ljust(100," ")
        posicion = busqueda_secuencial_registro(arfi_usuarios,arlo_usuarios,mail, "email_usuario")
        while posicion !=-1:
                print("El mail ya fue utilizado. Intentelo nuevamente con un correo distinto")
                mail = input("\nIngrese el mail con el que quiere registrarse o * para volver: ")
                while mail == "":
                    print("\nDebe ingresar un mail")
                    mail = input("\nIngrese el mail con el que quiere registrarse o * para volver: ")
                mail = mail.ljust(100," ")
                posicion = busqueda_secuencial_registro(arfi_usuarios,arlo_usuarios,mail, "email_usuario")
        else:
            arlo_usuarios.seek(0,2)
            user = usuario()
            user.email_usuario = mail
            cod = buscar_ultimo_registro(arfi_usuarios,arlo_usuarios)+1
            user.cod_usuario = cod
            clave = " "
            while len(clave)!=8:
                clave = input("Ingrese la clave de 8 caracteres: ")
            user.clave_usuario = clave
            tipo = " "
            while tipo !="ceo de aerolinea" and tipo !="usuario":
                tipo = input("Ingrese el tipo de usuario: ")
            tipo = tipo.ljust(20, " ")
            user.tipo_usuario = tipo
            telefono=" "
            while telefono == " " or len(telefono)>100:
                telefono = input("Ingrese el telefono: ")
                telefono = telefono.ljust(100, " ")
            user.telefono_usuario = telefono
            pickle.dump(user, arlo_usuarios)
            arlo_usuarios.flush()
            
            registrado = True
    os.system('cls')
        
def menu_login():
    print("╔════════════════════════════════════╗")
    print("║       🏠  INICIAR SESION  🏠       ║")
    print("╚════════════════════════════════════╝\n")
        
def login(arfi_usuarios, arlo_usuarios):
    intentos = 3
    tamArc = os.path.getsize(arfi_usuarios)
    tamReg = calcular_tamanio_registro(tamArc,arlo_usuarios)
    menu_login()
    mail_usuario = input("\nIngrese su usuario (enter para volver): ")
    
    while intentos != 0 and mail_usuario!="":
        mail_usuario = mail_usuario.ljust(100, " ")
        print(mail_usuario, "hola")
        contrasenia = pwinput.pwinput(prompt="Ingrese la contraseña: ")
        os.system('cls')
        posicion = busqueda_secuencial_registro(arfi_usuarios,arlo_usuarios, mail_usuario, "email_usuario")
        print(posicion)
        #posicion = busqueda_secuencial(usuarios, mail_usuario , 0)
        if posicion !=-1:
            arlo_usuarios.seek(posicion * tamReg,0)
            usuario = pickle.load(arlo_usuarios)
            if  contrasenia == usuario.clave_usuario: 
                intentos = 3 
                tipo_usuario = usuario.tipo_usuario
                if tipo_usuario == "administrador".ljust(20, " "):
                    menu_administrador()
                elif tipo_usuario == "ceo de aerolinea".ljust(20, " "):
                    menu_ceo()
                else:
                    menu_usuario()
            else:
                intentos = intentos -1
                print ("\nContraseña o usuario incorrectas, le quedan", intentos,"intentos\n" )
        else:
            intentos = intentos - 1
        if intentos == 0: 
                print("\nHubieron 3 intentos fallidos. Por medidas de seguridad se cerrara el programa\n")
        else:
            if intentos!=3:
                print ("\nContraseña o usuario incorrectas, le quedan", intentos,"intentos\n" )
                menu_login()
                mail_usuario = input("Ingrese su mail (Enter para volver):")
    os.system('cls')

def mostrar_primer_menu():
    print("╔════════════════════════════════════╗")
    print("║      🏠   BIENVENIDO     🏠        ║")
    print("╚════════════════════════════════════╝\n")
    print("1) Registrarse")
    print("2) Iniciar sesion")
    print("3) Salir")

def cargarNovedades(novedades):
    novedades[0][0] = "promocion aniversario"
    novedades[0][1] = "02/10/2025"
    novedades[0][2] = "01/11/2025"

    novedades[1][0] = "nueva disposicion equipaje"
    novedades[1][1] = "23/06/2025"
    novedades[1][2] = "23/07/2025"

    novedades[2][0] = "vuelos a Miami suspendidos"
    novedades[2][1] = "04/08/2025"
    novedades[2][2] = "11/08/2025"

def cargarUsuarios(usuarios):
    # Inicializar matriz de 10 usuarios con 4 columnas (email, clave, rol, extra opcional)
    
    # Administrador
    usuarios[0][0] = "admin"
    usuarios[0][1] = "admin123"
    usuarios[0][2] = "administrador"

    # CEOs
    usuarios[1][0] = "ceo"
    usuarios[1][1] = "ceo123"
    usuarios[1][2] = "ceo"

    usuarios[2][0] = "ceo2@ventaspasajes777.com"
    usuarios[2][1] = "ceo456"
    usuarios[2][2] = "ceo"

    usuarios[3][0] = "ceo3@ventaspasajes777.com"
    usuarios[3][1] = "ceo789"
    usuarios[3][2] = "ceo"

    usuarios[4][0] = "ceo4@ventaspasajes777.com"
    usuarios[4][1] = "ceo321"
    usuarios[4][2] = "ceo"

    usuarios[5][0] = "ceo5@ventaspasajes777.com"
    usuarios[5][1] = "ceo654"
    usuarios[5][2] = "ceo"

    # Usuarios comunes
    usuarios[6][0] = "usuario"
    usuarios[6][1] = "usuario123"
    usuarios[6][2] = "usuario"

    usuarios[7][0] = "usuario2@ventaspasajes777.com"
    usuarios[7][1] = "usuario456"
    usuarios[7][2] = "usuario"

#PROGRAMA PRINCIPAL



novedades = [[""] * 4 for i in range(3)] #no dice en ningun lado hasta cuantas novedades pueden ser
cargarNovedades(novedades)
usuarios = [[""] * 3 for i in range(10)]
cargarUsuarios(usuarios)
CANTIDAD_VUELOS = 20
CANTIDAD_AEROLINEAS = 5
aerolineas = [[""] * 5 for i in range(int(CANTIDAD_AEROLINEAS))]
vuelos = [[""]* 6 for i in range(int(CANTIDAD_VUELOS))]
precios_vuelos = [0.0 for i in range(int(CANTIDAD_VUELOS))]
ASIENTOS_POR_AVION = 240
asientos = [[""]*7 for i in range(int(20*(ASIENTOS_POR_AVION/6)))]

class usuario:
    def __init__(self):
        self.cod_usuario = 0
        self.email_usuario = ""
        self.clave_usuario = ""
        self.tipo_usuario = ""
        self.telefono_usuario = ""  

class aerolinea:
    def __init__(self):
        self.cod_aerolinea = 0
        self.nombre_aerolinea = ""
        self.cod_IATA = ""
        self.descripcion_aerolinea = ""
        self.cod_pais = ""
        
class vuelo:
    def __init__(self):
        self.cod_vuelo = 0
        self.cod_aerolinea = ""
        self.origen_vuelo = ""
        self.destino_vuelo = ""
        self.fecha_salida = ""
        self.hora_salida = ""
        self.precio_vuelo = 0.0
        self.asientos_vuelo = asientos = [[""]*7 for i in range(int(20*(ASIENTOS_POR_AVION/6)))]

class reserva:
    def __init__(self):
        self.cod_reserva = 0
        self.cod_usuario = 0
        self.cod_vuelo = 0
        self.fecha_reserva = 0
        self.estado_reserva = ""
        self.nro_asiento = ""
        
arfi_usuarios = "usuarios.dat"
arfi_aerolineas = "aerolineas.dat"
arfi_vuelos = "vuelos.dat"
arfi_reservas = "reservas.dat"

if os.path.exists(arfi_usuarios):
    arlo_usuarios = open(arfi_usuarios, "r+b")
    arlo_aerolineas = open(arfi_aerolineas, "r+b")
    arlo_vuelos = open(arfi_vuelos, "r+b")
    arlo_reservas = open(arfi_reservas, "r+b")
else:
    input(f"Los archivos {arfi_usuarios} {arfi_aerolineas} {arfi_vuelos} {arfi_reservas} NO existian y fueron creados")
    arlo_usuarios = open(arfi_usuarios, "w+b")
    arlo_aerolineas = open(arfi_aerolineas, "w+b")
    arlo_vuelos = open(arfi_vuelos, "w+b")
    arlo_reservas = open(arfi_reservas, "w+b")
    user = usuario()
    user.cod_usuario = 0
    user.email_usuario = "admin@ventaspasajes.com".ljust(100, " ")
    user.clave_usuario = "admin123".ljust(8," ")
    user.tipo_usuario = "administrador".ljust(20, " ")
    user.telefono_usuario = "3413112233".ljust(100, " ")
    pickle.dump(user, arlo_usuarios)
    arlo_usuarios.flush()
    

mostrar_primer_menu()
opc = validar_entero()
while opc!= 3:
    while opc <  1 or opc >3:
        print("⚠️   Opción no válida. Inténtelo nuevamente.")
        mostrar_primer_menu
        opc = validar_entero()
    os.system('cls')
    match opc:
        case 1:
            registrarse(arfi_usuarios,arlo_usuarios)
            mostrar_primer_menu()
            opc = validar_entero()
        case 2:
            login(arfi_usuarios,arlo_usuarios)
            mostrar_primer_menu()
            opc = validar_entero()
        case 3:
            print()
print("Cerrando programa...") 


