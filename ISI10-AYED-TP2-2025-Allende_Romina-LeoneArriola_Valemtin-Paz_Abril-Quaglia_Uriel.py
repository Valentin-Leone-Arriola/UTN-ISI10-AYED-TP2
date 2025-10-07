
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

def calcular_tamanio_registro(arfi,arlo):
    len_archivo  = os.path.getsize(arfi)
    if len_archivo != 0:
        arlo.seek(0,0)
        registro = pickle.load(arlo) 
        len_registro = arlo.tell()
        return len_registro
    else:
        return -1

def calcular_cant_registros(arfi, arlo):
    len_archivo  = os.path.getsize(arfi)
    if len_archivo != 0:
        arlo.seek(0,0)
        registro = pickle.load(arlo) 
        len_registro = arlo.tell()
        cant_registros = len_archivo // len_registro #al ser registros de tamanio fijo, no es necesario verificar que no sea cero para no dividir por 0. Si fuese 0 entonces todo el documento tendria registros vacios
        return cant_registros    
    else:
        return 0
    

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


def busqueda_secuencial_reservas(arfi, arlo, valor1, valor2):
    arlo.seek(0,0)
    cant_registros = calcular_cant_registros(arfi, arlo)
    if cant_registros != 0:
        arlo.seek(0,0)
        i = 1
        registro = reserva()
        registro = pickle.load(arlo)
        while registro.cod_vuelo != valor1 and registro.estado_reserva.strip() != valor2 and i < cant_registros:
            i = i+1
            registro = pickle.load(arlo)
        if registro.cod_vuelo == valor1 and registro.estado_reserva.strip() == valor2:
            return i-1
        else:
            return -1
    else:
        return -1

def busqueda_secuencial_aerolinea_cod(valor):
    arlo_aerolineas.seek(0,0)
    cant_registros = calcular_cant_registros(arfi_aerolineas, arlo_aerolineas)
    if cant_registros != 0:
        arlo_aerolineas.seek(0,0)
        i = 1
        registro = aerolinea()
        registro = pickle.load(arlo_aerolineas)
        while registro.cod_aerolinea.strip() != valor and i < cant_registros:
            i = i+1
            registro = pickle.load(arlo_aerolineas)
        if registro.cod_aerolinea.strip() == valor:
            return i-1
        else:
            return -1
    else:
        return -1

    
def aero_en_uso_y_con_reservas(cod_aero):
    global arlo_vuelos
    global arfi_vuelos
    global arlo_reservas
    global arfi_reservas
    en_uso = False
    tiene_reservas = False
    
    if os.path.getsize(arfi_vuelos) > 0:
        arlo_vuelos.seek(0,0)
        while arlo_vuelos.tell() < os.path.getsize(arfi_vuelos):
            vuelo = pickle.load(arlo_vuelos)
            if vuelo.cod_aerolinea.strip() == cod_aero.strip(): #si el vuelo pertenece a la aerolinea
                en_uso = True #como esta en uso
                codigo_vuelo = vuelo.cod_vuelo
                if os.path.getsize(arfi_reservas) > 0:
                    arlo_reservas.seek(0,0)
                    fin_reservas = False
                    while arlo_reservas.tell() < os.path.getsize(arfi_reservas) and not fin_reservas:
                        reserva = pickle.load(arlo_reservas)
                        if reserva.cod_vuelo.strip() == codigo_vuelo and reserva.estado_reserva == "confirmada":
                            tiene_reservas == True
                            fin_reservas = True

    return en_uso, tiene_reservas


 

 
def busqueda_secuencial_aerolinea_nombre(nom):
    arlo_aerolineas.seek(0,0)
    cant_registros = calcular_cant_registros(arfi_aerolineas, arlo_aerolineas)
    if cant_registros != 0:
        arlo_aerolineas.seek(0,0)
        i = 1
        registro = aerolinea()
        registro = pickle.load(arlo_aerolineas)
        while registro.nombre_aerolinea.strip() != nom and i < cant_registros:
            i = i+1
            registro = pickle.load(arlo_aerolineas)
        if registro.nombre_aerolinea.strip() == nom:
            return i-1
        else:
            return -1
    else:
        return -1
    
    
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


def ver_vuelos():
    global ASIENTOS_POR_AVION
    print("\n") 
    print("="*130)
    print("LISTADO DE VUELOS DISPONIBLES EN EL SISTEMA".center(110))
    print("="*130)
    print("\n")
    print("CÓDIGO   AEROLÍNEA                    ORIGEN           DESTINO        FECHA        HORA     PRECIO        ESTADO")
    print("-"*130)
    fecha_actual = datetime.today()
    i = 1
    cont = 0
    reg_vuelo = vuelo()
    reg_aerolinea = aerolinea()
    cant_vuelos = calcular_cant_registros(arfi_vuelos, arlo_vuelos)
    arlo_vuelos.seek(0,0)
    tam_reg_aerolinea = calcular_tamanio_registro(arfi_aerolineas, arlo_aerolineas)
    while i <= cant_vuelos:
        reg_vuelo = pickle.load(arlo_vuelos)
        if reg_vuelo.estado_vuelo == "A":
            fecha_vuelo = datetime.strptime(reg_vuelo.fecha_salida, "%d/%m/%Y")
            if fecha_vuelo > fecha_actual:
                cont = cont + 1   
                cod_aerolinea = reg_vuelo.cod_aerolinea.strip()
                pos_aerolinea = busqueda_secuencial_aerolinea_cod(cod_aerolinea)
                arlo_aerolineas.seek(tam_reg_aerolinea*pos_aerolinea,0)
                reg_aerolinea = pickle.load(arlo_aerolineas)
                cantidad_asientos = 0
                for j in range(int(ASIENTOS_POR_AVION/6)):
                    for k in range(3): #lectura hasta pasillo
                        if reg_vuelo.asientos_vuelo[j][k] == "L":
                            cantidad_asientos = cantidad_asientos + 1
                    for k in range(4,7): #lectura dsp pasillo
                        if reg_vuelo.asientos_vuelo[j][k] == "L":
                            cantidad_asientos = cantidad_asientos + 1
                print(f"{reg_vuelo.cod_vuelo:<8}{reg_aerolinea.nombre_aerolinea.strip():<30}{reg_vuelo.origen_vuelo.strip():<16}{reg_vuelo.destino_vuelo.strip():<16}{reg_vuelo.fecha_salida:<12}{reg_vuelo.hora_salida:<10}${reg_vuelo.precio_vuelo:<15}{reg_vuelo.estado_vuelo:<8}") 
               
        i += 1
    print("-"*130)
    print(f"Total de vuelos: {cont}")
    volver()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def listarAerolineas():
    global arlo_aerolineas
    global arfi_aerolineas
    registro = aerolinea()
    if os.path.getsize(arfi_aerolineas) == 0:
        print("No hay aerolíneas registradas.")
        return
    arlo_aerolineas.seek(0, 0)
    print("================ AEROLINEAS ACTIVAS ==================")
    print("\nCÓDIGO   NOMBRE    CÓD-IATA     PAIS    DESCRIPCIÓN")
    print("======================================================")
    while arlo_aerolineas.tell() < os.path.getsize(arfi_aerolineas):
        registro = pickle.load(arlo_aerolineas)
        if registro.baja == "N":
            print(f"{registro.cod_aerolinea:<8}{registro.nombre_aerolinea.strip():<13}{registro.cod_IATA.strip():<13}{registro.cod_pais.strip():<8}{registro.descripcion_aerolinea.strip():<30}")


