# Matriz de temperaturas para Guayaquil, Quito, Cuenca, Ambato
temperaturas = [
    [   # Guayaquil
        [   # Semana 1
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 35}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 35},
            {"day": "Domingo", "temp": 36}
        ],
        # Resto de las semanas para Guayaquil...
    ],
    [   # Quito
        # Datos de temperaturas por semana para Quito...
    ],
    [   # Cuenca
        # Datos de temperaturas por semana para Cuenca...
    ],
    [   # Ambato
        # Datos de temperaturas por semana para Ambato...
    ]
]

# Calcular el promedio de temperaturas por ciudad y semana
for ciudad in range(len(temperaturas)):
    for semana in range(len(temperaturas[ciudad])):
        total_temp = 0
        for dia in temperaturas[ciudad][semana]:
            total_temp += dia["temp"]
        promedio_temp = total_temp / len(temperaturas[ciudad][semana])
        print(
            f"Promedio de temperaturas para {['Guayaquil', 'Quito', 'Cuenca', 'Ambato'][ciudad]}, Semana {semana + 1}: {promedio_temp}")
