
productos = [
    {
        'id': 123,
        'Nombre': 'libreta',
        'precio': 12.580,
        'id_cat': 1
    },
    {
        'id': 345,
        'Nombre': 'Jabon',
        'precio': 10.500,
        'id_cat': 2
    }
]


categorias = [
    {
        'id': 1,
        'Nombre': 'Utiles Escolares'
    },
    {
        'id': 2,
        'Nombre': 'Aseo'
    }
]


diccionario_resultante = [
 {
'id' : 123,
'Nombre' : 'libreta' ,
'categoria' : 'utiles escolares' ,
},
{
    'id' : 345 ,
    'Nombre' : 'jabon' ,
    'categoria' : 'Aseo' 
    }

]    


for producto in productos:
    id_producto = producto['id']
    nombre_producto = producto['Nombre']
    id_categoria_producto = producto['id_cat']


    nombre_categoria = None
    for categoria in categorias:
        if categoria['id'] == id_categoria_producto:
            nombre_categoria = categoria['Nombre']
            break

    resultado = {
        'id': id_producto,
        'Nombre': nombre_producto,
        'categoria': nombre_categoria
    }

    diccionario_resultante.append(resultado)


for resultado in diccionario_resultante:
    print(resultado)