def eliminar_aero():
    global arfi_aerolineas
    global arlo_aerolineas
    registro = aerolinea()

    if os.path.getsize(arfi_aerolineas) == 0:
        print("Archivo vacio. No hay aerolineas cargadas")
        return

    cod = input("Ingrese código de aerolínea a eliminar ('*' para salir): ")
    while cod != "*" :
        arlo_aerolineas.seek(0, 0)
        while arlo_aerolineas.tell() < os.path.getsize(arfi_aerolineas):
            p = arlo_aerolineas.tell() #se guarda la pos actual antes de leer
            registro = pickle.load(arlo_aerolineas) #leemos un reg (aerolinea)

            if registro.cod_aerolinea.rstrip() == cod:
                if registro.baja == "N" : #si la aero esta activa 
                    en_uso, con_reservas =  aero_en_uso_y_con_reservas(cod)
                    if not en_uso:
                        print("la aerolinea no tiene vuelos cargados, puede darse de baja") #se puede eliminar
                        opc = input("seguro que quiere eliminar la aerolinea, (S/N) : ")
                        opc = opc.upper()
                        while opc != 'S' and opc != 'N':
                            opc = input("opcion invalida, por favor seleccione S o N: ")
                            opc = opc.upper()
                        if opc == 'S':
                            registro.baja = "S" #se dio de baja la aerolinea
                            arlo_aerolineas.seek(p,0)
                            pickle.dump(registro, arlo_aerolineas)
                            arlo_aerolineas.flush()   
                            print("✅ Aerolinea eliminada.")
                    elif not con_reservas:
                        print("la aerolinea tiene vuelos, pero sin reservas confirmadas") # tmb se puede eliminar
                        opc = input("seguro que quiere eliminar la aerolinea, (S/N) : ")
                        opc = opc.upper()
                        while opc != 'S' and opc != 'N':
                            opc = input("opcion invalida, por favor seleccione S o N: ")
                            opc = opc.upper()
                        if opc == 'S':
                            registro.baja = "S" #se dio de baja la aerolinea
                            arlo_aerolineas.seek(p,0)
                            pickle.dump(registro, arlo_aerolineas)
                            arlo_aerolineas.flush()   
                            print("✅ Aerolinea eliminada.")
                    else:
                        print("la aerolinea tiene vuelos y reservas confirmadas, No se puede eliminar") #no se puede eliminar
                    
                else: 
                    print("La aerolinea ya se encuentra eliminada")

        cod = input("Ingrese código de aerolínea a eliminar ('*' para salir): ")
    
    listarAerolineas()
    volver()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def modificar_aereo(): 
    global arfi_aerolineas
    global arlo_aerolineas
    registro = aerolinea()

    if os.path.getsize(arfi_aerolineas) == 0:
        input("Archivo vacio. No hay aerolineas cargadas")
    else:
        cod = input("Ingrese código de aerolínea a modificar ('*' para salir): ")
        while cod != "*" :
            arlo_aerolineas.seek(0, 0)
            pos = busqueda_secuencial_aerolinea_cod(cod)
            registro = aerolinea()
            if pos != -1:
                tamReg = calcular_tamanio_registro(arfi_aerolineas, arlo_aerolineas)
                arlo_aerolineas.seek(pos*tamReg, 0)
                registro = pickle.load(arlo_aerolineas)
                if registro.baja == "N":
                    os.system('cls')
                    print(f"Aerolínea actual:\nCódigo: {registro.cod_aerolinea}\nNombre: {registro.nombre_aerolinea}\nCódigo IATA: {registro.cod_IATA}\nDescripción: {registro.descripcion_aerolinea}\nPaís: {registro.cod_pais}")
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
                    match opcion:
                        case 1:
                            nuevo_nombre = str(input("Ingrese el nuevo nombre (max. 100 caracteres): "))
                            while len(nuevo_nombre) > 100:
                                print("solo 100 caracteres")
                                nuevo_nombre = str(input("Ingrese el nuevo nombre (max. 100 caracteres): "))
                            if len(nuevo_nombre) < 100:
                                registro.nombre_aerolinea = nuevo_nombre.ljust(100, " ")
                        case 2:
                            nuevo_iata = pedir_codigo_IATA()
                            registro.cod_IATA = nuevo_iata.ljust(3, " ")
                        case 3:
                            nueva_descripcion = str(input("Ingrese la nueva descripción (max. 200 caracteres): "))
                            while len(nueva_descripcion) > 200:
                                print("solo 200 caracteres")
                                nueva_descripcion = str(input("Ingrese la nueva descripción (max. 200 caracteres): "))
                            if len(nueva_descripcion) < 200:
                                registro.descripcion_aerolinea = nueva_descripcion.ljust(200, " ")
                        case 4:
                            nuevo_pais = pedir_codigo_pais()
                            registro.cod_pais = nuevo_pais.ljust(3, " ")
                        case 5:
                            volver()
                    if  opcion != 5 and opcion != " ":
                        arlo_aerolineas.seek(pos*tamReg, 0)
                        pickle.dump(registro, arlo_aerolineas)
                        arlo_aerolineas.flush()   
                        input("✅ Modificación realizada (o cancelada). Presione Enter para continuar...")
                os.system('cls')
            cod = input("Ingrese código de aerolínea a modificar ('*' para salir): ")

    os.system('cls')
    volver()
