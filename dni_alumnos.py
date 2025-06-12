# A. Operaciones con DNIs
print("-----A. Operaciones con DNIs-----")
print("Ingresando DNIs de los alumnos... ")
# DNI alumnos
# Diccionario de los DNIs (reales o ficticios).
dni_alumnos = {
    'molina': "31476619",
    'mele': "36552513",
    'martinez': "39964587",
    'meshler': "34433376",
    'masseroni': "39600348",
    'martilotta': "42095856"
}
# Imprimiendo Dnis
for apellido, dni in dni_alumnos.items():
    print(f"{str.capitalize(apellido)}: {dni}")

print("\nGeneración de los conjuntos de dígitos únicos...")
# Conjuntos de dígitos únicos de los DNIs generados automaticamente
conjuntos_dni_alumnos = {}
for apellido, dni in dni_alumnos.items():
    conjuntos_dni_alumnos[apellido] = set(dni) 

# Imprimiendo diccionario de conjuntos
for apellido, conjunto in conjuntos_dni_alumnos.items():
    print(f"{str.capitalize(apellido)}: {conjunto}")

# Función para sumar los dígitos de un DNI
def suma_digitos_dni(dni):
    suma = 0  # Inicializamos la suma en 0
    for digito in dni:  # Recorremos cada carácter del DNI
        suma += int(digito)  # Convertimos el carácter en número y lo sumamos
    return suma

# Función para encontrar la intersección de dos conjuntos
def interseccion_conjuntos(conjunto1, conjunto2):
    conjunto_interseccion = []
    for i in conjunto1:
        if i in conjunto2 and i not in conjunto_interseccion:
            conjunto_interseccion.append(i)
    return conjunto_interseccion
    
# Operacion unir conjuntos
def menu_union(conjuntos_dni_alumnos):
    # Funcion para unir dos conjuntos
    def union_conjuntos(conjunto1, conjunto2):
        conjunto_union = []
        for i in conjunto1:
            if i not in conjunto_union:
                conjunto_union.append(i)

        for i in conjunto2:
            if i not in conjunto_union:
                conjunto_union.append(i)
        return conjunto_union

    print("\n-----1 - Union de conjuntos-----")
    # Vista de las uniones de los conjuntos de molina con los demás
    for apellido, conjunto in conjuntos_dni_alumnos.items():
        if apellido == 'molina':
            continue
        else:
         print(f"Unión de Molina y {str.capitalize(apellido)}: {union_conjuntos(conjuntos_dni_alumnos['molina'], conjunto)}")

def menu_interseccion(conjuntos_dni_alumnos):
    
    print("\n-----2 - Intersección de conjuntos-----")
    for apellido, conjunto in conjuntos_dni_alumnos.items():
        if apellido == 'molina':
            continue
        else:
         print(f"Intersección de Molina y {str.capitalize(apellido)}: {interseccion_conjuntos(conjuntos_dni_alumnos['molina'], conjunto)}") 

def menu_diferencia(conjuntos_dni_alumnos):
    # Función para encontrar la diferencia entre dos conjuntos
    def diferencia_entre_pares(conjunto1, conjunto2):
        conjunto_diferencia = []
        for i in conjunto1:
            if i not in conjunto2 and i not in conjunto_diferencia:
                conjunto_diferencia.append(i)
        return conjunto_diferencia
    
    print("\n-----3 - Diferencia entre pares de conjuntos-----")
    # Vista de las diferencias entre los conjuntos de molina con los demás
    for apellido, conjunto in conjuntos_dni_alumnos.items():
        if apellido == 'molina':
            continue
        else:
         print(f"Diferencia de Molina y {str.capitalize(apellido)}: {diferencia_entre_pares(conjuntos_dni_alumnos['molina'], conjunto)}")

