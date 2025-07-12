
# STRING: us_admin, contrasenia_admin, texto_nove1, texto_nove2, texto_nove3, fecha_ini_nove1, fecha_ini_nove2, fecha_ini_nove3, fecha_fin_nove1, fecha_fin_nove2, fecha_fin_nove3, fecha, fecha_aux, codigo_pais, descripcion_aereo, nombre_aereo, codigo_mayor, codigo_menor, usuario, contrasenia
# INT: intentos, codigo_nove1, codigo_nove2, codigo_nove3, opc, nuevo_codigo, opc_novedad, opc_aspecto, mayor, menor, contador_arg, contador_bra, contador_chi, opc_input, codigo_IATA
# BOOL: fecha_valida

import pwinput
import os
from datetime import datetime
import getpass


#PROCEDIMIENTOS Y FUNCIONES GENERALES

def validar_entero():
    opc_input = input("\nSeleccione una opción valida: ")
    if opc_input.isdigit():
        return(int(opc_input))
    else:
        return -1

def en_construccion():
    input("En construccion. Presione enter para continuar")
    os.system('cls')

def volver():
    input("Regresando al menu anterior. Presione enter para continuar")
    os.system('cls')
    
def add_item(arreglo, valores_fila, posicion):
    for i in range(len(valores_fila)): #[0-1-2]
        arreglo[posicion][i] = valores_fila[i]
        
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

#MENU ADMINISTRADOR

#############

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

""" def ver_nov():
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
    volver() """

def ver_novedades(novedades):
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
    return i


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

def editar_nov(novedades): #menu3_2
    global codigo_nove1, codigo_nove2, codigo_nove3, texto_nove1, texto_nove2, texto_nove3, fecha_ini_nove1, fecha_ini_nove2, fecha_ini_nove3, fecha_fin_nove1, fecha_ini_nove2, fecha_fin_nove3
    
    ultima_novedad = ver_novedades(novedades)
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
        ver_novedades(novedades)
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

def menu_novedades(novedades): #menu3
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
                editar_nov(novedades)
            case 3:
                en_construccion()
            case 4:
                ver_novedades(novedades)
                input("Presione Enter para continuar...")
                os.system('cls')
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

def pedir_codigo_IATA():
    codigo = input("Ingrese código IATA: ")
    while not (1 <= len(codigo) <= 3):   
        print("El código debe tener como máximo 3 caracteres")
        codigo = input("Ingrese código IATA: ")
    return codigo

def pedir_codigo_aerolinea():
    codigo = input("Ingrese código de la aerolinea: ")
    while not (1 <= len(codigo) <= 5):   
        print("El código debe tener como máximo 5 caracteres")
        codigo = input("Ingrese código de la aerolinea: ")
        codigo = codigo.upper()
    return codigo

def obtener_pos_menor(arreglo):
    pos_menor = 0
    for i in range(1, len(arreglo)):
        if arreglo[i] < arreglo[pos_menor]:
            pos_menor = i
    return pos_menor

def obtener_pos_mayor(arreglo):
    pos_mayor = 0
    for i in range(1, len(arreglo)):
        if arreglo[i] > arreglo[pos_mayor]:
            pos_mayor = i
    return pos_mayor

def crear_aereo(aerolineas):
    
    nombre_aereo = input('Ingrese el nombre del aereo. Ingrese 0 para salir\n')
    cantidad_aereo =  busquedaSecuencial(aerolineas,"",0)
    if cantidad_aereo ==-1:
        input("\nYa no se pueden cargar mas usuarios. Presione enter para continuar")
        nombre_aereo = "0"
    else:
        contadores = [0]*3
        paises = ["ARG", "BRA", "CHI"]
        while nombre_aereo != "0" and cantidad_aereo<5:
            aerolineas[cantidad_aereo][0]=pedir_codigo_aerolinea()
            aerolineas[cantidad_aereo][1]=nombre_aereo
            aerolineas[cantidad_aereo][2] = pedir_codigo_IATA()
            aerolineas[cantidad_aereo][3]= input("\nIngrese la descripcion del vuelo\n")
            codigo_pais = pedir_codigo_pais()
            aerolineas[cantidad_aereo][4]=codigo_pais

            os.system('cls')
            cantidad_aereo = cantidad_aereo+1
            nombre_aereo = input('Ingrese el nombre del aereo. Ingrese 0 para salir\n')
    
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
        print("Menor:", paises[menor], "con una cantidad de aerolineas cargada de", contadores[menor])
        print("")
    volver()


def modificar_aereo(aerolineas): #falta testear
    os.system('cls')
    
    codigo = input("Ingrese el código de la aerolínea que desea modificar (0 para salir): ")

    while codigo != "0":
        pos = busquedaSecuencial(aerolineas, codigo, 0)

        if pos == -1:
            print("⚠️  No se encontró ninguna aerolínea con ese código.")
        else:
            os.system('cls')
            print(f"Aerolínea actual:\nCódigo: {aerolineas[pos][0]}\nNombre: {aerolineas[pos][1]}\nIATA: {aerolineas[pos][2]}\nDescripción: {aerolineas[pos][3]}\nPaís: {aerolineas[pos][4]}")
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
        codigo = input("Ingrese otro código de aerolínea a modificar (0 para salir): ").upper()

    os.system('cls')
    volver()
    

def mostrar_menu_gestion_aereo():
    print("╔════════════════════════════════════════╗")
    print("║  🛩️  MENÚ DE GESTIÓN DE AEROLÍNEAS 🛩️    ║")
    print("╚════════════════════════════════════════╝\n")
    print("1) Crear Aerolínea ✈️")
    print("2) Modificar Aerolínea ✏️")
    print("3) Eliminar Aerolínea 🗑️")
    print("4) Volver al Menú Principal 🔙")

