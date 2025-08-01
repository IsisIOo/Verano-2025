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

# FUNCIONES
def abrir_archivo(archivo):        
    archivo= open(archivo, 'r', encoding='utf-8')
    contenido = archivo.read()
    archivo.close()
    return contenido

def separador(comuna):  
    lista = comuna.split("\n")
    largo = len(lista)
    i = 0
    while i < largo:
        lista[i] = lista[i].split(",")
        i = i + 1
    return lista

# BLOQUE PRINCIPAL

print("Seleccione el conjunto de datos que desea procesar:")
print("1. Alcalde - Conchali")
print("2. Distrito 12 - Grande")
print("3. Distrito 12 - Pequeno")
print("4. RM - Grande")
print("5. RM - Pequeno")

opcion = int(input("\nIngrese la carpeta que desea revisar: "))

carpetas = [
    "",  # índice 0 (para alinear con opciones 1-5)
    "conjunto-1-alcalde-conchali",
    "conjunto-2-distrito-12-grande",
    "conjunto-3-distrito-12-pequeño",
    "conjunto-4-RM-grande",
    "conjunto-5-RM-pequeño"
]

max_mesas_por_conjunto = [
    0,
    47,
    430,
    40,
    1000,
    100
]

if opcion >= 1 and opcion <= 5:
    carpeta = carpetas[opcion]
    max_disponibles = max_mesas_por_conjunto[opcion]
else:
    print("Opcion no valida. Por favor, elija un numero entre 1 y 5.")
    exit()

while True:
    cantidad_mesas = int(input("ingrese la cantidad de mesas que desea ver: "))
    if cantidad_mesas <= max_disponibles:
        break
    else:
        print("Error: solo hay", max_disponibles, "mesas disponibles.")
        print("Intente nuevamente con un valor valido.")

i = 1
todas_las_mesas = []

while i <= cantidad_mesas:
    nombre_archivo = carpeta + "/mesa-" + str(i) + ".txt"
    contenido = abrir_archivo(nombre_archivo)
    datos_mesa = separador(contenido)
    todas_las_mesas.append(datos_mesa)
    i = i + 1

mesas_descuadradas = 0
mesas_cuadradas = 0
lista_mesas_cuadradas = []
lista_mesas_descuadradas = []
cantidad_mesas = len(todas_las_mesas)

# Listas para almacenar los candidatos encontrados y los resultados por comuna
candidatos = []
comunas_votos = []

# Recolectar todos los candidatos SIN set ni dict
for m in range(len(todas_las_mesas)):
    mesa = todas_las_mesas[m]
    for k in range(1, len(mesa)):
        nombre = mesa[k][0]
        if nombre != "NULOS" and nombre != "BLANCOS":
            ya_esta = 0
            for c in range(len(candidatos)):
                if candidatos[c] == nombre:
                    ya_esta = 1
            if ya_esta == 0:
                candidatos.append(nombre)

# Proceso de conteo agrupado por comuna
for m in range(len(todas_las_mesas)):
    mesa = todas_las_mesas[m]
    encabezado = mesa[0]
    comuna = encabezado[0]
    nombre_mesa = encabezado[1]
    votos_emitidos = int(encabezado[2])
    print("")
    print("Comuna:", comuna, "Mesa:", nombre_mesa, "Votos Emitidos:", votos_emitidos)
    
    # Sumar votos de la mesa
    votos_totales = 0
    for k in range(1, len(mesa)):
        votos_totales = votos_totales + int(mesa[k][1])
    
    # Buscar si la comuna ya existe en comunas_votos
    idx_comuna = -1
    for i in range(len(comunas_votos)):
        if comunas_votos[i][0] == comuna:
            idx_comuna = i
    if idx_comuna == -1:
        nueva_comuna = [comuna, [], 0, 0, []]
        for c in range(len(candidatos)):
            nueva_comuna[1].append(0)
        comunas_votos.append(nueva_comuna)
        idx_comuna = len(comunas_votos) - 1

    # Si la mesa está cuadrada, sumar votos
    if votos_totales == votos_emitidos:
        mesas_cuadradas = mesas_cuadradas + 1
        lista_mesas_cuadradas.append(nombre_mesa)
        comunas_votos[idx_comuna][4].append(nombre_mesa)
        for k in range(1, len(mesa)):
            nombre = mesa[k][0]
            votos = int(mesa[k][1])
            if nombre == "NULOS":
                comunas_votos[idx_comuna][2] = comunas_votos[idx_comuna][2] + votos
            elif nombre == "BLANCOS":
                comunas_votos[idx_comuna][3] = comunas_votos[idx_comuna][3] + votos
            else:
                # Buscar el índice del candidato
                idx_cand = -1
                for p in range(len(candidatos)):
                    if candidatos[p] == nombre:
                        idx_cand = p
                if idx_cand != -1:
                    comunas_votos[idx_comuna][1][idx_cand] = comunas_votos[idx_comuna][1][idx_cand] + votos
        print("Votos totales:", votos_totales, "(correcto)")
    else:
        mesas_descuadradas = mesas_descuadradas + 1
        lista_mesas_descuadradas.append(nombre_mesa)
        print("Votos totales:", votos_totales, "(incorrecto, se esperaba", votos_emitidos, ")")