#-------------------------------------------------------------------------------------------------------------------------
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
        print("El código debe tener como mínimo 1 caracter y como máximo 5 caracteres")
        codigo = input("Ingrese código de la aerolinea: ")
    return codigo

#----------------------------------------------------------------------------------------------------------------------------------------------------------

def crear_aereo():
    registro = aerolinea()
 
    nombre = input('Ingrese el nombre de la aerolínea (max 100 caracteres). Presione enter para salir\n')
    while len(nombre) > 100:
        print("solo 100 caracteres")
        nombre = input('Ingrese el nombre de la aerolínea (max 100 caracteres). Presione enter para salir\n')

    while nombre != "":
        pos = busqueda_secuencial_aerolinea_nombre(nombre)

        while pos != -1 and nombre != "": 
            print("\n Este Nombre de aerolinea ya existe. Intente con otro. ")
            nombre = input('Ingrese el nombre de la aerolínea (max 100 caracteres). Presione enter para salir\n')
            while len(nombre) > 100:
                print("solo 100 caracteres")
                nombre = input('Ingrese el nombre de la aerolínea (max 100 caracteres). Presione enter para salir\n')
            pos = busqueda_secuencial_aerolinea_nombre(nombre)

        if nombre != "":
            nro = -2
            while nro != -1:
                codigo = pedir_codigo_aerolinea()
                nro = busqueda_secuencial_aerolinea_cod(codigo) 
                if nro != -1:
                    print("Ese código de aerolínea ya existe. Intente con otro.")
            arlo_aerolineas.seek(0,2)
            registro.nombre_aerolinea = nombre.ljust(100, " ")
            cod_aero = codigo
            registro.cod_aerolinea = cod_aero.ljust(5, " ")
            cod_iata = pedir_codigo_IATA()
            registro.cod_IATA = cod_iata.ljust(3, " ")
            codigo_pais =  pedir_codigo_pais()
            registro.cod_pais = codigo_pais.ljust(3, " ")
            desc = input("Ingrese la descripcion de la aerolinea: ")
            registro.descripcion_aerolinea = desc.ljust(200, " ")
            registro.baja = "N" # DADO DE BAJA? N-NO/S-SI

            arlo_aerolineas.seek(0,2)
            pickle.dump(registro, arlo_aerolineas)
            arlo_aerolineas.flush()
            print(f">> Aerolínea creada >>")

            nombre = input('Ingrese el nombre de la aerolínea. Presione enter para salir\n')
            pos = busqueda_secuencial_aerolinea_nombre(nombre)

    listarAerolineas()
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
                eliminar_aero()
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
    
    


def validar_entero_2():
    opc_input = input("\nSeleccione una opción valida: ")
    if opc_input == "*" :
        return "*"
    else:
       if  opc_input.isdigit():
           return(int(opc_input))
       else:
            return -1


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
                print("⚠️  El precio no puede ser negativo.")
        except:
            print("⚠️  Precio inválido. Ingrese solo números.")
    return precio
            
