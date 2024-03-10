def calcular_promedio(suma, day_semana):
    return suma / day_semana if day_semana != 0 else 0

def calcular_promedio_temperaturas(temperaturas):
    for ciudad in range(len(temperaturas)):
        promedio_mensual = 0
        if len(temperaturas[ciudad]) == 0:
            print(f"No hay datos de temperaturas para {['Guayaquil', 'Quito', 'Cuenca', 'Ambato'][ciudad]}")
            continue
        for semana in range(len(temperaturas[ciudad])):
            total_temp = 0
            for dia in temperaturas[ciudad][semana]:
                total_temp += dia["temp"]
            promedio_temp = calcular_promedio(total_temp, len(temperaturas[ciudad][semana]))
            promedio_mensual += promedio_temp
            print(f"Ciudad {['Guayaquil', 'Quito', 'Cuenca', 'Ambato'][ciudad]} - Promedio de la semana {semana + 1}: {promedio_temp}")
        promedio_mensual /= len(temperaturas[ciudad])
        print(f"El promedio mensual de {['Guayaquil', 'Quito', 'Cuenca', 'Ambato'][ciudad]} es: {promedio_mensual}")

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
        [   # Semana 3
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 35},
            {"day": "Domingo", "temp": 36}
        ]
    ],
    [   # Quito
        [   # Semana 1
            {"day": "Lunes", "temp": 10},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 11},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 13}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 10},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 12}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp": 11},
            {"day": "Jueves", "temp": 10},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 12}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 10},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 12}
        ]
    ],
    [   # Cuenca
        [   # Semana 1
            {"day": "Lunes", "temp": 10},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 11},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 13}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 10},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 12}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp": 11},
            {"day": "Jueves", "temp": 10},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 12}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 10},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 12}
        ]
    ],
    [   # Ambato
        [   # Semana 1
            {"day": "Lunes", "temp": 10},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 11},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 13}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 10},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 12}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp": 11},
            {"day": "Jueves", "temp": 10},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 12}
        ],
       [   # Semana 4
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 10},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 12}
        ]
    ]
]

calcular_promedio_temperaturas(temperaturas)