
# STRING: us_admin, contrasenia_admin, texto_nove1, texto_nove2, texto_nove3, fecha_ini_nove1, fecha_ini_nove2, fecha_ini_nove3, fecha_fin_nove1, fecha_fin_nove2, fecha_fin_nove3, fecha, fecha_aux, codigo_pais, descripcion_aereo, nombre_aereo, codigo_mayor, codigo_menor, usuario, contrasenia
# INT: intentos, codigo_nove1, codigo_nove2, codigo_nove3, opc, nuevo_codigo, opc_novedad, opc_aspecto, mayor, menor, contador_arg, contador_bra, contador_chi, opc_input, codigo_IATA
# BOOL: fecha_valida
#uriii holaaaas

import os
from datetime import datetime
import getpass

intentos = 3

us_admin = "admin@ventaspasajes777.com"
contrasenia_admin = "admin"

codigo_nove1 = 1
texto_nove1 = "por aniversario todos los vuelos tiene un %20 de descuento con cualquier medio de pago"
fecha_ini_nove1 = "02/10/2025"
fecha_fin_nove1 = "01/11/2025"
codigo_nove2 = 2
texto_nove2 = "cambio de tarifa referente al equipaje extra en pasajes turista"
fecha_ini_nove2 = "23/06/2025"
fecha_fin_nove2 = "23/07/2025"
codigo_nove3 = 3
texto_nove3 = "los vuelos con destino a Miami seran suspendidos por fuertes tormentas y posibilidad de huracan"
fecha_ini_nove3 = "04/08/2025"
fecha_fin_nove3 = '11/08/2025'

def validar_entero():
    opc_input = input("\nSeleccione una opción valida: ")
    if opc_input.isdigit():
        return(int(opc_input))
    else:
        return -1

def pedir_fecha_valida():
    fecha_valida = False
    while not fecha_valida:
        fecha = input("Ingrese la fecha en formato dd/mm/aaaa: ")
        try:
            datetime.strptime(fecha,"%d/%m/%Y")
            fecha_valida = True
        except:
            print("Error: Fecha inexistente. Verificá los valores.\n")
    return fecha

def en_construccion():
    input("En construccion. Presione enter para continuar")
    os.system('cls')

def volver():
    input("Regresando al menu anterior. Presione enter para continuar")
    os.system('cls')

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

def ver_nov():
    print("╔═══════════════════════════════════════╗")
    print("║    📑  NOVEDADES DISPONIBLES  📑      ║")
    print("╚═══════════════════════════════════════╝\n")
    linea = "-" * 150
    print("Novedad #",codigo_nove1, "descripcion:", texto_nove1 )
    print("con fecha del", fecha_ini_nove1 ,"hasta", fecha_fin_nove1)
    print(linea)
    print("Novedad #",codigo_nove2, "Descripcion:", texto_nove2 )
    print("con fecha del", fecha_ini_nove2 ,"hasta", fecha_fin_nove2)
    print(linea)
    print("Novedad #",codigo_nove3, "descripcion:", texto_nove3 )
    print("con fecha del", fecha_ini_nove3 ,"hasta", fecha_fin_nove3)
    print(linea)
    volver()

""" def ver_nov():
    print(f"{'N°':<4} {'Codigo':<12} {'Descripcion':<100} {'Desde':<12} {'Hasta':<12}")
    linea = "-" * 150
    print(linea)
    print(f"{'1':<4} {codigo_nove1:<12} {texto_nove1:<100} {fecha_ini_nove1:<12} {fecha_ini_nove1:<12}")
    print(linea)
    print(f"{'2':<4} {codigo_nove2:<12} {texto_nove2:<100} {fecha_ini_nove2:<12} {fecha_fin_nove2:<12}")
    print(linea)
    print(f"{'3':<4} {codigo_nove3:<12} {texto_nove3:<100} {fecha_ini_nove3:<12} {fecha_fin_nove3:<12}")
    print(linea)
    print()
    input("Presione enter para continuar")
    os.system('cls') """

def validar_codigo():
    nuevo_codigo = -1
    while nuevo_codigo <0:
        nuevo_codigo = input("Ingrese el nuevo codigo (DEBE SER ENTERO POSITIVO, 0 PARA SALIR)\n")
        if nuevo_codigo.isdigit():
            nuevo_codigo = int(nuevo_codigo)
        else:
            nuevo_codigo = -1
            print("El codigo debe ser un numero entero positivo")
    os.system('cls')
    return nuevo_codigo

def mostrar_menu_editar_nov():
    print("╔══════════════════════════════════════╗")
    print("║   ✏️ EDITAR ASPECTOS DE LA NOVEDAD ✏️  ║")
    print("╚══════════════════════════════════════╝\n")
    print("1) Código 🔢")
    print("2) Descripción 📝")
    print("3) Fecha de Inicio 📅")
    print("4) Fecha de Finalización 📅")
    print("5) Volver 🔙")