def menu_diferencia_simetrica(conjuntos_dni_alumnos):
    # Función para encontrar la diferencia simétrica entre dos conjuntos
    def diferencia_simetrica(conjunto1, conjunto2):
        conjunto_diferencia_simetrica = []
        for i in conjunto1:
            if i not in conjunto2 and i not in conjunto_diferencia_simetrica:
                conjunto_diferencia_simetrica.append(i)
        
        for i in conjunto2:
            if i not in conjunto1 and i not in conjunto_diferencia_simetrica:
                conjunto_diferencia_simetrica.append(i)
        
        return conjunto_diferencia_simetrica

    print("\n-----4 - Diferencia simétrica-----")
    # Vista de las diferencias simétricas entre los conjuntos de molina con los demás
    for apellido, conjunto in conjuntos_dni_alumnos.items():
        if apellido == 'molina':
            continue
        else:
         print(f"Diferencia simétrica entre Molina y {str.capitalize(apellido)}: {diferencia_simetrica(conjuntos_dni_alumnos['molina'], conjunto)}")

def menu_frecuencia(dni_alumnos):
    # Conteo de frecuencia de cada dígito en cada DNI utilizando estructuras repetitivas
    def contar_frecuencia_dni(dni):
        frecuencia = {}  # Diccionario aux para almacenar la frecuencia de cada dígito
        for digito in dni:  # Recorremos cada carácter del DNI
            if digito in frecuencia: # Si el dígito ya está en el diccionario
                frecuencia[digito] += 1  # Incrementamos la cuenta si ya existe
            else:
                frecuencia[digito] = 1  # Si no existe, lo inicializamos en 1
        return frecuencia

    print("\n-----5 - Frecuencia de cada dígito en los DNI-----")
    # Imprimimos la frecuencia de cada dígito en los DNIs
    for apellido, dni in dni_alumnos.items():
        frecuencias = contar_frecuencia_dni(dni)
        # Ordenamos las frecuencias por dígito para mejor presentación
        frecuencias_ordenadas = sorted(frecuencias.items())
        
        print(f"# {str.capitalize(apellido)} (DNI: {dni}):")
        for digito, count in frecuencias_ordenadas:
            print(f"   Dígito {digito}: aparece {count} {'vez' if count == 1 else 'veces'}")
        print()  # Espacio entre alumnos

def menu_suma_digitos(dni_alumnos):
    
    print("\n-----6 - Suma total dígitos DNI-----")
    # Imprimimos la suma de los dígitos de cada DNI
    for apellido, dni in dni_alumnos.items():
        print(f"Suma de los dígitos del DNI de {str.capitalize(apellido)}: {suma_digitos_dni(dni)}")

def menu_digito_compartido(conjuntos_dni_alumnos):
    # Dígito compartido entre todos los conjuntos
    def digitos_compartidos(conjunto1, conjunto2, conjunto3, conjunto4, conjunto5, conjunto6):
        conjunto_digitos_compartidos = []  # Usamos un conjunto para almacenar los dígitos compartidos

        for digito in "0123456789":  # Recorremos los dígitos del 0 al 9
            if digito in conjunto1 and digito in conjunto2 and digito in conjunto3 and digito in conjunto4 and digito in conjunto5 and digito in conjunto6:
                conjunto_digitos_compartidos.append(digito)  # Si el dígito está en todos los conjuntos, lo añadimos
        return conjunto_digitos_compartidos  # Devolvemos el conjunto de dígitos compartidos

    print("\n-----7 - Evaluacion lógica: Dígito compartido-----")
    print("Dígito compartido entre todos los conjuntos:", digitos_compartidos(conjuntos_dni_alumnos['molina'], conjuntos_dni_alumnos['mele'], conjuntos_dni_alumnos['martinez'], conjuntos_dni_alumnos['meshler'], conjuntos_dni_alumnos['masseroni'], conjuntos_dni_alumnos['martilotta']))