def menu_gestion_aereo(aerolineas): #menu 1
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
                crear_aereo(aerolineas)
            case 2:
                en_construccion()
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

def menu_administrador(novedades,aerolineas):
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
                menu_gestion_aereo(aerolineas)
            case 2:
                en_construccion()
            case 3:
                menu_novedades(novedades)
            case 4:
                menu_report()
            case 5:
                os.system('cls') #se borra la consola ya que la consigna dice que con salir se abandona el sistema

def menu_ceo():
    print("entro")
    
def menu_usuario():
    print("entro")
    

def cargarNovedades(novedades):
    novedades[0][0] = "por aniversario todos los vuelos tiene un %20 de descuento con cualquier medio de pago"
    novedades[0][1] = "02/10/2025"
    novedades[0][2] = "01/11/2025"

    novedades[1][0] = "cambio de tarifa referente al equipaje extra en pasajes turista"
    novedades[1][1] = "23/06/2025"
    novedades[1][2] = "23/07/2025"

    novedades[2][0] = "los vuelos con destino a Miami seran suspendidos por fuertes tormentas y posibilidad de huracan"
    novedades[2][1] = "04/08/2025"
    novedades[2][2] = "11/08/2025"

def cargarUsuarios(usuarios):
    # Inicializar matriz de 10 usuarios con 4 columnas (email, clave, rol, extra opcional)
    

    # Administrador
    usuarios[0][0] = "admin@ventaspasajes777.com"
    usuarios[0][1] = "admin123"
    usuarios[0][2] = "administrador"

    # CEOs
    usuarios[1][0] = "ceo1@ventaspasajes777.com"
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
    usuarios[6][0] = "usuario1@ventaspasajes777.com"
    usuarios[6][1] = "usuario123"
    usuarios[6][2] = "usuario"

    usuarios[7][0] = "usuario2@ventaspasajes777.com"
    usuarios[7][1] = "usuario456"
    usuarios[7][2] = "usuario"



def busquedaSecuencial (arreglo, elemento_buscado, columna):
    cant_filas = len(arreglo)
    i=0
    while i<cant_filas-1 and arreglo[i][columna]!=elemento_buscado:
        i=i+1
    if arreglo[i][columna]==elemento_buscado:
        return i
    else:
        return-1

       
def registrarse(usuarios):
    registrado = False
    mail = input("\nIngrese el mail con el que quiere registrarse o * para volver: ")
    while mail == "":
            print("\nDebe ingresar un mail")
            mail = input("\nIngrese el mail con el que quiere registrarse o * para volver: ")
    while mail != "*" and not registrado:
        posicion = busquedaSecuencial(usuarios, "", 0)
        if posicion ==-1:
            input("\nYa no se pueden cargar mas usuarios. Presione enter para continuar")
            mail = "*"
        else:
            encontrado = busquedaSecuencial(usuarios, mail, 0)
            if encontrado == -1:
                usuarios[posicion][0] = mail
                usuarios[posicion][2] = "usuario"
                contrasenia = input("Ingrese la contraseña: ")
                usuarios[posicion][1] = contrasenia
                registrado = True
            else:
                print("El mail ya fue utilizado. Intentelo nuevamente con un correo distinto")
                mail = input("\nIngrese el mail con el que quiere registrarse o * para volver: ")
                while mail == "":
                    print("\nDebe ingresar un mail")
                    mail = input("\nIngrese el mail con el que quiere registrarse o * para volver: ")
    os.system('cls')
    
    
def menu_login():
    print("╔════════════════════════════════════╗")
    print("║       🏠  INICIAR SESION  🏠       ║")
    print("╚════════════════════════════════════╝\n")
        
def login(usuarios,novedades,aerolineas):
    intentos = 3
    menu_login()
    mail_usuario = input("\nIngrese su usuario (* para volver): ")
    while intentos != 0 and mail_usuario!="*":
        contrasenia = pwinput.pwinput(prompt="Ingrese la contraseña: ")
        os.system('cls')
        posicion = busquedaSecuencial(usuarios, mail_usuario , 0)
        if posicion !=-1:
            if  contrasenia == usuarios[posicion][1]: 
                intentos = 3 
                tipo_usuario = usuarios[posicion][2]
                if tipo_usuario == "administrador":
                    menu_administrador(novedades,aerolineas)
                elif tipo_usuario == "ceo":
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
                print ("\nContraseña o usuario incorrectas, le quedan", intentos,"intentos\n" )
        menu_login()
        mail_usuario = input("Ingrese su mail: (* para volver)")
    os.system('cls')

def mostrar_primer_menu():
    print("╔════════════════════════════════════╗")
    print("║      🏠   BIENVENIDO     🏠        ║")
    print("╚════════════════════════════════════╝\n")
    print("1) Registrarse")
    print("2) Iniciar sesion")
    print("3) Salir")




#PROGRAMA PRINCIPAL
novedades = [[""] * 4 for i in range(3)] #no dice en ningun lado hasta cuantas novedades pueden ser
cargarNovedades(novedades)
usuarios = [[""] * 3 for i in range(10)]
cargarUsuarios(usuarios)
aerolineas = [[""] * 5 for i in range(5)]

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
            registrarse(usuarios)
            mostrar_primer_menu()
            opc = validar_entero()
        case 2:
            login(usuarios,novedades,aerolineas)
            mostrar_primer_menu()
            opc = validar_entero()
        case 3:
            print()
print("Cerrando programa...")
        