# Mostrar resultados por comuna
print("")
print("==== RESULTADOS POR COMUNA ====")
for i in range(len(comunas_votos)):
    nombre_comuna = comunas_votos[i][0]
    votos_cand = comunas_votos[i][1]
    nulos = comunas_votos[i][2]
    blancos = comunas_votos[i][3]
    mesas_cuad = comunas_votos[i][4]
    total_validos = 0
    for v in votos_cand:
        total_validos = total_validos + v
    total_emitidos = total_validos + nulos + blancos
    print("")
    print("---", nombre_comuna, "---")
    print("Total votos validos:", total_validos)
    print("Total votos emitidos (incluye nulos y blancos):", total_emitidos)
    for c in range(len(candidatos)):
        if total_emitidos > 0:
            porcentaje = round(votos_cand[c]*100.0/total_emitidos, 2)
        else:
            porcentaje = 0.0
        print(candidatos[c], ":", votos_cand[c], "votos", "(", porcentaje, "%)")
    if total_emitidos > 0:
        porcentaje_nulos = round(nulos*100.0/total_emitidos, 2)
        porcentaje_blancos = round(blancos*100.0/total_emitidos, 2)
    else:
        porcentaje_nulos = 0.0
        porcentaje_blancos = 0.0
    print("NULOS:", nulos, "votos", "(", porcentaje_nulos, "%)")
    print("BLANCOS:", blancos, "votos", "(", porcentaje_blancos, "%)")

print("")
print("Total de mesas procesadas:", cantidad_mesas)
print("Total de mesas cuadradas:", mesas_cuadradas)
print("Total de mesas descuadradas:", mesas_descuadradas)
print("")
print("==== DETALLES DE LAS MESAS ====")
print("Total de mesas cuadradas:", lista_mesas_cuadradas)
print("Total de mesas descuadradas:", lista_mesas_descuadradas)
print("")


# Generar un archivo de informe .txt para cada comuna

for i in range(len(comunas_votos)):
    nombre_comuna = comunas_votos[i][0]
    votos_cand = comunas_votos[i][1]
    nulos = comunas_votos[i][2]
    blancos = comunas_votos[i][3]
    mesas_cuad = comunas_votos[i][4]

    # Buscar todas las mesas descuadradas de esta comuna
    mesas_descuadradas_comuna = []
    for j in range(len(todas_las_mesas)):
        mesa = todas_las_mesas[j]
        encabezado = mesa[0]
        comuna = encabezado[0]
        nombre_mesa = encabezado[1]
        votos_emitidos = int(encabezado[2])
        votos_totales = 0
        for k in range(1, len(mesa)):
            votos_totales = votos_totales + int(mesa[k][1])
        if comuna == nombre_comuna and votos_totales != votos_emitidos:
            mesas_descuadradas_comuna.append(nombre_mesa)

    # Solo generar archivo si hay al menos una mesa (cuadrada o descuadrada)
    num_mesas_en_comuna = len(mesas_cuad) + len(mesas_descuadradas_comuna)
    if num_mesas_en_comuna > 0:
        texto = ""
        texto = texto + "INFORME DE VOTACION COMUNA: " + nombre_comuna + "\n\n"
        texto = texto + "Cantidad de mesas escrutadas: " + str(num_mesas_en_comuna) + "\n"
        texto = texto + "Cantidad de mesas cuadradas: " + str(len(mesas_cuad)) + "\n"
        texto = texto + "Cantidad de mesas descuadradas: " + str(len(mesas_descuadradas_comuna)) + "\n\n"

        total_validos = 0
        for v in votos_cand:
            total_validos = total_validos + v
        total_emitidos = total_validos + nulos + blancos

        texto = texto + "RESULTADOS PARCIALES (Solo mesas cuadradas):\n"
        texto = texto + "Total votos validos: " + str(total_validos) + "\n"
        texto = texto + "Total votos emitidos (incluye nulos y blancos): " + str(total_emitidos) + "\n"

        for c in range(len(candidatos)):
            if total_emitidos > 0:
                porcentaje = round(votos_cand[c]*100.0/total_emitidos, 2)
            else:
                porcentaje = 0.0
            texto = texto + candidatos[c] + ": " + str(votos_cand[c]) + " votos (" + str(porcentaje) + "%)\n"
        if total_emitidos > 0:
            porcentaje_nulos = round(nulos*100.0/total_emitidos, 2)
            porcentaje_blancos = round(blancos*100.0/total_emitidos, 2)
        else:
            porcentaje_nulos = 0.0
            porcentaje_blancos = 0.0
        texto = texto + "NULOS: " + str(nulos) + " votos (" + str(porcentaje_nulos) + "%)\n"
        texto = texto + "BLANCOS: " + str(blancos) + " votos (" + str(porcentaje_blancos) + "%)\n\n"

        texto = texto + "Listado de mesas descuadradas:\n"
        if len(mesas_descuadradas_comuna) == 0:
            texto = texto + "No hay mesas descuadradas en esta comuna.\n"
        else:
            for m in mesas_descuadradas_comuna:
                texto = texto + str(m) + "\n"

        # Guardar archivo
        nombre_archivo = "informe_" + nombre_comuna.replace(" ", "_") + ".txt"
        archivo = open(nombre_archivo, "w", encoding="utf-8")
        archivo.write(texto)
        archivo.close()


    