def menu_diversidad_alta(conjuntos_dni_alumnos):
    # Diversidad numérica alta si tiene mas de 6 digitos únicos
    def diversidad_numerica_alta(conjunto):
        if len(conjunto) > 6:  # Si el conjunto tiene más de 6 dígitos únicos
            return "Diversidad Numerica Alta"
        else:
            return "Diversidad Numerica Baja"

    print("\n-----8 - Evaluacion lógica: Diversidad numérica-----")
    # Imprimimos la diversidad numérica de cada conjunto único
    for apellido, conjunto in conjuntos_dni_alumnos.items():  
        print(f"DNI de {str.capitalize(apellido)}: {diversidad_numerica_alta(conjunto)}")

def menu_suma_total_digitos_dni(dni_alumnos):
    # Existe al menos un par de DNIs cuyo total de la suma de los dígitos es igual.
    def buscar_pares_dni(dnis):  # Definimos una función que recibe una lista de DNIs
        suma_dict = {}  # Creamos un diccionario vacío para almacenar las sumas de los dígitos

        for dni in dnis:  # Recorremos cada DNI en la lista
            total = suma_digitos_dni(dni)  # Calculamos la suma de los dígitos del DNI actual con la función suma_digitos_dni
            if total in suma_dict:  # Si ya existe una suma igual en el diccionario...
                suma_dict[total].append(dni)  # Agregamos el DNI a la lista de DNIs con la misma suma
            else:  # Si es la primera vez que encontramos esta suma...
                suma_dict[total] = [dni]  # Creamos una nueva entrada en el diccionario con la suma como clave

        for total, dni_lista in suma_dict.items():  # Recorremos el diccionario para buscar coincidencias
            if len(dni_lista) > 1:  # Si hay más de un DNI con la misma suma...
                print(f"DNI con suma {total}: {', '.join(dni_lista)}")  # Imprimimos los DNIs que tienen la misma suma de dígitos

    # Lista de DNIs
    #dnis = [dni_molina, dni_mele, dni_martinez, dni_meshler, dni_masseroni, dni_martilotta]

    print("\n-----9 - Evaluacion lógica: Pares de dni con mismo valor en la suma de sus dígitos-----")
    buscar_pares_dni(dni_alumnos.values())  # Llamamos a la función para buscar pares de DNIs con sumas iguales

def menu_compatibilidad_dnis(conjuntos_dni_alumnos):
    # El conjunto A y el conjunto B se consideran altamente compatibles si tienen tres o más dígitos en común.
    def alta_compatibilidad(nombre1, conjunto1, nombre2, conjunto2):
        interseccion = interseccion_conjuntos(conjunto1, conjunto2)  # Usamos la función de intersección definida anteriormente
        if len(interseccion) >= 3:  # Si la intersección tiene 3 o más dígitos...
            return f"El {nombre1} tiene alta compatibilidad con el {nombre2}"
        else:  # Si hay menos de 3 elementos en común...
            return f"El {nombre1} tiene baja compatibilidad con el {nombre2}"

    print("\n-----10-Compatibilidad entre conjuntos de DNIs-----")
    # Comprobamos la compatibilidad entre el conjunto de Molina y los demás conjuntos
    print("Compatibilidad:", alta_compatibilidad("conjunto Molina", conjuntos_dni_alumnos['molina'], "conjunto Mele", conjuntos_dni_alumnos['mele']))

# B. Operaciones con años de nacimiento
#print("\n-----B. Operaciones con años de nacimiento-----")

# Creamos un diccionario con los años de nacimiento de los alumnos
anios_nacimiento = {
    "Molina": 1985,
    "Mele": 1991,
    "Martinez": 1997,
    "Meshler": 1989,
    "Masseroni": 1996,
    "Martilotta": 1999
}

# Obtenemos los años de nacimiento en una lista
lista_anios = list(anios_nacimiento.values())

def menu_cant_anios_pares_impares(lista_anios):
    # Contar cuántos nacieron en años pares e impares utilizando estructuras repetitivas.
    pares = 0
    for anio in lista_anios:
        if anio % 2 == 0:
            pares += 1

    impares = len(lista_anios) - pares

    print("\n-----11 - Cantidad de años pares e impares-----")
    print(f"Cantidad de alumnos nacidos en años pares: {pares}")
    print(f"Cantidad de alumnos nacidos en años impares: {impares}")

