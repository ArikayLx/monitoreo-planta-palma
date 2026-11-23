# Sistema de Monitoreo Industrial y Control Automatizado On-Off
**Planta Extractora de Aceite Crudo de Palma Africana (*Elaeis guineensis*)**

* **Asignatura:** Programación 1
* **Institución:** Universidad Nacional de Colombia
* **Autor:** Nery Fabian Angulo Estacio
* **Docente:** Prof. Álvaro René Córdoba
* **Ubicación:** San Andrés de Tumaco, Nariño, Colombia

---

## 📋 Descripción del Proyecto

Solución de software desarrollada en Python estándar bajo una arquitectura de procesamiento por lotes (**ETL**) para supervisar cuatro variables críticas en una planta extractora de aceite de palma africana y accionar de forma automática actuadores de seguridad mediante control lógico **On-Off**.

El sistema prioriza la seguridad humana sobre las alertas mecánicas, térmicas y ambientales, generando una bitácora histórica trazable para auditoría y mantenimiento preventivo.

### Variables Monitoreadas y Umbrales de Seguridad
| Variable Industrial | Etapa / Área | Umbral Crítico | Acción Automatizada (On-Off) |
| :--- | :--- | :--- | :--- |
| **Proximidad en Banda** | Bandas de RFF / Sinfín | `< 30.0 cm` | **Parada de Emergencia:** Relé de parada `ON` + Alarma sonora `ON` |
| **Temperatura Digestor** | Digestión y Prensado | `> 100.0 °C` | **Alerta Térmica:** Extractores `ON` |
| **Presión de Vapor** | Calderas / Esterilización | `> 3.5 bar` | **Alerta Mecánica:** Válvula de purga `ON` |
| **Humedad Relativa** | Bodega de Palmiste | `> 75.0 %` | **Alerta Ambiental:** Deshumidificador `ON` + Alarma bodega `ON` |

---

## 📁 Estructura del Repositorio

```text
├── datos/
│   └── lecturas_planta.txt       # Archivo plano con registros históricos de sensores
├── documentacion/
│   └── SISTEMA DE MONITOREO...   # Documento SRS, Manuales (APA 7.ª) y Acta de Entrega
├── resultados/
│   └── bitacora_control.txt      # Reporte de auditoría generado automáticamente
├── main.py                       # Código fuente principal y lógica de control
├── requirements.txt              # Gestión de dependencias (Librería estándar Python 3.x)
└── README.md                     # Portada y guía técnica del repositorio