def editar_nov(): #menu3_2
    global codigo_nove1, codigo_nove2, codigo_nove3, texto_nove1, texto_nove2, texto_nove3, fecha_ini_nove1, fecha_ini_nove2, fecha_ini_nove3, fecha_fin_nove1, fecha_ini_nove2, fecha_fin_nove3
    
    print("Ingrese el codigo de la novedad (0 para salir, inicializadas en 1-2-3)")
    opc_novedad = validar_entero()
    while opc_novedad !=0:

        while opc_novedad != 0 and opc_novedad != codigo_nove1 and opc_novedad != codigo_nove2 and opc_novedad !=codigo_nove3: #se hace con if anidados ya que la consigna dice "el sistema permitirá según el código de novedad ingresado poder editar los datos de la misma."
            print("⚠️   Opción no válida. Inténtelo nuevamente (0 para salir)") #se pide codigo ya que la consigna dice "segun codigo de novedad ingresado"
            opc_novedad = validar_entero()
            
        os.system('cls')
        mostrar_menu_editar_nov()
        opc_aspecto = validar_entero()
        os.system('cls')

        while opc_aspecto < 1 or opc_aspecto > 5:
            print("⚠️   Opción no válida. Inténtelo nuevamente.")
            mostrar_menu_editar_nov()
            opc_aspecto = validar_entero()
            os.system('cls')

        while opc_aspecto != 5:

            if opc_novedad == codigo_nove1:
                match opc_aspecto:                
                    case 1:
                        print("El codigo actual es:", codigo_nove1)
                        nuevo_codigo = validar_codigo()
                        if nuevo_codigo != 0:
                            codigo_nove1 = nuevo_codigo
                            opc_novedad = nuevo_codigo
                    case 2:
                        print("El texto actual es:", texto_nove1)
                        texto_nove1= input("Ingrese el nuevo texto: ")
                    case 3:
                        print("La fecha actual es:", fecha_ini_nove1)
                        fecha_aux = pedir_fecha_valida()
                        if datetime.strptime(fecha_aux,"%d/%m/%Y") <= datetime.strptime(fecha_fin_nove1,"%d/%m/%Y"):
                            fecha_ini_nove1 = fecha_aux
                        else:
                            input("⚠️   La fecha de inicio no puede venir después de la fecha de finalización. Se mantuvo la fecha original. Presione enter para continuar")
                    case 4:
                        print("La fecha actual es:", fecha_fin_nove1)
                        fecha_aux = pedir_fecha_valida()
                        if datetime.strptime(fecha_aux,"%d/%m/%Y") >= datetime.strptime(fecha_ini_nove1,"%d/%m/%Y"):
                            fecha_fin_nove1 = fecha_aux
                        else:
                            input("⚠️   La fecha de inicio no puede venir después de la fecha de finalización. Se mantuvo la fecha original. Presione enter para continuar")
            elif opc_novedad == codigo_nove2:
                match opc_aspecto:
                    case 1:
                        print("El codigo actual es:", codigo_nove2)
                        nuevo_codigo = validar_codigo()
                        if nuevo_codigo != 0:
                            codigo_nove2 = nuevo_codigo
                            opc_novedad = nuevo_codigo
                    case 2:
                        print("El texto actual es:", texto_nove2)
                        texto_nove2= input("Ingrese el nuevo texto: ")
                    case 3:
                        print("La fecha actual es:", fecha_ini_nove2)
                        fecha_aux = pedir_fecha_valida()
                        if datetime.strptime(fecha_aux,"%d/%m/%Y") <= datetime.strptime(fecha_fin_nove2,"%d/%m/%Y"):
                            fecha_ini_nove2 = fecha_aux
                        else:
                            input("⚠️   La fecha de inicio no puede venir después de la fecha de finalización. Se mantuvo la fecha original. Presione enter para continuar")
                    case 4:
                        print("La fecha actual es:", fecha_fin_nove2)
                        fecha_aux = pedir_fecha_valida()
                        if datetime.strptime(fecha_aux,"%d/%m/%Y") >= datetime.strptime(fecha_ini_nove2,"%d/%m/%Y"):
                            fecha_fin_nove2 = fecha_aux
                        else:
                            input("⚠️   La fecha de inicio no puede venir después de la fecha de finalización. Se mantuvo la fecha original. Presione enter para continuar")
            elif opc_novedad == codigo_nove3:
                match opc_aspecto:
                    case 1:
                        print("El codigo actual es:", codigo_nove3)
                        nuevo_codigo = validar_codigo()
                        if nuevo_codigo != 0:
                            codigo_nove3 = nuevo_codigo
                            opc_novedad = nuevo_codigo
                    case 2:
                        print("El texto actual es:", texto_nove3)
                        texto_nove3= input("Ingrese el nuevo texto: ")
                    case 3:
                        print("La fecha actual es:", fecha_ini_nove3)
                        fecha_aux = pedir_fecha_valida()
                        if datetime.strptime(fecha_aux,"%d/%m/%Y") <= datetime.strptime(fecha_fin_nove3,"%d/%m/%Y"):
                            fecha_ini_nove3 = fecha_aux
                        else:
                            input("⚠️   La fecha de inicio no puede venir después de la fecha de finalización. Se mantuvo la fecha original. Presione enter para continuar")
                    case 4:
                        print("La fecha actual es:", fecha_fin_nove3)
                        fecha_aux = pedir_fecha_valida()
                        if datetime.strptime(fecha_aux,"%d/%m/%Y") >= datetime.strptime(fecha_ini_nove3,"%d/%m/%Y"):
                            fecha_fin_nove3 = fecha_aux
                        else:
                            input("⚠️   La fecha de inicio no puede venir después de la fecha de finalización. Se mantuvo la fecha original. Presione enter para continuar")
            os.system('cls')
            mostrar_menu_editar_nov()
            opc_aspecto = validar_entero()
            os.system('cls')

            while opc_aspecto < 1 or opc_aspecto > 5:
                print("⚠️   Opción no válida. Inténtelo nuevamente.")
                mostrar_menu_editar_nov()
                opc_aspecto = validar_entero()
                os.system('cls')

        volver()
        print("Ingrese el codigo de la novedad (0 para salir, inicializadas en 1-2-3)")
        opc_novedad = validar_entero()
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