def eliminar_vuelo():
    
    resv = reserva()
    registro = vuelo()
    os.system('cls')
    cod_vu = -3
    while cod_vu != "*" :
        print(f"ingrese el codigo del vuelo que quiere eliminar, * para salir ")
        cod_vu = validar_entero_2()
       
        while cod_vu != "*" and cod_vu == -1:
            os.system('cls')
            print("⚠️  codigo de vuelo invalido, * para salir")
            cod_vu = validar_entero_2()
        
        if cod_vu != "*" :
            cant_reg = calcular_cant_registros(arfi_vuelos, arlo_vuelos)

            if cod_vu < cant_reg and cod_vu != "*" :
                arlo_vuelos.seek(0, 0)
                tam_reg = calcular_tamanio_registro(arfi_vuelos, arlo_vuelos)
                pos = tam_reg * cod_vu
                arlo_vuelos.seek(pos, 0)
                registro = pickle.load(arlo_vuelos)
                
                if registro.estado_vuelo == "A":
                    
                    estado = "confirmada"
                    reservado = busqueda_secuencial_reservas(arfi_reservas, arlo_reservas, cod_vu, estado)
                    if reservado == -1 :
                        
                        opc = input("seguro que quiere eliminar el vuelo, (S/N) : ")
                        opc = opc.upper()
                        while opc != 'S' and opc != 'N':
                            opc = input("opcion invalida, poravor seleccione S o N: ")
                            opc = opc.upper()
                        
                        if opc == 'S':
                            registro.estado_vuelo = "B"
                            arlo_vuelos.seek(pos, 0)
                            pickle.dump(registro, arlo_vuelos)
                            arlo_vuelos.flush()
                            input("se ha eliminado el vuelo, enter para continuar")
                              
                        else:
                            input("no se ha eliminado el vuelo, presione enter para volver.")
                     
                    else:
                        input("no se puede eliminar el vuelo porque tiene reservas confirmadas, presione enter para continuar. ")
                               
                else:
                    input("ese vuelo ya fue eliminado, presione enter para volver.")
                     
            else:
                input("no se ha creado un vuelo con ese codigo aun, enter para volver. ")
                
        os.system('cls')       
            


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
    
    registro = vuelo()
    os.system('cls')
    cod_vu = -3
    while cod_vu != "*" :
        os.system('cls')
        print(f"ingrese el codigo del vuelo que quiere modificar, * para salir ")
        cod_vu = validar_entero_2()
       
        while cod_vu != "*" and cod_vu == -1:
            os.system('cls')
            print("⚠️  codigo de vuelo invalido, * para salir")
            cod_vu = validar_entero_2()
        
        if cod_vu != "*" :
            cant_reg = calcular_cant_registros(arfi_vuelos, arlo_vuelos)
            if cod_vu < cant_reg and cod_vu != "*" :
                
                arlo_vuelos.seek(0, 0)
                tam_reg = calcular_tamanio_registro(arfi_vuelos, arlo_vuelos)
                pos = tam_reg * cod_vu
                arlo_vuelos.seek(pos, 0)
                registro = pickle.load(arlo_vuelos) 
                
                if registro.estado_vuelo == "A" :
                   puede_modificar = True 
                   
                elif registro.estado_vuelo == "B" :
                    os.system('cls')
                    print("✈️  VUELO EN ESTADO INACTIVO.")
                    opc = input("¿Desea cambiar el estado de su vuelo? (S/N): ").upper()
                    while opc != 'S' and opc != 'N':
                        opc = input("porfavor ingrese 'S' o 'N': " ).upper()
                    if opc == 'S' :
                        registro.estado_vuelo = "A"
                        arlo_vuelos.seek(pos, 0)
                        pickle.dump(registro, arlo_vuelos)
                        arlo_vuelos.flush()
                        puede_modificar = True
                    else:
                        input("no se puede modificar un vuelo dado de baja.")
                
                if puede_modificar:  
                    opc2 = 0
                    while opc2 != 7:
                        
                        os.system('cls')
                        print("\n✈️  VUELO EN ESTADO ACTIVO:")
                        print("1) Codigo aerolinea:", registro.cod_aerolinea)
                        print("2) Origen:", registro.origen_vuelo)
                        print("3) Destino:", registro.destino_vuelo)
                        print("4) Fecha salida:", registro.fecha_salida)
                        print("5) Hora salida:", registro.hora_salida)
                        print("6) Precio: $", registro.precio_vuelo) 
                        print("7) salir") 
                         
                        opc2 = validar_entero()
                        while opc2 < 1 and opc2 > 7:
                            print("⚠️  Opción no válida. Inténtelo nuevamente.")
                            opc2 = validar_entero()
                        
                        match opc2:
                            case 1:
                                existe = -1
                                while existe == -1:
                                    os.system('cls')
                                    nuevo_cod_aero = input("ingrese el nuevo codigo de aerolinea: ")
                                    existe = busqueda_secuencial_aerolinea_cod(nuevo_cod_aero)
                                     
                                registro.cod_aerolinea = nuevo_cod_aero.ljust(5, " ") 
                            case 2:  
                                os.system('cls')           
                                nuevo_origen =  input("ingrese el nuevo origen: ")  
                                while len(nuevo_origen) > 50:
                                   nuevo_origen = input("por favor no mas de 50 caracteres, ingrese el origen nuevamente: ")
                                   
                                registro.origen_vuelo = nuevo_origen.ljust(50, " ")
                            case 3:
                                os.system('cls')
                                nuevo_destino = input("ingrese el nuevo destino: ")
                                while len(nuevo_destino) > 50:
                                   nuevo_destino = input("por favor no mas de 50 caracteres, ingrese el destino nuevamente: ")
                                
                                registro.destino_vuelo = nuevo_destino.ljust(50, " ")
                            case 4:
                                os.system('cls')
                                nueva_fecha = validar_fecha()
                                registro.fecha_salida = nueva_fecha.ljust(10, " ")
                            case 5:
                                os.system('cls')
                                nueva_hora = validar_hora()
                                registro.hora_salida = nueva_hora.ljust(5, " ")
                            case 6:
                                os.system('cls')
                                nuevo_precio = validar_precio()
                                registro.precio_vuelo = nuevo_precio
                            case 7:
                                os.system('cls')
                                volver() 
                                 
                        if  opc2 != 7 and opc2 != " ":
                            arlo_vuelos.seek(pos, 0)
                            pickle.dump(registro, arlo_vuelos)
                            arlo_vuelos.flush()
                            input("✅ Modificación realizada, enter para continuar ")
            else:
                input("no hay vuelos creados con ese codigo.")
        else:
            volver()    
    os.system('cls')        
    

    
def crear_vuelo():
    
    registro = vuelo()
    cod_aero = ' '
    
    while cod_aero != '*':
        os.system('cls')
        cod_aero = input("ingrese el codigo de la aerolinea, * para salir: ")
        pos = busqueda_secuencial_aerolinea_cod(cod_aero)
        
        while pos == -1 and cod_aero != '*':
            os.system('cls')
            cod_aero = input("el codigo de aerolinea no existe, ingrese uno valido o * para salir:")
            pos = busqueda_secuencial_aerolinea_cod(cod_aero)
            
        if cod_aero != '*':
            
            arlo_vuelos.seek(0, 2)
            registro.cod_aerolinea = cod_aero.ljust(5, " ")
            cod_vu = calcular_cant_registros(arfi_vuelos, arlo_vuelos)
            registro.cod_vuelo = cod_vu
            origen = input("ingrese el origen del vuelo: ")
            while len(origen) > 50:
                origen =input("por favor no mas de 50 caracteres, ingrese el origen nuevamente: ")  
            origen = origen.upper()             
            registro.origen_vuelo = origen.ljust(50, " ")
            destino = input("ingrese el destino del vuelo: ")
            while len(destino) > 50:
                destino = input("por favor no mas de 50 caracteres, ingrese el destino nuevamente: ")
            destino = destino.upper() 
            registro.destino_vuelo = destino.ljust(50, " ")
            fecha = pedir_fecha_valida() 
            registro.fecha_salida = fecha.ljust(10, " ") 
            hora = validar_hora()
            registro.hora_salida = hora.ljust(5, " ")
            precio = validar_precio()
            registro.precio_vuelo = precio
            for i in range(40):
              for k in range(3):
                  registro.asientos_vuelo[i][k] = 'L'
              for k in range(4,7): 
                  registro.asientos_vuelo[i][k] = 'L'
            registro.estado_vuelo = "A"
            arlo_vuelos.seek(0,2)
            pickle.dump(registro, arlo_vuelos)
            arlo_vuelos.flush()
            input("vuelo creado con exito, enter para continuar")
        else :         
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
            ver_vuelos()

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

