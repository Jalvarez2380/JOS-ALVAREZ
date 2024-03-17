# Diccionario

informacion_personal = {
    'nombre':'José',
    'edad':44,
    'ciudad':'Guayas',
    'provincia':'Guayaquil',
}
print('----------------------')
print('Diccionario Original')
print('----------------------')
for clave, valor in informacion_personal.items():
    print(f'{clave} : {valor}')

# Clave "ciudad" y modifícalo con una ciudad diferente.
informacion_personal['ciudad'] = 'Machala'
informacion_personal['provincia'] = 'El Oro'

# Nueva clave-valor al diccionario "profesion"
informacion_personal['Pasatiempo'] = 'tocar piano'

# Verifica si la clave "telefono" existe
if 'telefono' not in informacion_personal:
    informacion_personal['telefono'] = '0999772225'

# Elimina la clave "edad" del diccionario
# del informacion_personal['edad']
informacion_personal.pop('edad')

print('----------------------')
print('Diccionario Modificado')
print('----------------------')
for clave, valor in informacion_personal.items():
    print(f'{clave} : {valor}')