def menu_novedades(): #menu3
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
                ver_nov()
            case 5:
                volver()
    os.system('cls')

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

def crear_aereo():
    nombre_aereo = input('Ingrese el nombre del aereo. Ingrese 0 para salir\n')
    contador_arg = 0
    contador_chi = 0
    contador_bra = 0
    while nombre_aereo != "0":
        codigo_IATA = 1000
        while codigo_IATA > 999 or codigo_IATA < 1:
            codigo_IATA = input("\nIngrese el codigo IATA\n")
            if codigo_IATA.isdigit():
                codigo_IATA = int(codigo_IATA)
                if codigo_IATA > 999 or codigo_IATA < 1:
                    print("\nEl codigo debe ser de un maximo de 3 digitos y mayor a 0. Intentelo nuevamente.")
            else:
                print("\nEl codigo debe ser un numero entero positivo. Intentelo nuevamente.")
                codigo_IATA = 0
        descripcion_aereo = input("\nIngrese la descripcion del vuelo\n")
        codigo_pais = pedir_codigo_pais()
        match codigo_pais:
            case "ARG":
                contador_arg+=1
            case "BRA":
                contador_bra+=1
            case "CHI":
                contador_chi+=1
        os.system('cls')
        nombre_aereo = input('Ingrese el nombre del aereo. Ingrese 0 para salir\n')
        
    if contador_arg == contador_chi == contador_bra:
        print("Los tres codigos (ARG, CHI y BRA) tienen la misma cantidad de aerolineas cargadas:", contador_arg)
        print("")
    else:
        mayor = contador_arg
        codigo_mayor = "ARG"
        menor = contador_arg
        codigo_menor = "ARG"
        
        if contador_bra > mayor:
            mayor = contador_bra
            codigo_mayor = "BRA"
        elif contador_bra < menor:
            menor = contador_bra
            codigo_menor = "BRA"        
        
        if contador_chi > mayor:
            mayor = contador_chi
            codigo_mayor = "CHI"
        else:
            menor = contador_chi
            codigo_menor = "CHI"
            
        print("")
        print("Mayor:", codigo_mayor,"con una cantidad de aerolineas cargadas de", mayor)
        print("Menor:", codigo_menor, "con una cantidad de aerolineas cargada de", menor)
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
                en_construccion()
            case 3:
                en_construccion()
            case 4:
                volver()

def mostrar_menu_principal():
    print("╔════════════════════════════════════╗")
    print("║      🏠  MENÚ PRINCIPAL  🏠        ║")
    print("╚════════════════════════════════════╝\n")
    print("1) Gestión de Aerolíneas 🛩️")
    print("2) Aprobar / Denegar Promociones💲")
    print("3) Gestión de Novedades 📆")
    print("4) Mostrar Reportes 📊")
    print("5) Salir del Programa ❌")

def menu_principal():
    opc = -1
    while opc != 5:
        mostrar_menu_principal()
        opc = validar_entero()
        os.system('cls')
        while opc < 1 or opc > 5:
            print("⚠️   Opción no válida. Inténtelo nuevamente.\n")
            mostrar_menu_principal()
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
                os.system('cls') #se borra la consola ya que la consigna dice que con salir se abandona el sistema

while intentos != 0:
    usuario = (input("Ingrese su usuario: "))
    contrasenia = getpass.getpass(prompt="Ingrese la contraseña: ")
    os.system('cls')
    if usuario == us_admin and contrasenia == contrasenia_admin: 
            intentos = 0 #se pone el intentos 0 para despues forzar a que se cierre el programa al cerrar cesion (segun consigna)
            menu_principal()
    else:
        intentos = intentos - 1
        if intentos == 0: 
            print("\nHubieron 3 intentos fallidos. Por medidas de seguridad se cerrara el programa\n")
        else:
            print ("\nContraseña o usuario incorrectas, le quedan", intentos,"intentos\n" )
print("Se ha cerrado el programa")