def ver_historial_compras():
    continuar = "S"
    while continuar.upper() == "S":
        email = input("Ingrese su email de usuario: ").ljust(100, " ")
        pos_usuario = busqueda_secuencial_usuario(arfi_usuarios, arlo_usuarios, email)

        if pos_usuario == -1:
            print("⚠️ Usuario no encontrado.")
        else:
            tam_reg_usuario = calcular_tamanio_registro(arfi_usuarios, arlo_usuarios)
            arlo_usuarios.seek(tam_reg_usuario * pos_usuario, 0)
            reg_usuario = pickle.load(arlo_usuarios)
            cod_usuario = reg_usuario.cod_usuario

            print("\n====== HISTORIAL DE COMPRAS ======\n")
            print("CodReserva | CodVuelo | Fecha Reserva |     Origen ===> Destino     |    Fecha    | Hora | Precio")
            print("-"*95)

            cant_reservas = calcular_cant_registros(arfi_reservas, arlo_reservas)
            arlo_reservas.seek(0, 0)

            for i in range(cant_reservas):
                reg_reserva = pickle.load(arlo_reservas)
                if (reg_reserva.cod_usuario == cod_usuario and
                    reg_reserva.estado_reserva.strip() == "confirmada"):

                    # Buscar vuelo
                    tam_reg_vuelo = calcular_tamanio_registro(arfi_vuelos, arlo_vuelos)
                    arlo_vuelos.seek(tam_reg_vuelo * reg_reserva.cod_vuelo, 0)
                    reg_vuelo = pickle.load(arlo_vuelos)

                    print(f"{reg_reserva.cod_reserva:<12} "
                          f"{reg_vuelo.cod_vuelo:<10} "
                          f"{reg_reserva.fecha_reserva:<22} "
                          f"{reg_vuelo.origen_vuelo.strip()} ===> {reg_vuelo.destino_vuelo.strip():<10} "
                          f"{reg_vuelo.fecha_salida:<13}"
                          f"{reg_vuelo.hora_salida:<5} "
                          f"${reg_vuelo.precio_vuelo}")
            print("-"*95)
            print("Fin del historial.")  
        continuar = " "
        while continuar.upper() !="S" and continuar.upper() !="N":
            continuar = input("Desea continuar? S/N\n")
    volver()

def cancelar_reserva():
    continuar = "S"
    while continuar.upper() == "S":
        print("Ingrese un codigo de reserva")
        cod_reserva = validar_entero()
        while cod_reserva == -1:
            print("⚠️  Opción no válida. Debe ser un número entero. Inténtelo nuevamente.")
            cod_reserva = validar_entero()
        cod_reserva = int(cod_reserva)
        tam_arc = os.path.getsize(arfi_reservas)
        tam_reg = calcular_tamanio_registro(arfi_reservas, arlo_reservas)
        if cod_reserva*tam_reg >= tam_arc or tam_arc == -1:
            print("⚠️  No existe una reserva con ese código.")
        else:
            reg_reserva = reserva()
            arlo_reservas.seek(cod_reserva*tam_reg, 0)
            reg_reserva = pickle.load(arlo_reservas)
            cod_vuelo = reg_reserva.cod_vuelo
            tam_reg_vuelo = calcular_tamanio_registro(arfi_vuelos, arlo_vuelos)
            arlo_vuelos.seek(cod_vuelo * tam_reg_vuelo, 0)
            reg_vuelo = pickle.load(arlo_vuelos)
            dt_salida = datetime.strptime(f"{reg_vuelo.fecha_salida} {reg_vuelo.hora_salida}","%d/%m/%Y %H:%M")
            ahora = datetime.today()
            diferencia = dt_salida - ahora
            diferencia_horas = diferencia.days * 24 + diferencia.seconds / 3600  
            print("Horas hasta salida:", diferencia_horas)
            
            if diferencia_horas < 72:
                print("⚠️ No se puede cancelar. Hay menos de 72 horas faltantes para el vuelo")
            else:
                asiento_str = reg_reserva.nro_asiento.strip()   
                partes = asiento_str.split("-")     
                fila = int(partes[0])               
                columna = int(partes[1])            
                if columna <= 3:
                    col_real = columna - 1
                else:
                    col_real = columna
                fila_real = fila - 1
                reg_vuelo.asientos_vuelo[fila_real][col_real] ="L"
                arlo_vuelos.seek(tam_reg_vuelo*(cod_vuelo), 0)
                pickle.dump(reg_vuelo, arlo_vuelos)
                arlo_vuelos.flush()
                reg_reserva.fecha_reserva = ahora.strftime("%d/%m/%Y")
                reg_reserva.estado_reserva = "cancelada".ljust(20, " ")
                arlo_reservas.seek(cod_reserva*tam_reg, 0)
                pickle.dump(reg_reserva, arlo_reservas)
                arlo_reservas.flush()
                print("Reserva cancelada correctamente")
        continuar = " "
        while continuar.upper() !="S" and continuar.upper() !="N":
            continuar = input("Desea continuar? S/N\n")
    volver()
    
    
def consultar_reservas():
    continuar = "S"
    while continuar.upper() == "S":
        print("Ingrese un codigo de reserva")
        cod_reserva = validar_entero()
        while cod_reserva == -1:
            print("⚠️  Opción no válida. Debe ser un número entero. Inténtelo nuevamente.")
            cod_reserva = validar_entero()
        cod_reserva = int(cod_reserva)
        
        tam_arc = os.path.getsize(arfi_reservas)
        tam_reg = calcular_tamanio_registro(arfi_reservas, arlo_reservas)
        if cod_reserva*tam_reg >= tam_arc or tam_reg == -1:
            print("⚠️  No existe una reserva con ese código.")
        else:
            reg_reserva = reserva()
            arlo_reservas.seek(cod_reserva*tam_reg, 0)
            reg_reserva = pickle.load(arlo_reservas)
            print("\n====== INFORMACIÓN DE LA RESERVA ======")
            print(f"Código de reserva: {reg_reserva.cod_reserva}")
            print(f"Código de usuario: {reg_reserva.cod_usuario}")
            print(f"Código de vuelo:   {reg_reserva.cod_vuelo}")
            print(f"Nro de asiento:    {reg_reserva.nro_asiento.strip()}")
            print(f"Fecha reserva:     {reg_reserva.fecha_reserva}")
            print(f"Estado:            {reg_reserva.estado_reserva.strip()}")
            print("=======================================\n")

        continuar = " "
        while continuar.upper() !="S" and continuar.upper() !="N":
            continuar = input("Desea continuar? S/N\n")

    volver()
    
    
