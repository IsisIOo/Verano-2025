# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA
# SECCIÓN DEL CURSO: 0-C-2 
# PROFESOR DE TEORÍA: Hernan Cornejo
# PROFESOR DE LABORATORIO: Paulo Quinsacara
# 
# AUTOR 
# NOMBRE: Isidora Oyanedel
# RUT: 21.168.603-0
# CARRERA: Ingeniería Civil en informatica  
# DESCRIPCIÓN DEL PROGRAMA ...<CONTINÚE CON EL PROGRAMA A PARTIR DE AQUÍ>
"""
Se deberia crear un programa para poder ayudar/facilitar el conteo de votos, los cuales fueron separados en muchos
archivos y además hay algunos de estos que están mal contados, por lo que nuestro trabajo es identificar estos archivos
incorrectos y entregar los votos en un solo archivo final.
RECORDATORIO
CONCHALI (COMUNA A LA QUE PERTENCE LA MESA), 10M(NUMERO DE LA MESA), 210(CANTIDAD DE SUFRAGIOS EMITIDOS),
350(TOTAL DE PERSONAS HABILITADAS PARA SUFRAGAR EN LA MESA)

primero pensé en solo hacer la carpeta 1 ya que, pensé que podrá reutilizar el codigo para con las demás carpetas
haciendole cambios minimos, pero no me funcionó muy bien.
"""



#FUNCIONES
#funcion para abrir el archivo y correccion de letras
def abrir_archivo(archivo):        
     archivo= open(archivo, 'r', encoding='utf-8')
     contenido = archivo.read()
     archivo.close()
     return contenido


#FUNCION: Separador
#ENTRADA: String con los datos de una comuna
#SALIDA: Lista de listas, donde cada sublista contiene los datos de una mesa
#DESCRIPCIÓN:
def separador(comuna):  
     lista=comuna.split("\n")
     largo=len(lista)
     i=0
     while i<largo:
          lista[i]=lista[i].split(",")
          i=i+1
     return lista




#BLOQUE PRINCIPAL

print("Seleccione el conjunto de datos que desea procesar:")
print("1. Alcalde - Conchali")
print("2. Distrito 12 - Grande")
print("3. Distrito 12 - Pequeno")
print("4. RM - Grande")
print("5. RM - Pequeno")

#DATOS DE CADA CARPETA




opcion = int(input("\nIngrese la carpeta que desea revisar: "))

carpetas = [
    "",  # índice 0 (para alinear con opciones 1-5)
    "conjunto-1-alcalde-conchali",
    "conjunto-2-distrito-12-grande",
    "conjunto-3-distrito-12-pequeño",
    "conjunto-4-RM-grande",
    "conjunto-5-RM-pequeño"
]

# Cantidad real de mesas en cada carpeta (contadas previamente)
max_mesas_por_conjunto = [
    0,   # índice 0 vacío
    47,  # conjunto-1-alcalde-conchali
    430,  # conjunto-2-distrito-12-grande
    40,  # conjunto-3-distrito-12-pequeño
    1000, # conjunto-4-RM-grande
    100   # conjunto-5-RM-pequeño
]

if 1 <= opcion <= 5:
    carpeta = carpetas[opcion] 
    max_disponibles = max_mesas_por_conjunto[opcion]
else:
    print("Opción no válida. Por favor, elija un número entre 1 y 5. ")
    exit()

while True:
    cantidad_mesas=int(input("ingrese la cantidad de mesas que desea ver: "))

    if cantidad_mesas <= max_disponibles:
        break
    else:
        print(f"\nError: solo hay {max_disponibles} mesas disponibles.")
        print("Intente nuevamente con un valor válido.\n")

i=1
todas_las_mesas = []

#este crea la lista de listas con todos los elementos de las mesas, lee el archivo y separa los datos y luego junta todas las mesas
while i <= cantidad_mesas:
    nombre_archivo = carpeta + "/mesa-" + str(i) + ".txt"
    contenido = abrir_archivo(nombre_archivo)
    datos_mesa = separador(contenido)
    todas_las_mesas.append(datos_mesa)
    i += 1

mesas_descuadradas = 0
mesas_cuadradas = 0
lista_mesas_cuadradas = []
lista_mesas_descuadradas = []
votos_por_candidato = {}  # clave: nombre candidato, valor: votos
nulos_blancos = {"NULOS": 0, "BLANCOS": 0}  # Contador de votos nulos y blancos
total_votos_validos = 0

for mesa in todas_las_mesas:
    encabezado = mesa[0] #Encabezado con la informacion total de la mesa
    comuna = encabezado[0]
    nombre_mesa = encabezado[1]
    votos_emitidos = int(encabezado[2])
    print(f"\nComuna: {comuna}, Mesa: {nombre_mesa}, Votos Emitidos: {votos_emitidos}")

    j = 1
    votos_totales = 0

    while j < len(mesa) :
        fila = mesa[j]
        nombre = fila[0]
        votos = int(fila[1])
        #print(nombre, "→", votos)
        # esto verifica si la cantidad de votos de una mesa esta cuadrada o no, no es global
        votos_totales= votos + votos_totales
        j += 1
    

    #COMO SABEMOS QUE LA MESA ESTA CUADRADA SUMAMOS LOS VOTOS DE CADA CANDIDATO 
    if votos_totales == votos_emitidos:
        mesas_cuadradas += 1
        lista_mesas_cuadradas.append(nombre_mesa)
        print(f"Votos totales: {votos_totales} (correcto)")
        # Acumular votos de candidatos (evita NULOS y BLANCOS)
        for fila in mesa[1:]:
            nombre = fila[0]
            #print(nombre)
            votos = int(fila[1])
            if nombre == "NULOS":
                nulos_blancos["NULOS"] += votos
            elif nombre == "BLANCOS":
                nulos_blancos["BLANCOS"] += votos
            else:
                if nombre in votos_por_candidato:
                    votos_por_candidato[nombre] += votos
                else:
                    votos_por_candidato[nombre] = votos
                total_votos_validos += votos

    else:
        mesas_descuadradas += 1
        lista_mesas_descuadradas.append(nombre_mesa)
        print(f"Votos totales: {votos_totales} (incorrecto, se esperaba {votos_emitidos})")    
    
    
total_votos_emitidos = total_votos_validos + nulos_blancos["NULOS"] + nulos_blancos["BLANCOS"]

print("\n==== RESULTADOS PARCIALES ====\n")
print(f"Total votos válidos (mesas cuadradas): {total_votos_validos}\n")

# Imprime porcentajes de candidatos
for candidato, votos in votos_por_candidato.items():
    porcentaje = (votos / total_votos_emitidos) * 100
    print(f"{candidato}: {votos} votos ({porcentaje:.2f}%)")

# Imprime porcentajes de nulos y blancos
for clave in ["NULOS", "BLANCOS"]:
    votos = nulos_blancos[clave]
    porcentaje = (votos / total_votos_emitidos) * 100
    print(f"{clave}: {votos} votos ({porcentaje:.2f}%)")

#print(f"\nMesas cuadradas: {mesas_cuadradas}, Mesas descuadradas: {mesas_descuadradas}")
print(f"Total de mesas procesadas: {cantidad_mesas}")
print(f"Total de mesas cuadradas", len(lista_mesas_cuadradas))
print(f"Total de mesas descuadradas", len(lista_mesas_descuadradas))
print("\n==== DETALLES DE LAS MESAS ====\n")
print(f"Total de mesas cuadradas: {lista_mesas_cuadradas}")
print(f"Total de mesas descuadradas: {lista_mesas_descuadradas}\n")



    

