# ==============================================================================
# SISTEMA DE MONITOREO INDUSTRIAL Y CONTROL ON-OFF - EXTRACTORA DE PALMA AFRICANA
# Asignatura: Programación 1 - Universidad Nacional de Colombia
# Autor: Nery Fabian Angulo Estacio
# Docente: Prof. Álvaro René Córdoba
# ==============================================================================

# 1. DEFINICIÓN DE UMBRALES DE SEGURIDAD INDUSTRIAL (PARÁMETROS DE PLANTA)
TEMP_DIGESTOR_MAX = 100.0   # Grados Celsius (°C) - Evita quemado de aceite
PRESION_VAPOR_MAX = 3.5     # Bares (bar) - Evita sobrepresión en calderas/prensa
PROX_BANDA_MIN = 30.0       # Centímetros (cm) - Perímetro de seguridad en bandas
HUMEDAD_BODEGA_MAX = 75.0   # Porcentaje (%) - Evita fermentación del palmiste

# Rutas de archivos del sistema
RUTA_ENTRADA = "datos/lecturas_planta.txt"
RUTA_SALIDA = "resultados/bitacora_control.txt"

# Lista para almacenar los registros de auditoría
bitacora_eventos = []

# 2. EXTRACCIÓN DE DATOS DESDE ARCHIVO DE SENSORES
archivo_entrada = open(RUTA_ENTRADA, "r", encoding="utf-8")
lineas = archivo_entrada.readlines()
archivo_entrada.close()

# Encabezado del reporte de salida
bitacora_eventos.append("================================================================================\n")
bitacora_eventos.append("BITACORA DE CONTROL INDUSTRIAL - PLANTA EXTRACTORA DE ACEITE DE PALMA\n")
bitacora_eventos.append("================================================================================\n")

# 3. PROCESAMIENTO Y EVALUACIÓN DE LÓGICA ON-OFF
for linea in lineas:
    linea = linea.strip()
    if linea == "":
        continue

    datos = linea.split(",")
    timestamp = datos[0]
    temp = float(datos[1])
    presion = float(datos[2])
    prox = float(datos[3])
    humedad = float(datos[4])

    # Prioridad 1: Seguridad Humana (Invasión de perímetro en banda transportadora)
    if prox < PROX_BANDA_MIN:
        estado = "PARADA DE EMERGENCIA (SEGURIDAD HUMANA)"
        actuadores = "RELE_PARADA: ON | ALARMA_SONORA: ON"

    # Prioridad 2: Falla Térmica y de Presión Combinada en Digestor/Prensa
    elif temp > TEMP_DIGESTOR_MAX and presion > PRESION_VAPOR_MAX:
        estado = "ALERTA CRITICA (SOBRETEMPERATURA Y SOBREPRESION)"
        actuadores = "EXTRACTORES: ON | PURGA_VAPOR: ON | ALARMA: ON"

    # Prioridad 3: Sobretemperatura en Digestor
    elif temp > TEMP_DIGESTOR_MAX:
        estado = "ADVERTENCIA TERMICA (DIGESTOR > 100 C)"
        actuadores = "EXTRACTORES: ON | PURGA_VAPOR: OFF"

    # Prioridad 4: Sobrepresión en Línea de Vapor
    elif presion > PRESION_VAPOR_MAX:
        estado = "ADVERTENCIA MECANICA (PRESION > 3.5 bar)"
        actuadores = "PURGA_VAPOR: ON | EXTRACTORES: OFF"

    # Prioridad 5: Exceso de Humedad en Bodega de Palmiste
    elif humedad > HUMEDAD_BODEGA_MAX:
        estado = "ALERTA AMBIENTAL (HUMEDAD BODEGA > 75%)"
        actuadores = "DESHUMIDIFICADOR: ON | ALARMA_BODEGA: ON"

    # Operación dentro de rangos nominales
    else:
        estado = "OPERACION NORMAL"
        actuadores = "TODOS LOS ACTUADORES EN REPOSO (OFF)"

    registro = (
        f"[{timestamp}] T:{temp}°C | P:{presion}bar | Prox:{prox}cm | H:{humedad}% "
        f"--> {estado} | Accion: [{actuadores}]\n"
    )
    bitacora_eventos.append(registro)

# 4. CARGA DE RESULTADOS EN BITÁCORA DE AUDITORÍA
archivo_salida = open(RUTA_SALIDA, "w", encoding="utf-8")
archivo_salida.writelines(bitacora_eventos)
archivo_salida.close()

print("Proceso de monitoreo completado con exito.")
print(f"Total de lecturas procesadas: {len(lineas)}")
print(f"Bitacora generada en: {RUTA_SALIDA}")