def reservar_vuelos():
    global logged_user
    reg_reserva = reserva()
    continuar = "S"
    while continuar =="S":
        print("Ingrese el codigo del vuelo que desea")
        cod_vuelo = validar_entero()
        while cod_vuelo ==-1:
            print("⚠️   Opción no válida. Debe ser un numero entero. Inténtelo nuevamente.")
            cod_vuelo = validar_entero()
        cod_vuelo = int(cod_vuelo)
        vuelo_valido = validar_vigencia(cod_vuelo)
        if vuelo_valido:
            tam_reg_vuelo = calcular_tamanio_registro(arfi_vuelos,arlo_vuelos)
            arlo_vuelos.seek(tam_reg_vuelo*cod_vuelo, 0)
            reg_vuelo = pickle.load(arlo_vuelos)
            asientos_disponibles = False
            j = 0 
            i=0
            while i < 40 and not asientos_disponibles:  # recorre filas
                    j = 0
                    while j < 7 and not asientos_disponibles:  # recorre columnas
                        if reg_vuelo.asientos_vuelo[i][j] == "L":  # asiento libre y no pasillo
                            asientos_disponibles = True
                        else:
                            j += 1
                    if not asientos_disponibles:
                        i += 1        
            if asientos_disponibles:
                continuar_seleccion = "S"
                while continuar_seleccion.upper( )== "S":
                    print("Ingrese un numero de fila (1-40)")
                    fila = validar_entero()
                    while fila == -1 or fila>40 or fila<1:
                        print("⚠️   Opción no válida. Debe ser un numero entero entre 1 y 40. Inténtelo nuevamente.")
                        fila = validar_entero()
                    fila_real = fila-1
                    print("Ingrese un numero de columna (1-6)")
                    columna = validar_entero()
                    while columna == -1 or columna<1 or columna>6:
                        print("⚠️   Opción no válida. Debe ser un numero entero entre 1 y 6. Inténtelo nuevamente.")
                        columna = validar_entero()
                    if columna <= 3:
                        col_real = columna - 1
                    else:
                        col_real = columna
                    fila = str(fila)
                    columna = str(columna)
                    asiento = (fila + "-" + columna)
                    asiento = asiento.ljust(4," ")
                    if reg_vuelo.asientos_vuelo[fila_real][col_real] == "L":
                        reg_vuelo.asientos_vuelo[fila_real][col_real] ="R"
                        arlo_vuelos.seek(tam_reg_vuelo*(cod_vuelo), 0)
                        pickle.dump(reg_vuelo, arlo_vuelos)
                        arlo_vuelos.flush()
                        continuar_seleccion = "N"
                        print("Se reservo correctamente el asiento\n")
                        reg_reserva.cod_reserva = int(calcular_cant_registros(arfi_reservas, arlo_reservas))
                        reg_reserva.cod_usuario = logged_user.cod_usuario
                        reg_reserva.cod_vuelo = reg_vuelo.cod_vuelo
                        reg_reserva.estado_reserva = "confirmada".ljust(20, " ")
                        reg_reserva.nro_asiento = asiento
                        hoy = datetime.today()
                        reg_reserva.fecha_reserva = hoy.strftime("%d/%m/%Y")
                        arlo_reservas.seek(0,2)
                        pickle.dump(reg_reserva,arlo_reservas)
                        arlo_reservas.flush()
                        continuar = " "
                        while continuar.upper() !="S" and continuar.upper() !="N":
                            continuar = input(f"Desea reservar otro vuelo? S/N")
                    else:
                        continuar_seleccion = " "
                        while continuar_seleccion.upper() !="S" and continuar_seleccion.upper() !="N":
                            continuar_seleccion = input(f"No se encuentra disponible. Desea intentar con otro asiento? S/N (hint: {i-j})")
            else:
                print("No hay asientos disponibles")
                continuar = " "
                while continuar.upper() !="S" and continuar.upper() !="N":
                    continuar = input("Desea intentar con otro vuelo? S/N\n")
            
        elif not vuelo_valido:
            print("No existe un vuelo vigente con ese codigo")
            continuar = " "
            while continuar.upper() !="S" and continuar.upper() !="N":
                continuar = input("Desea intentar con otro vuelo? S/N\n")
    volver()
        
        

def mostrar_menu_reservas():
    print("╔════════════════════════════════════════╗")
    print("║  📆  MENÚ DE GESTION DE RESERVAS 📆    ║")
    print("╚════════════════════════════════════════╝\n")
    print("1) Reservar Vuelo 🛩️") 
    print("2) Consultar Reservas📆")
    print("3) Cancelar Reservas❌")
    print("4) Volver al Menú Principal 🔙") 

def gestionar_reservas():
    opc = -1
    while opc != 4:
        mostrar_menu_reservas()
        opc = validar_entero()
        os.system('cls' if os.name == 'nt' else 'clear')
        while opc < 1 or opc > 4:
            print("⚠️   Opción no válida. Inténtelo nuevamente.\n")
            mostrar_menu_reservas()
            opc = validar_entero()
            os.system('cls' if os.name == 'nt' else 'clear')
        match opc: 
            case 1:
                reservar_vuelos()
            case 2:
                consultar_reservas()
            case 3:
                cancelar_reserva()
            case 4:
                volver()
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_asientos(cod_vuelo):
    global ASIENTOS_POR_AVION
    print("  A      B     C            D     E     F")
    print("+-----+-----+-----+      +-----+-----+-----+")
    tam_reg = calcular_tamanio_registro(arfi_vuelos, arlo_vuelos)
    posicion_en_archivo = tam_reg*cod_vuelo
    arlo_vuelos.seek(posicion_en_archivo, 0)
    reg_vuelo = pickle.load(arlo_vuelos)
    for i in range(0, int(ASIENTOS_POR_AVION/6)):
        print(" ", end="")
        for k in range(3):
            print("|",reg_vuelo.asientos_vuelo[i][k],"|", end=" ")
        print("       ", end="")
        for k in range(4,7):
            print("|",reg_vuelo.asientos_vuelo[i][k],"|", end=" ")
        print("    ",i+1)
        print()