def menu_grupo_z_u_old_school(lista_anios):
    print("\n-----12-Grupo Z u Old School-----")
    # Si todos nacieron después del 2000, mostrar "Grupo Z".
    es_grupo_z = True

    for anio in lista_anios:
        if anio <= 2000:
            es_grupo_z = False
            break

    if es_grupo_z:
        print("Tenemos un Grupo Z")
    else:
        print("Tenemos un Grupo Old School")

def menu_verifica_bisiesto(lista_anios):
    print("\n-----13 - Verifica año bisiesto-----")
    # Implementar una función para determinar si un año es bisiesto.
    def es_bisiesto(anio):
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            return True
        return False

    # Si alguno nació en año bisiesto, mostrar "Tenemos un año especial".
    for anio in lista_anios:
        if es_bisiesto(anio):
            print(f"Tenemos un año especial: {anio}")
            break  # Detiene el ciclo en cuanto encuentra un año bisiesto

def menu_prod_cartesiano_anios_edades(anios_nacimiento):
    print("\n-----14 - Producto cartesiano años y edades-----")
    # Calculamos las edades 
    anio_actual = 2025
    edades = {} 
    for nombre, anio in anios_nacimiento.items():
        edades[nombre] = anio_actual - anio
    # Producto cartesiano: cada persona con su año de nacimiento y edad
    print("Relación entre años de nacimiento y edades:")
    for nombre in anios_nacimiento:
        print(f"{nombre} nació en {anios_nacimiento[nombre]} y tiene {edades[nombre]} años.")

################## MENU #############################
opciones = {
    '1': lambda: menu_union(conjuntos_dni_alumnos),
    '2': lambda: menu_interseccion(conjuntos_dni_alumnos),
    '3': lambda: menu_diferencia(conjuntos_dni_alumnos),
    '4': lambda: menu_diferencia_simetrica(conjuntos_dni_alumnos),
    '5': lambda: menu_frecuencia(dni_alumnos),
    '6': lambda: menu_suma_digitos(dni_alumnos),
    '7': lambda: menu_digito_compartido(conjuntos_dni_alumnos),
    '8': lambda: menu_diversidad_alta(conjuntos_dni_alumnos),
    '9': lambda: menu_suma_total_digitos_dni(dni_alumnos),
    '10': lambda: menu_compatibilidad_dnis(conjuntos_dni_alumnos),
    '11': lambda: menu_cant_anios_pares_impares(lista_anios),
    '12': lambda: menu_grupo_z_u_old_school(lista_anios),
    '13': lambda: menu_verifica_bisiesto(lista_anios),
    '14': lambda: menu_prod_cartesiano_anios_edades(anios_nacimiento)
}

while True:
    ver_menu = input("\n¿Desea ver el menú? (S/N): ").lower()
    if ver_menu == 's':
        print("\n***MENU EJERCICIOS TP INTEGRDOR II***")
        print("--- A. Operaciones con DNIs ---")
        print("1 - Union de conjuntos")
        print("2 - Intersección de conjuntos")
        print("3 - Diferencia entre pares de conjuntos")
        print("4 - Diferencia simétrica")
        print("5 - Frecuencia de cada dígito en los DNI")
        print("6 - Suma total dígitos DNI")
        print("7 - Evaluacion lógica: Dígito compartido")
        print("8 - Evaluacion lógica: Diversidad numérica")
        print("9 - Evaluacion lógica: Pares de dni con mismo valor en la suma de sus dígitos")
        print("10 - Compatibilidad entre conjuntos de DNI")
        print("--- B. Operaciones con años de nacimiento ---")
        print("11 - Cantidad de años pares e impares")
        print("12 - Grupo Z u Old School")
        print("13 - Verifica año bisiesto")
        print("14 - Producto cartesiano años y edades")
        print("0 - Salir")
        opcion = input("Ingese una opción: ")
        if opcion == '0':
            break

        if opcion in opciones:
            opciones[opcion]()
    else:
        exit()