def validar_vigencia(cod_vuelo):
    vigente = False
    cantidad_vuelos = calcular_cant_registros(arfi_vuelos, arlo_vuelos)
    if cod_vuelo >= cantidad_vuelos:
        return vigente
    else:
        tam_reg = calcular_tamanio_registro(arfi_vuelos, arlo_vuelos)
        arlo_vuelos.seek(cod_vuelo*tam_reg,0)
        registro = vuelo()
        registro = pickle.load(arlo_vuelos)
        fecha_actual = datetime.today()
        if registro.estado_vuelo == "A":
            fecha_vuelo = datetime.strptime(registro.fecha_salida, "%d/%m/%Y")
            if fecha_vuelo > fecha_actual:
                vigente = True
    return vigente

def  buscar_asientos():
    continuar = "S"
    while continuar == "S":
        print(f"Ingrese el codigo del vuelo del cual quiere ver los asientos")
        cod_vuelo = validar_entero()
        os.system('cls')
        while cod_vuelo == -1:
            print(f" ⚠️  Codigo de vuelo invalido. Intentelo nuevamente")
            cod_vuelo = validar_entero()
        if validar_vigencia(cod_vuelo):
            mostrar_asientos(cod_vuelo)
        else:
            print("El vuelo no esta vigente.")
        continuar = " "
        while continuar.upper() !="S" and continuar.upper() !="N":
            continuar = input("Desea continuar? S/N\n")
        if continuar.upper() != "S":
            volver()

def ver_vuelos_limitado(fecha_desde, fecha_hasta, origen, destino):
    global ASIENTOS_POR_AVION
    print("\n") 
    print("="*120)
    print("LISTADO DE VUELOS DISPONIBLES EN EL SISTEMA".center(100))
    print("="*120)
    print("\n")
    print("CÓDIGO   AEROLÍNEA                    ORIGEN           DESTINO        FECHA        HORA     PRECIO    CANTIDAD ASIENTOS")
    print("-"*120)
    fecha_actual = datetime.today()
    i = 1
    cont = 0
    reg_vuelo = vuelo()
    reg_aerolinea = aerolinea()
    cant_vuelos = calcular_cant_registros(arfi_vuelos, arlo_vuelos)
    arlo_vuelos.seek(0,0)
    tam_reg_aerolinea = calcular_tamanio_registro(arfi_aerolineas, arlo_aerolineas)
    fecha_desde = datetime.strptime(fecha_desde, "%d/%m/%Y")
    fecha_hasta = datetime.strptime(fecha_hasta, "%d/%m/%Y")
    while i <= cant_vuelos:
        reg_vuelo = pickle.load(arlo_vuelos)
        if reg_vuelo.estado_vuelo == "A":
            fecha_vuelo = datetime.strptime(reg_vuelo.fecha_salida, "%d/%m/%Y")
            if fecha_vuelo > fecha_actual and fecha_vuelo >= fecha_desde and fecha_vuelo <= fecha_hasta:
                if reg_vuelo.origen_vuelo.strip() == origen.upper() and reg_vuelo.destino_vuelo.strip() == destino.upper():
                    cont = cont + 1   
                    cod_aerolinea = reg_vuelo.cod_aerolinea.strip()
                    pos_aerolinea = busqueda_secuencial_aerolinea_cod(cod_aerolinea)
                    arlo_aerolineas.seek(tam_reg_aerolinea*pos_aerolinea,0)
                    reg_aerolinea = pickle.load(arlo_aerolineas)
                    cantidad_asientos = 0
                    for j in range(int(ASIENTOS_POR_AVION/6)):
                        for k in range(3): #lectura hasta pasillo
                            if reg_vuelo.asientos_vuelo[j][k] == "L":
                                cantidad_asientos = cantidad_asientos + 1
                        for k in range(4,7): #lectura dsp pasillo
                            if reg_vuelo.asientos_vuelo[j][k] == "L":
                                cantidad_asientos = cantidad_asientos + 1
                    print(f"{reg_vuelo.cod_vuelo:<8}{reg_aerolinea.nombre_aerolinea.strip():<30}{reg_vuelo.origen_vuelo.strip():<16}{reg_vuelo.destino_vuelo.strip():<16}{reg_vuelo.fecha_salida:<12}{reg_vuelo.hora_salida:<10}${reg_vuelo.precio_vuelo:<15}{cantidad_asientos:<5}")        
        i += 1
    print("-"*120)
    if cont != 0:
        print(f"Total de vuelos: {cont}")
    else:
        print("NO SE ENCONTRARON VUELOS")
    volver()
    
def  buscar_vuelos():
    valida = False
    fecha_desde = input("Ingrese a partir de que fecha dd/mm/aaaa, enter para salir")
    valida = validar_fecha(fecha_desde)
    while valida != True and fecha_desde!="" :
        fecha_desde = input("Porfavor, Ingrese la fecha en formato dd/mm/aaaa")
        valida = validar_fecha(fecha_desde)
    if fecha_desde !="":
        valida=False
        fecha_hasta = input("Ingrese hasta que fecha dd/mm/aaaa")
        valida = validar_fecha(fecha_hasta)
        while valida != True :
            fecha_hasta = input("Porfavor, Ingrese la fecha en formato dd/mm/aaaa")
            valida = validar_fecha(fecha_hasta)
        origen = input("Ingrese el origen del vuelo: ").upper()
        destino = input("Ingrese el destino del vuelo: ").upper()
        os.system('cls')
        ver_vuelos_limitado(fecha_desde, fecha_hasta, origen, destino)
    else:
        os.system('cls')
        volver()
               


def  mostrar_menu_principal_usuario():
    print("╔════════════════════════════════════╗")
    print("║   👤 MENÚ PRINCIPAL USUARIO  👤    ║")
    print("╚════════════════════════════════════╝\n")
    print("1) Buscar Vuelos 🛩️")
    print("2) Buscar Asientos💺")
    print("3) Gestionar Reservas 📆")
    print("4) Ver Historial de Compras 💲")
    print("5) Ver Novedades 📑")
    print("6) Cerrar Sesión ❌")
    
def menu_usuario():
     opc = -1
     global novedades
     while opc != 6:
        mostrar_menu_principal_usuario()
        opc = validar_entero()
        os.system('cls' if os.name == 'nt' else 'clear')

        while opc < 1 or opc > 6:
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
                gestionar_reservas()
            case 4:
                ver_historial_compras()
            case 5:
                ver_arreglo_limitado_pr(novedades, "NOVEDADES DISPONIBLES", ["descripcion", "fecha inicio", "fecha fin"], " ", 0, [1,1], 100)
            case 6:
                input("Cerrando sesión...\nPresione enter para continuar")
                os.system('cls' if os.name == 'nt' else 'clear')

       
#----------------------------------------------------------------------------------------------------------------------------------





#----------------------------------------MAIN---------------------------------------------------------------------------------------------
def busqueda_secuencial_usuario(arfi, arlo, valor):
    arlo.seek(0,0)
    cant_registros = calcular_cant_registros(arfi, arlo)
    if cant_registros != 0:
        arlo.seek(0,0)
        i = 1
        registro = usuario()
        registro = pickle.load(arlo)
        while registro.email_usuario!= valor and i < cant_registros:
            i = i+1
            registro = pickle.load(arlo)
        if registro.email_usuario == valor:
            return i-1
        else:
            return -1
    else:
        return -1
        

def registrarse(arfi_usuarios, arlo_usuarios):
    registrado = False
    mail = input("\nIngrese el mail con el que quiere registrarse o * para volver: ")
    while mail != "*" and not registrado:
        while len(mail) > 100 :
            mail = input("⚠️  el mail no puede tener mas de 100 caracteres, por favor ingrese otro: ")
        mail = mail.ljust(100," ")
        posicion = busqueda_secuencial_usuario(arfi_usuarios,arlo_usuarios,mail)
        while posicion !=-1:
                print("El mail ya fue utilizado. Intentelo nuevamente con un correo distinto")
                mail = input("\nIngrese el mail con el que quiere registrarse o * para volver: ")
                if mail != "*":
                    mail = mail.ljust(100," ")
                    posicion = busqueda_secuencial_usuario(arfi_usuarios,arlo_usuarios,mail)
                else:
                    posicion = -1
        if mail != "*":
            user = usuario()
            user.email_usuario = mail
            cod = calcular_cant_registros(arfi_usuarios,arlo_usuarios)
            user.cod_usuario = cod
            clave = " "
            while len(clave)!=8:
                clave = input("Ingrese la clave de 8 caracteres: ")
            user.clave_usuario = clave
            tipo = " "
            while tipo != "ceo de aerolinea" and tipo != "usuario" :
                tipo = input("Ingrese el tipo de usuario: ")
            tipo = tipo.ljust(20, " ")
            user.tipo_usuario = tipo
            telefono=" "
            while telefono == " " or len(telefono)>100:
                telefono = input("Ingrese el telefono: ")
                telefono = telefono.ljust(100, " ")
            user.telefono_usuario = telefono
            arlo_usuarios.seek(0,2)
            pickle.dump(user, arlo_usuarios)
            arlo_usuarios.flush()
            
            registrado = True
            input("Registrado correctamente")
    os.system('cls')
        
def menu_login():
    print("╔════════════════════════════════════╗")
    print("║       🏠  INICIAR SESION  🏠       ║")
    print("╚════════════════════════════════════╝\n")
        
def login(arfi_usuarios, arlo_usuarios):
    global logged_user
    intentos = 3
    tamReg = calcular_tamanio_registro(arfi_usuarios,arlo_usuarios)
    menu_login()
    mail_usuario = input("\nIngrese su usuario (enter para volver): ")
    
    while intentos != 0 and mail_usuario!="":
        mail_usuario = mail_usuario.ljust(100, " ")
        contrasenia = pwinput.pwinput(prompt="Ingrese la contraseña: ")
        os.system('cls')
        posicion = busqueda_secuencial_usuario(arfi_usuarios,arlo_usuarios, mail_usuario)
        #posicion = busqueda_secuencial(usuarios, mail_usuario , 0)
        if posicion !=-1:
            arlo_usuarios.seek(posicion * tamReg,0)
            usuario = pickle.load(arlo_usuarios)
            if  contrasenia == usuario.clave_usuario:
                logged_user = usuario
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



#PROGRAMA PRINCIPAL



novedades = [[""] * 4 for i in range(3)] #no dice en ningun lado hasta cuantas novedades pueden ser
cargarNovedades(novedades)
ASIENTOS_POR_AVION = 240

class usuario:
    def __init__(self):
        self.cod_usuario = 0
        self.email_usuario = " "
        self.clave_usuario = " "
        self.tipo_usuario = " "
        self.telefono_usuario = " "  

class aerolinea:
    def __init__(self):
        self.cod_aerolinea = " "
        self.nombre_aerolinea = " "
        self.cod_IATA = " "
        self.descripcion_aerolinea = " "
        self.cod_pais = " "
        self.baja = " "
        
class vuelo:
    def __init__(self):
        self.cod_vuelo = 0
        self.cod_aerolinea = " "
        self.origen_vuelo = " "
        self.destino_vuelo = " "
        self.fecha_salida = " "
        self.hora_salida = " "
        self.precio_vuelo = 0.0
        self.asientos_vuelo = [[""]*7 for i in range(int(ASIENTOS_POR_AVION/6))]
        self.estado_vuelo = " "

class reserva:
    def __init__(self):
        self.cod_reserva = 0
        self.cod_usuario = 0
        self.cod_vuelo = 0
        self.fecha_reserva = 0
        self.estado_reserva = " "
        self.nro_asiento = " "
        
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
            logged_user = usuario()
            login(arfi_usuarios,arlo_usuarios)
            mostrar_primer_menu()
            opc = validar_entero()
        case 3:
            print()
print("Cerrando programa...") 


